<template>
    <section class="relative py-20 overflow-hidden" id="experience">
        <div class="relative z-10 max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center mb-16" data-aos="fade-up">
                <h2 class="text-4xl md:text-5xl font-bold text-white mb-4 flex items-center justify-center gap-3">
                    <BriefcaseIcon class="w-8 h-8 text-cyan-400"/>
                    <span class="text-transparent bg-clip-text bg-linear-to-r from-blue-400 to-cyan-400">
                        Work Experience
                    </span>
                </h2>
            </div>
                <div data-aos="fade-right">
                    <div class="space-y-8">
                        <div
                        v-for="exp in experiences"
                        :key="exp.id"
                        class="relative pl-8 border-l-2 group"
                        :class="exp.borderColor">
                        <div
                        class="absolute -left-2 top-0 w-4 h-4 rounded-full
                        group-hover:scale-150 transition-transform duration-300"
                        :class="exp.dotColor">
                        </div>
                        <div class="bg-linear-to-br from-gray-800/50
                        to-blue-900/30 rounded-2xl p-6 border
                        backdrop-blur-sm group-hover:border-blue-400/40
                        transition-all duration-300"
                        :class="exp.borderClass">
                        <div class="flex flex-col sm:flex-row sm:items-center
                        sm:justify-between mb-3">
                            <h4 class="text-lg font-bold text-white">{{ exp.position }}</h4>
                            <span
                            :class="exp.dateColor"
                            class="mt-1 sm:mt-0"
                            >{{ exp.period }}</span>
                        </div>
                        <p
                        :class="exp.companyColor" 
                        class="font-medium mb-3">{{ exp.company }}</p>
                        <p
                        class="text-blue-100 text-sm leading-relaxed whitespace-pre-line"
                        v-html="exp.desc"></p>
                        <div v-if="exp.techStack?.length" class="flex flex-wrap gap-2 mt-4">
                            <span
                            v-for="tech in exp.techStack"
                            :key="tech"
                            class="px-3 py-1 bg-blue-500/10 border border-blue-400/20 rounded-full text-blue-300 text-xs font-medium">
                                {{ tech }}
                            </span>
                        </div>
                        </div>
                        </div>
                </div>
            </div>
        </div>
    </section>
</template>

<script setup>
import { BriefcaseIcon, Squares2X2Icon } from '@heroicons/vue/16/solid';


const experiences = [
    {
        id: 1,
        position: "Research Assistant",
        company: "University of Technology, Sydney",
        period: "April 2025 - February 2026",
        desc: `<strong>Project: Scoliosis Assessment Application</strong>
        • Implemented ETL pipeline for processing X-ray images, resulting in over 20,000 X-ray images with landmark annotations.
        • Fine-tuned Mask R-CNN models for vertebrae segmentation and proposed APEX/Cobb angle measurement method, with an absolute error of 3.02°±2.85°.
        • Architected a CI/CD pipeline via GitHub Actions, Docker to automate deployment on AWS EC2, integrating AWS S3 for secure versioning and efficient retrieval of deep learning model weights.`,
        techStack: ['Python', 'PyTorch', 'Mask R-CNN', 'AWS EC2', 'AWS S3', 'Docker', 'GitHub Actions'],
        borderColor: "border-cyan-500/30",
        dotColor: "bg-cyan-500",
        borderClass: "border-cyan-500/20",
        dateColor: "text-cyan-400 text-sm font-semibold",
        companyColor: "text-blue-400",
    },

    {
        id: 2,
        position: "Research Assistant",
        company: "The University of Melbourne",
        period: "October 2025 - December 2025",
        desc: `• Implemented an automated workflow in n8n that runs the ETL pipeline to extract and transform data from GeoScape APIs and Google Maps APIs to generate comprehensive property reports.`,
        techStack: ['n8n', 'Python', 'GeoScape API', 'Google Maps API', 'ETL'],
        borderColor: "border-cyan-500/30",
        dotColor: "bg-cyan-500",
        borderClass: "border-cyan-500/20",
        dateColor: "text-cyan-400 text-sm font-semibold",
        companyColor: "text-blue-400",
    },

    {
        id: 3,
        position: "Machine Learning Engineer",
        company: "Ycomm Viet Nam",
        period: "April 2023 - January 2024",
        desc: `<strong> Project: Webtoon editor</strong> – Agile development
        • Deployed text inpainting API using LaMa model and text detection APIs using EasyOCR and Google Vision API, which is the main feature in the webtoon editor.
        • Built a webtoon dataset pipeline for English, Korean, Japanese, and Chinese using Label Studio.

        <strong>Project: Subtitle extractor</strong> – Agile development
        • Deployed Stable_Whisper and Google Speech-to-text API to extract subtitles in cartoons.
        • Integrated DeepL API for translation API.`,
        techStack: ['Python', 'LaMa', 'EasyOCR', 'Google Vision API', 'Label Studio', 'Stable Whisper', 'DeepL API'],
        borderColor: "border-cyan-500/30",
        dotColor: "bg-cyan-500",
        borderClass: "border-cyan-500/20",
        dateColor: "text-cyan-400 text-sm font-semibold",
        companyColor: "text-blue-400",
    },

    {
        id: 4,
        position: "Artificial Intelligence Specialist",
        company: "VinBigData",
        period: "October 2021 - July 2022",
        desc: `<strong>Project: Text-to-Speech with subword embedding</strong>
        • Researched phoneme + subword context modelling based on Tacotron2. 
        • Developed a custom Vietnamese tokenizer using Hugging Face tokenization tools.
        • Achieved Mel Cepstral Distortion (MCD) of 11.37, outperforming phoneme-only (12.1) and subword-only (11.77) models.

        <strong>Project: Vietnamese Spelling Error Correction System</strong>
        • Implemented augmentation techniques to create 5 million training samples.
        • Experimented with BI-LSTM (ROUGE-1 0.86), and Transformer (ROUGE-1 0.93).

        <strong>Project: Visual Question Answering</strong>
        • Implemented pipeline including Faster R-CNN for image feature extraction, GloVe embeddings for question representation, and BERT for context modeling.
        • Achieved overall accuracy of 70.98%.`,
        techStack: ['Python', 'PyTorch', 'Tacotron2', 'Hugging Face', 'BERT', 'Faster R-CNN', 'GloVe', 'BI-LSTM', 'Transformer'],
        borderColor: "border-cyan-500/30",
        dotColor: "bg-cyan-500",
        borderClass: "border-cyan-500/20",
        dateColor: "text-cyan-400 text-sm font-semibold",
        companyColor: "text-blue-400",
    },

    {
        id: 5,
        position: "Data Scientist",
        company: "FPT Telecom",
        period: "June 2021 - October 2021",
        desc: `<strong>Unknown Recognition by Camera Project</strong>
        • Integrated EfficientNet into the backbone of RetinaFace, reducing model weight to 50%.
        • Optimized user registration using FAISS, users only provide 3 images to create account.`,
        techStack: ['Python', 'PyTorch', 'EfficientNet', 'RetinaFace', 'FAISS'],
        borderColor: "border-cyan-500/30",
        dotColor: "bg-cyan-500",
        borderClass: "border-cyan-500/20",
        dateColor: "text-cyan-400 text-sm font-semibold",
        companyColor: "text-blue-400",
    },

    {
        id: 6,
        position: "Artificial Intelligence Intern",
        company: "Cloud Nine Solutions",
        period: "July 2020 - October 2020",
        desc: `<strong>Facial Recognition Check-in Project</strong>
        • Developed a neural network model for real-time facial recognition.
        • Deployed the solution on Jetson Nano for on-device, low-latency check-in.`,
        techStack: ['Python', 'PyTorch', 'OpenCV', 'Jetson Nano'],
        borderColor: "border-cyan-500/30",
        dotColor: "bg-cyan-500",
        borderClass: "border-cyan-500/20",
        dateColor: "text-cyan-400 text-sm font-semibold",
        companyColor: "text-blue-400",
    },
]

const techStack = [
    'Python', 'SQL', 'Pytorch', 'Tensorflow', 'PGVector', 'SQLite3', 'AWS', 'GCP', 'Docker', 'Git', 'REST APIs'
]
</script>
