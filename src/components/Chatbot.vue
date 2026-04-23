<template>
    <div class="fixed bottom-20 right-4 z-50 flex flex-col items-end">
        <!-- Chat panel -->
        <transition name="chat-slide">
            <div
                v-if="isOpen"
                class="mb-3 w-80 rounded-2xl shadow-2xl overflow-hidden flex flex-col"
                style="height: 460px; background: rgba(17,24,39,0.97); border: 1px solid rgba(59,130,246,0.3);"
            >
                <!-- Header -->
                <div class="flex items-center justify-between px-4 py-3 bg-linear-to-r from-blue-600 to-cyan-600">
                    <div class="flex items-center gap-2">
                        <div class="w-2 h-2 rounded-full bg-green-400 animate-pulse"></div>
                        <span class="text-white font-semibold text-sm">Chat with Phuc's AI</span>
                    </div>
                    <button @click="isOpen = false" class="text-white/70 hover:text-white text-lg leading-none">✕</button>
                </div>

                <!-- JD context banner -->
                <div v-if="jdLoaded" class="flex items-center gap-2 px-4 py-1.5 bg-green-900/40 border-b border-green-700/40 text-xs text-green-300">
                    <span>📄</span>
                    <span class="flex-1 truncate">JD loaded — asking about job fit</span>
                    <button @click="clearJd" class="text-green-400 hover:text-green-200">✕</button>
                </div>

                <!-- Messages -->
                <div ref="messagesEl" class="flex-1 overflow-y-auto px-4 py-3 space-y-3">
                    <div
                        v-for="(msg, i) in messages"
                        :key="i"
                        :class="msg.role === 'user' ? 'flex justify-end' : 'flex justify-start'"
                    >
                        <div
                            :class="[
                                'max-w-[78%] px-3 py-2 rounded-2xl text-sm leading-relaxed',
                                msg.role === 'user'
                                    ? 'bg-linear-to-r from-blue-600 to-cyan-600 text-white rounded-br-sm'
                                    : 'bg-gray-700 text-gray-100 rounded-bl-sm prose prose-sm prose-invert max-w-none'
                            ]"
                        >
                            <span v-if="msg.role === 'user'">{{ msg.content }}</span>
                            <span v-else>
                                <span v-html="renderMarkdown(msg.content)"></span>
                                <span v-if="msg.streaming" class="inline-block w-1.5 h-3.5 bg-gray-300 ml-0.5 animate-pulse align-middle"></span>
                            </span>
                        </div>
                    </div>
                    <!-- Thinking dots -->
                    <div v-if="isThinking" class="flex justify-start">
                        <div class="bg-gray-700 text-gray-100 px-3 py-2 rounded-2xl rounded-bl-sm text-sm">
                            <span class="inline-flex gap-1">
                                <span class="w-1.5 h-1.5 bg-gray-400 rounded-full animate-bounce" style="animation-delay:0ms"></span>
                                <span class="w-1.5 h-1.5 bg-gray-400 rounded-full animate-bounce" style="animation-delay:150ms"></span>
                                <span class="w-1.5 h-1.5 bg-gray-400 rounded-full animate-bounce" style="animation-delay:300ms"></span>
                            </span>
                        </div>
                    </div>
                </div>

                <!-- Input -->
                <div class="px-3 py-3 border-t border-gray-700">
                    <!-- JD upload error -->
                    <p v-if="uploadError" class="text-red-400 text-xs mb-2 px-1">{{ uploadError }}</p>
                    <form @submit.prevent="sendMessage" class="flex gap-2 items-center">
                        <!-- JD upload button -->
                        <label
                            class="w-8 h-8 rounded-full flex items-center justify-center cursor-pointer transition-colors shrink-0"
                            :class="jdLoaded ? 'bg-green-600 text-white' : 'bg-gray-700 text-gray-400 hover:bg-gray-600'"
                            title="Upload Job Description (PDF or DOCX)"
                        >
                            <span class="text-sm">📎</span>
                            <input
                                type="file"
                                accept=".pdf,.docx"
                                class="hidden"
                                @change="uploadJd"
                                :disabled="isUploading"
                            />
                        </label>
                        <input
                            v-model="input"
                            type="text"
                            placeholder="Ask me anything..."
                            class="flex-1 bg-gray-800 text-gray-100 text-sm rounded-full px-4 py-2 outline-none border border-gray-600 focus:border-blue-500 placeholder-gray-500 transition-colors"
                            :disabled="isStreaming"
                        />
                        <button
                            type="submit"
                            :disabled="!input.trim() || isStreaming || isThinking"
                            class="w-9 h-9 rounded-full bg-gradient-to-r from-blue-600 to-cyan-600 text-white flex items-center justify-center disabled:opacity-40 transition-opacity shrink-0"
                        >
                            ➤
                        </button>
                    </form>
                </div>
            </div>
        </transition>

        <!-- Bubble button -->
        <button
            @click="toggleChat"
            class="w-14 h-14 rounded-full bg-linear-to-r from-blue-600 to-cyan-600 text-white shadow-lg flex items-center justify-center text-2xl transition-transform hover:scale-110 active:scale-95"
        >
            <span v-if="!isOpen">💬</span>
            <span v-else class="text-lg">✕</span>
        </button>
    </div>
</template>

<script setup>
import { ref, nextTick } from 'vue';
import { marked } from 'marked';

marked.setOptions({ breaks: true, gfm: true });

function renderMarkdown(text) {
    return marked.parse(text || '');
}

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

const isOpen = ref(false);
const input = ref('');
const isThinking = ref(false);
const isStreaming = ref(false);
const isUploading = ref(false);
const uploadError = ref('');
const messagesEl = ref(null);
const jdContext = ref('');
const jdLoaded = ref(false);

// history stores {role, content} for both display and API
const messages = ref([
    { role: 'assistant', content: "Hi! I'm Phuc's AI assistant. Ask me anything about his skills, experience, or projects 👋\n\nYou can also upload a Job Description (📎) to see how well Phuc fits the role!" }
]);

async function scrollToBottom() {
    await nextTick();
    if (messagesEl.value) messagesEl.value.scrollTop = messagesEl.value.scrollHeight;
}

async function uploadJd(event) {
    const file = event.target.files?.[0];
    if (!file) return;
    event.target.value = '';
    uploadError.value = '';
    isUploading.value = true;

    try {
        const formData = new FormData();
        formData.append('file', file);
        const res = await fetch(`${API_URL}/upload-jd`, { method: 'POST', body: formData });
        if (!res.ok) {
            const err = await res.json();
            throw new Error(err.detail || 'Upload failed');
        }
        const data = await res.json();
        jdContext.value = data.text;
        jdLoaded.value = true;
    } catch (e) {
        uploadError.value = e.message;
    } finally {
        isUploading.value = false;
    }
}

function clearJd() {
    jdContext.value = '';
    jdLoaded.value = false;
}

async function sendMessage() {
    const text = input.value.trim();
    if (!text || isStreaming.value || isThinking.value) return;

    messages.value.push({ role: 'user', content: text });
    input.value = '';
    await scrollToBottom();

    isThinking.value = true;
    await scrollToBottom();

    // Build API payload from conversation history (exclude streaming flag)
    const apiMessages = messages.value
        .filter(m => !m.streaming)
        .map(m => ({ role: m.role, content: m.content }));

    try {
        const res = await fetch(`${API_URL}/chat`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                messages: apiMessages,
                jd_context: jdContext.value || null,
            }),
        });

        if (!res.ok) {
            throw new Error(`Server error ${res.status}`);
        }

        isThinking.value = false;
        isStreaming.value = true;

        // Add empty streaming message
        messages.value.push({ role: 'assistant', content: '', streaming: true });
        const botMsgIndex = messages.value.length - 1;
        await scrollToBottom();

        const reader = res.body.getReader();
        const decoder = new TextDecoder();
        let buffer = '';

        while (true) {
            const { done, value } = await reader.read();
            if (done) break;

            buffer += decoder.decode(value, { stream: true });
            const lines = buffer.split('\n');
            buffer = lines.pop(); // keep incomplete line

            for (const line of lines) {
                if (!line.startsWith('data: ')) continue;
                const payload = line.slice(6);
                if (payload === '[DONE]') break;
                try {
                    const { text: chunk } = JSON.parse(payload);
                    messages.value[botMsgIndex].content += chunk;
                    await scrollToBottom();
                } catch {
                    // ignore parse errors
                }
            }
        }

        messages.value[botMsgIndex].streaming = false;
    } catch (e) {
        isThinking.value = false;
        messages.value.push({ role: 'assistant', content: "Sorry, I couldn't connect to the server. Please try again later." });
    } finally {
        isStreaming.value = false;
        await scrollToBottom();
    }
}

function toggleChat() {
    isOpen.value = !isOpen.value;
    if (isOpen.value) nextTick(scrollToBottom);
}
</script>

<style scoped>
.chat-slide-enter-active,
.chat-slide-leave-active {
    transition: opacity 0.2s ease, transform 0.2s ease;
}
.chat-slide-enter-from,
.chat-slide-leave-to {
    opacity: 0;
    transform: translateY(12px) scale(0.97);
}

/* Markdown styles inside bot bubbles */
:deep(.prose p) { margin: 0 0 0.4em; }
:deep(.prose p:last-child) { margin-bottom: 0; }
:deep(.prose strong) { color: #e2e8f0; font-weight: 600; }
:deep(.prose em) { color: #cbd5e1; }
:deep(.prose h1, .prose h2, .prose h3) { color: #f1f5f9; font-weight: 600; margin: 0.5em 0 0.25em; font-size: 0.95em; }
:deep(.prose ul, .prose ol) { padding-left: 1.2em; margin: 0.3em 0; }
:deep(.prose li) { margin: 0.15em 0; }
:deep(.prose code) { background: rgba(0,0,0,0.3); padding: 0.1em 0.3em; border-radius: 3px; font-size: 0.85em; }
:deep(.prose pre) { background: rgba(0,0,0,0.4); padding: 0.6em; border-radius: 6px; overflow-x: auto; margin: 0.4em 0; }
:deep(.prose a) { color: #60a5fa; text-decoration: underline; }
:deep(.prose hr) { border-color: rgba(255,255,255,0.15); margin: 0.5em 0; }
</style>