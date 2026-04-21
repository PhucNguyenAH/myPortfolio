<template>
    <section class="relative py-20 overflow-hidden" id="education">
        <div class="relative z-10 max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center mb-16" data-aos="fade-up">
                <h2 class="text-4xl md:text-5xl font-bold text-white mb-4 flex items-center justify-center gap-3">
                    <AcademicCapIcon class="w-8 h-8 text-cyan-400"/>
                    <span class="text-transparent bg-clip-text bg-linear-to-r from-blue-400 to-cyan-400">
                        Education
                    </span>
                </h2>
            </div>
                <div data-aos="fade-right">
                    <div class="space-y-8">
                        <div
                        v-for="edu in educations"
                        :key="edu.id"
                        class="relative pl-8 border-l-2 group"
                        :class="edu.borderColor">
                        <div
                        class="absolute -left-2 top-0 w-4 h-4 rounded-full
                        group-hover:scale-150 transition-transform duration-300"
                        :class="edu.dotColor">
                        </div>
                        <div class="bg-linear-to-br from-gray-800/50
                        to-blue-900/30 rounded-2xl p-6 border
                        backdrop-blur-sm group-hover:border-blue-400/40
                        transition-all duration-300"
                        :class="edu.borderClass">
                        <div class="flex flex-col sm:flex-row sm:items-center
                        sm:justify-between mb-3">
                            <h4 class="text-lg font-bold text-white">{{ edu.university }}</h4>
                            <span
                            :class="edu.dateColor"
                            class="mt-1 sm:mt-0"
                            >{{ edu.period }}</span>
                        </div>
                        <p
                        :class="edu.qualificationColor" 
                        class="font-medium mb-3">{{ edu.qualification }}</p>
                        <p
                        class="text-blue-100 text-sm leading-relaxed whitespace-pre-line"
                        v-html="edu.desc"></p>
                        </div>
                        </div>
                </div>
            </div>
        </div>
    </section>
</template>

<script setup>
import { AcademicCapIcon, Squares2X2Icon } from '@heroicons/vue/16/solid';


const educations = [
    {
        id: 1,
        university: "University of Technology, Sydney (UTS)",
        qualification: "Master of Artificial Intelligence",
        period: "February 2024 - December 2025",
        desc: `• Postgraduate Academic Excellence International Scholarship.
        • Participated in Waymo 3D Semantic Segmentation Challenge: trained and validated SpUNet and Point Transformer V3 on Waymo v2.0.1.
        • Implemented ClearML for the Job and Candidate recommendation project, nominated for presentation at AI Showcase in UTS FEIT TechFest 2025.`,
        borderColor: "border-cyan-500/30",
        dotColor: "bg-cyan-500",
        borderClass: "border-cyan-500/20",
        dateColor: "text-cyan-400 text-sm font-semibold",
        qualificationColor: "text-blue-400",
    },

    {
        id: 2,
        university: "Ho Chi Minh City University of Technology (HCMUT)",
        qualification: "Bachelor of Engineering in Computer Science",
        period: "August 2017 - October 2021",
        desc: `• Authored Facial Recognition Attendance System in the 8th Science and Technology Symposium for OISP Students.
        • Implemented Kalman filter for optimised face tracking and Apache Kafka to connect Jetson Nano and Google Cloud Platform.
        • Fine-tuned FaceNet on HCMUT student dataset, achieving F1 score of 99.395% (0.335% improvement over baseline).`,
        borderColor: "border-cyan-500/30",
        dotColor: "bg-cyan-500",
        borderClass: "border-cyan-500/20",
        dateColor: "text-cyan-400 text-sm font-semibold",
        qualificationColor: "text-blue-400",
    },
]

const techStack = [
    'Python', 'SQL', 'Pytorch', 'Tensorflow', 'PGVector', 'SQLite3', 'AWS', 'GCP', 'Docker', 'Git', 'REST APIs'
]
</script>
