<template>
    <div class="fixed bottom-20 right-4 z-50 flex flex-col items-end">
        <!-- Chat panel -->
        <transition name="chat-slide">
            <div
                v-if="isOpen"
                class="mb-3 w-80 rounded-2xl shadow-2xl overflow-hidden flex flex-col"
                style="height: 420px; background: rgba(17,24,39,0.97); border: 1px solid rgba(59,130,246,0.3);"
            >
                <!-- Header -->
                <div class="flex items-center justify-between px-4 py-3 bg-gradient-to-r from-blue-600 to-cyan-600">
                    <div class="flex items-center gap-2">
                        <div class="w-2 h-2 rounded-full bg-green-400 animate-pulse"></div>
                        <span class="text-white font-semibold text-sm">Chat with Phuc's AI</span>
                    </div>
                    <button @click="isOpen = false" class="text-white/70 hover:text-white text-lg leading-none">✕</button>
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
                                'max-w-[75%] px-3 py-2 rounded-2xl text-sm leading-relaxed',
                                msg.role === 'user'
                                    ? 'bg-gradient-to-r from-blue-600 to-cyan-600 text-white rounded-br-sm'
                                    : 'bg-gray-700 text-gray-100 rounded-bl-sm'
                            ]"
                        >
                            {{ msg.text }}
                        </div>
                    </div>
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
                    <form @submit.prevent="sendMessage" class="flex gap-2">
                        <input
                            v-model="input"
                            type="text"
                            placeholder="Ask me anything..."
                            class="flex-1 bg-gray-800 text-gray-100 text-sm rounded-full px-4 py-2 outline-none border border-gray-600 focus:border-blue-500 placeholder-gray-500 transition-colors"
                        />
                        <button
                            type="submit"
                            :disabled="!input.trim() || isThinking"
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
            class="w-14 h-14 rounded-full bg-gradient-to-r from-blue-600 to-cyan-600 text-white shadow-lg flex items-center justify-center text-2xl transition-transform hover:scale-110 active:scale-95"
        >
            <span v-if="!isOpen">💬</span>
            <span v-else class="text-lg">✕</span>
        </button>
    </div>
</template>

<script setup>
import { ref, nextTick } from 'vue';

const isOpen = ref(false);
const input = ref('');
const isThinking = ref(false);
const messagesEl = ref(null);

const FAQ = [
    { keys: ['hello', 'hi', 'hey'], answer: "Hi there! I'm Phuc's portfolio assistant. Ask me about his skills, experience, or projects!" },
    { keys: ['skill', 'tech', 'stack', 'language', 'framework'], answer: "Phuc works with Vue.js, React, TypeScript, Node.js, Python, and TailwindCSS — among other tools." },
    { keys: ['experience', 'work', 'job', 'career'], answer: "Phuc has professional experience in full-stack development. Check the Experience section for details!" },
    { keys: ['project', 'portfolio', 'build'], answer: "Phuc has built several projects including this portfolio! Scroll to the Projects section to see them." },
    { keys: ['education', 'study', 'degree', 'university'], answer: "Check the Education section for Phuc's academic background." },
    { keys: ['contact', 'email', 'reach', 'hire'], answer: "You can reach Phuc via the Contact section at the bottom of this page." },
    { keys: ['publication', 'paper', 'research'], answer: "Phuc has published research work — scroll to the Publications section to find out more." },
];

const messages = ref([
    { role: 'bot', text: "Hi! I'm Phuc's AI assistant. Feel free to ask about his skills, experience, or projects 👋" }
]);

function getBotReply(text) {
    const lower = text.toLowerCase();
    for (const entry of FAQ) {
        if (entry.keys.some(k => lower.includes(k))) return entry.answer;
    }
    return "I'm not sure about that, but you can explore the sections above or reach out via the Contact form!";
}

async function scrollToBottom() {
    await nextTick();
    if (messagesEl.value) messagesEl.value.scrollTop = messagesEl.value.scrollHeight;
}

async function sendMessage() {
    const text = input.value.trim();
    if (!text || isThinking.value) return;

    messages.value.push({ role: 'user', text });
    input.value = '';
    await scrollToBottom();

    isThinking.value = true;
    await scrollToBottom();

    setTimeout(async () => {
        isThinking.value = false;
        messages.value.push({ role: 'bot', text: getBotReply(text) });
        await scrollToBottom();
    }, 800);
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
</style>
