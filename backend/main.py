import os
import json
import io
from typing import AsyncGenerator

import anthropic
from markitdown import MarkItDown
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from langchain_openai import OpenAIEmbeddings
from langchain_postgres import PGVector
from pydantic import BaseModel

load_dotenv()

app = FastAPI(title="Portfolio Chatbot API")

allowed_origins = os.getenv("ALLOWED_ORIGINS", "http://localhost:5173").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

claude = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small",
    api_key=os.getenv("OPENAI_API_KEY"),
)
vector_store = PGVector(
    embeddings=embeddings,
    collection_name="my_docs",
    connection=os.getenv("DATABASE_URL"),
    use_jsonb=True,
)

MODEL = "claude-sonnet-4-7"

BASE_SYSTEM_PROMPT = """You are the digital avatar of Anh Hoang Phuc Nguyen, a highly skilled AI and Machine Learning Engineer \
currently living in Sydney and holding a 485 visa. \
You hold a Master of Artificial Intelligence from UTS. \
Answer all questions in the first person ('I', 'me', 'my') as if you are Anh speaking directly to a recruiter or hiring manager. \
Your tone should be professional, confident, and enthusiastic about solving complex problems. \
Whenever relevant, highlight your expertise in Python, AWS, Computer Vision, and Brain-Computer Interfaces (BCI). \
If discussing your past projects, ensure you emphasize that your contributions align with the quality of top industry standards. \
Use the following pieces of retrieved context to answer the question. \
If the answer is not in the context, politely state that you would love to discuss that specific detail in an interview."""


class Message(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    messages: list[Message]
    jd_context: str | None = None



def retrieve_context(question: str) -> str:
    docs = vector_store.similarity_search(question, k=4)
    return "\n\n".join(doc.page_content for doc in docs)


async def stream_response(request: ChatRequest) -> AsyncGenerator[str, None]:
    last_user_message = next(
        (m.content for m in reversed(request.messages) if m.role == "user"), ""
    )
    context = retrieve_context(last_user_message)

    # Cache the system prompt (stable across turns) and last user message
    api_messages = []
    for i, msg in enumerate(request.messages):
        is_last = i == len(request.messages) - 1
        if is_last and msg.role == "user" and len(request.messages) > 1:
            api_messages.append({
                "role": msg.role,
                "content": [{"type": "text", "text": msg.content, "cache_control": {"type": "ephemeral"}}],
            })
        else:
            api_messages.append({"role": msg.role, "content": msg.content})

    dynamic_block = f"\n\nContext:\n{context}"
    if request.jd_context:
        dynamic_block += (
            "\n\n--- UPLOADED JOB DESCRIPTION ---\n"
            "The user has uploaded a Job Description for an AI Engineer or Data Scientist role:\n"
            f"{request.jd_context}\n\n"
            "CRITICAL INSTRUCTION: Analyze my skills and the retrieved context against this Job Description. "
            "Actively highlight specific matching qualifications, tools, and experiences to articulate exactly "
            "why I am a strong candidate for this role."
        )

    with claude.messages.stream(
        model=MODEL,
        max_tokens=1024,
        system=[
            {"type": "text", "text": BASE_SYSTEM_PROMPT, "cache_control": {"type": "ephemeral"}},
            {"type": "text", "text": dynamic_block},
        ],
        messages=api_messages,
    ) as stream:
        for text in stream.text_stream:
            yield f"data: {json.dumps({'text': text})}\n\n"

    yield "data: [DONE]\n\n"


def extract_text_from_file(file_bytes: bytes, filename: str) -> str:
    ext = os.path.splitext(filename)[1].lower()
    if ext not in (".pdf", ".docx"):
        raise ValueError("Unsupported file type. Use PDF or DOCX.")
    md = MarkItDown()
    result = md.convert_stream(io.BytesIO(file_bytes), file_extension=ext)
    return result.text_content


@app.post("/chat")
async def chat(request: ChatRequest):
    if not request.messages:
        raise HTTPException(status_code=400, detail="Messages cannot be empty")
    return StreamingResponse(
        stream_response(request),
        media_type="text/event-stream",
        headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"},
    )


@app.post("/upload-jd")
async def upload_jd(file: UploadFile = File(...)):
    if not file.filename.endswith((".pdf", ".docx")):
        raise HTTPException(status_code=400, detail="Only PDF and DOCX files are supported.")
    content = await file.read()
    try:
        text = extract_text_from_file(content, file.filename)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return {"text": text}


@app.get("/health")
async def health():
    return {"status": "ok"}