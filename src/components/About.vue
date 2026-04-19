<template>
    <section class="relative py-20 overflow-hidden min-h-screen
    flex items-center" id="about">
        <div class="w-full px-5 sm:px-8 md:px-12 lg:px-8 max-w-5xl
        lg:max-w-7xl mx-auto relative z-10">
            <div class="grid lg:grid-cols-2 gap-10 xl:gap-14
            items-center">
                <div class="lg:h-full flex justify-center
                lg:justify-start order-2 lg:order-1">
                    <div class="relative w-full max-w-md">
                        <div 
                        data-aos="zoom-in"
                        class="relative bg-linear-to-br
                        from-gray-800/60 to-blue-900/40 rounded-3xl p-6
                        backdrop-blur-sm border border-blue-500/10 shadow-2xl">
                            <div class="grid grid-cols-2 gap-4">
                                <div
                                v-for="(image, index) in aboutImage"
                                :key="image.id"
                                class="relative group"
                                :data-aos="image.animation"
                                :data-aos-delay="image.delay"
                                >
                                    <div class="rounded-2xl p-2 border shadow-lg"
                                    :class="image.gradient">
                                        <img 
                                        :src="image.src" 
                                        :alt="image.alt"
                                        class="w-full h-48 object-cover rounded-xl group-hover:scale-105 transition-transform duration-300">
                                    </div>
                                    <div class="absolute -top-2 -right-2 text-white text-xs px-2 py-1 rounded-full font-semibold"
                                    :class="image.badgeColor">
                                        {{ image.badge }}
                                    </div>
                                </div>
                            </div>
                                <div class="absolute -bottom-4 left-1/2 
                                transform -translate-x-1/2 z-20 bg-linear-to-r 
                                from-blue-500 to-cyan-500 rounded-2xl px-6 py-3
                                border border-blue-400/40 shadow-xl"
                                data-aos="fade-up"
                                data-aos-delay="400">
                                    <div
                                    class="text-center text-white text-xl font-bold">3+ Years Experience</div>
                                </div>
                            </div>
                        </div>
                    </div>
                
                <!-- Text -->
                <div class="flex flex-col justify-center
                order-1 lg:order-2">
                <div class="text-center lg:text-left"
                data-aos="fade-left">
                    <h2 class="text-white font-bold text-4xl md:text-5xl lg:text-6xl leading-tight">
                        About
                        <span
                        class="text-transparent bg-clip-text
                        bg-linear-to-r from-blue-400 to-cyan-400">
                        Me</span>
                    </h2>
                    <p class="text-blue-200 font-medium text-lg
                    md:text-xl mt-4" data-aos="fade-left"
                    data-aos-delay="100">
                        AI/ML Engineer & Data Scientist
                    </p>
                </div>
                <p class="text-gray-300 pt-4 text-center
                lg:text-left text-lg leading-relaxed"
                data-aos="fade-left"
                data-aos-delay="200">
                    I am an AI/ML Engineer and Data Scientist with a Master of Artificial Intelligence and published research experience. I specialise in bridging advanced academic research with hands-on technical execution, particularly in the fields of computer vision and natural language processing.
                </p>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-6 pt-8"
                data-aos="fade-up" data-aos-delay="300">
                    <div
                    v-for="skill in skills"
                    :key="skill.id"
                    class="flex flex-col">
                        <div class="flex items-center gap-3 mb-3">
                            <component 
                            :is="skill.icon"
                            class="w-6 h-6"
                            :class="skill.iconColor"
                            ></component>
                            <h3 class="text-lg font-bold text-white">
                                {{ skill.title }}
                            </h3>
                            
                        </div>
                        <p class="text-blue-100 text-sm">
                            {{ skill.desc }}
                        </p>
                    </div>
                </div>
                <div class="flex gap-4 pt-8 flex-col sm:flex-row"
                data-aos="fade-up"
                data-aos-delay="400">
                    <button
                    v-for="button in ctaButtons"
                    :key="button.id"
                    class="px-8 py-3 rounded-xl font-semibold
                    transition-allduration-300 flex items-center
                    justify-center"
                    :class="button.classes"
                    @click="button.onClick && button.onClick()">
                    <component
                    :is="button.icon"
                    class="w-4 h-4"
                    :class="button.iconclass"></component>
                        {{ button.text }}
                    </button>
                </div>
            </div>
        </div>
        </div>
    </section>
</template>

<script setup>

import { ArrowRightIcon, 
        ChatBubbleLeftRightIcon,
        CodeBracketSquareIcon,
        CircleStackIcon,
        CubeIcon,
        CloudIcon,
        CubeTransparentIcon} from '@heroicons/vue/16/solid'
import about1 from '/About1.jpg'
import about2 from '/About2.jpg'
import about3 from '/About3.png'
import about4 from '/About4.png'

const aboutImage = [
    {
        id: 1,
        src: about1,
        alt: "Anh - AI/ML Engineer",
        gradient: 'bg-linear-to-r from-blue-600 to-cyan-600 border-blue-400/40',
        badge: 'AI/ML Engineer',
        badgeColor: 'bg-blue-500',
        animation: 'fade-right',
        delay: 200
    },

    {
        id: 2,
        src: about2,
        alt: "Anh - Data Scientist",
        gradient: 'bg-linear-to-r from-blue-500 to-cyan-500 border-blue-400/40',
        badge: 'Data Scientist',
        badgeColor: 'bg-cyan-500',
        animation: 'fade-left',
        delay: 300
    },

    {
        id: 3,
        src: about3,
        alt: "Anh - Research Assistant",
        gradient: 'bg-linear-to-r from-blue-500 to-cyan-500 border-blue-400/40',
        badge: 'Research Assistant',
        badgeColor: 'bg-cyan-500',
        animation: 'fade-right',
        delay: 400
    },

    {
        id: 4,
        src: about4,
        alt: "Anh - Data Analyst",
        gradient: 'bg-linear-to-r from-blue-600 to-cyan-600 border-blue-400/40',
        badge: 'Data Analyst',
        badgeColor: 'bg-blue-500',
        animation: 'fade-left',
        delay: 500
    },
]

const skills = [
    {
        id:1,
        icon:CodeBracketSquareIcon,
        iconColor: "text-blue-400",
        title: "Programming Languages",
        desc: "Python, SQL"
    },
    {
        id:2,
        icon:CubeTransparentIcon,
        iconColor: "text-blue-400",
        title: "AI & Data Science",
        desc: "PyTorch, Tensorflow, LLMs, LoRA, RAG, LangChain, n8n"
    },
    {
        id:3,
        icon:CloudIcon,
        iconColor: "text-blue-400",
        title: "Cloud & Deployment",
        desc: "AWS, GCP, Docker, CI/CD, Git"
    },
    {
        id:4,
        icon:CircleStackIcon,
        iconColor: "text-blue-400",
        title: "Database",
        desc: "SQLit3, PGVector, MySQL"
    },
    {
        id:5,
        icon:CubeIcon,
        iconColor: "text-blue-400",
        title: "Others",
        desc: "Linux, Jira, Tableau, PyQT5, Apache Kafka, MQTT, RabbitMQ, Flask"
    }
]

const ctaButtons = [
    {
        id:1,
        text: 'View Portfolio',
        icon: ArrowRightIcon,
        iconclass: 'ml-2 group-hover:translate-x-1 transition-transform',
        classes: 'bg-linear-to-r from-blue-600 to-cyan-600 text-white hover:from-blue-500 hover:to-cyan-500',
        onClick: () => window.open('https://anhhoangphucnguyen.com', '_blank')
    },
    {
        id:2,
        text: 'Contact Me',
        icon: ChatBubbleLeftRightIcon,
        iconclass: 'mr-2',
        classes: 'border border-blue-400 text-blue-400 hover:bg-blue-400/10',
        onClick: () => document.getElementById('contact')?.scrollIntoView({ behavior: 'smooth' })
    },
]
</script>
