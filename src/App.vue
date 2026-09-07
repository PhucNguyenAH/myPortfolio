<template>
    <div v-if="loading">
        <LoadingSpinner />
    </div>
    <div v-else class="min-h-screen bg-linear-to-br 
    from-gray-900 via-blue-900 to-gray-900">
        <Navbar />
        <Avatar />
        <About />
        <Experience />
        <Education />
        <Projects />
        <Publications />
        <Contact />
        <BackToTop />
        <Chatbot />
    </div>
</template>
<script>

import AOS from 'aos';
import 'aos/dist/aos.css';
import {ref, nextTick, onMounted, defineComponent} from 'vue';
import Avatar from './components/Avatar.vue';
import Navbar from './components/Navbar.vue';
import About from './components/About.vue';
import Experience from './components/Experience.vue';
import Education from './components/Education.vue';
import Projects from './components/Projects.vue';
import Contact from './components/Contact.vue';
import BackToTop from './components/BackToTop.vue';
import LoadingSpinner from './components/LoadingSpinner.vue';
import Publications from './components/Publications.vue';
import Chatbot from './components/Chatbot.vue';

export default defineComponent({
    name: 'App',
    components : {
        Navbar,
        Avatar,
        About,
        Experience,
        Education,
        Projects,
        Publications,
        Contact,
        Chatbot,
        BackToTop,
        LoadingSpinner,
    },
    setup() {
        const loading = ref(true);

        onMounted(async () => {
            await nextTick();

            AOS.init({
                duration: 800,
                once: false,
                offset: 100,
                easing: 'ease-in-out',
            });
            setTimeout(() => {
                loading.value = false;
        }, 800);
        });
        return {loading};
    }
})
</script>