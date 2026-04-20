<template>
    <section class="relative w-full overflow-hidden py-20
    flex items-center">
        <div class="w-full px-5 sm:px-8 md:px-12 lg:px-8 max-w-5xl
        lg:max-w-7xl mx-auto relative z-10">
            <div class="flex flex-col md:mt-0 mt-20 justify-center items-center">
                <div
                class="text-white text-center"
                data-aos="fade-right"
                >
                <h1 class="text-white font-bold text-4xl"
                md:text-5xl lg:text-6xl leading-tight>
                    Hi, I'm 
                    <span
                    class="text-transparent bg-clip-text bg-linear-to-r
                    from-blue-400 to-cyan-400"
                    >Anh Hoang Phuc Nguyen </span> 👋
                </h1>
                <p
                class="text-blue-200 font-medium text-lg md:text-xl
                mt-4"
                data-aos="fade-right"
                data-aos-delay="100"
                >
                    AI/ML Engineer & Data Scientist
                </p>
                </div>
                <p class="text-gray-300 pt-6 text-center
                mx-auto max-w-xl text-lg leading-relaced"
                data-aos="fade-right"
                data-aos-delay="200">
                    I am an AI/ML Engineer and Data Scientist with a Master of Artificial Intelligence and published research experience. I specialise in bridging advanced academic research with hands-on technical execution, particularly in the fields of computer vision and natural language processing.
                </p>
                <div
                class="flex items-center gap-4 pt-8 flex-col
                sm:flex-row sm:w-max mx-auto"
                data-aos="fade-up"
                data-aos-delay="300">
                <button
                @click="scrollToContact"
                class="px-8 md:px-10 py-4 rounded-xl relative group
                w-full sm:w-max flex justify-center overflow-hidden
                bg-linear-to-r from-blue-600 to-cyan-600
                hover:from-blue-500 hover:to-cyan-500 transition-all
                duration-300">
                    <span class="relative flex items-center
                    justify-center text-white font-semibold
                    text-lg">
                        Contact me
                        <ArrowRightIcon class="ml-2 w-5 h-5
                    group-hover:translate-x-1 transition-transform"/>
                    </span>
                </button>
                <a
                href="/Anh Hoang Phuc Nguyen - resume.pdf"
                download="Anh Hoang Phuc Nguyen - resume.pdf"
                class="border-2 border-blue-400 px-8 md:px-10
                py-4 rounded-1 relative group w-full sm:w-max
                flex justify-center hover:bg-blue-400/10
                transition-all duration-300">
                <div class="flex items-center justify-center relative">
                    <ArrowDownTrayIcon
                    class="w-5 h-5 text-blue-400
                    group-hover:translate-y-1 transition-transform"/>
                    <span class="pl-3 text-blue-400 font-semibold
                    text-lg">
                        Download Resume
                    </span>
                </div>
                </a>
                </div>
            </div>
        </div>
    </section>
</template>

<script setup>
import { ArrowDownTrayIcon, ArrowRightIcon } from '@heroicons/vue/16/solid';

function scrollToContact() {
    document.getElementById('contact')?.scrollIntoView({ behavior: 'smooth' });
}
</script>

