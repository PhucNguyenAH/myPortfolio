<template>
    <section class="relative py-20 overflow-hidden" id="publications">
        <div class="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center mb-16" data-aos="fade-up">
                <h2 class="text-4xl md:text-5xl font-bold text-white mb-4">
                    My <span class="text-transparent bg-clip-text
                    bg-linear-to-r from-blue-400 to-cyan-400">
                        Publications
                    </span>
                </h2>
                <p class="text-blue-200 text-lg max-w-2xl mx-auto">
                    A collection of my publications
                </p>
            </div>

            <!-- Publications Grid -->
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-2 gap-8">
                <div
                v-for="(publication, index) in publications"
                :key="publication.id"
                class="group relative bg-linear-to-br from-gray-800/50
                to-blue-900/30 rounded-3xl overflow-hidden border
                backdrop-blur-sm hover:border-blue-400/40
                transition-all duration-500 hover:transform
                hover:-translate-y-2"
                :class="publication.bordColor"
                data-aos="fade-up"
                :data-aos-delay="(index+1)*100">
                <!-- Publication Image -->
                    <div class="relative overflow-hidden">
                        <img 
                        :src="publication.image" 
                        :alt="publication.title"
                        class="w-full h-48 object-cover group-hover:scale-110
                        transition-transform duration-500">
                        <div class="absolute inset-0 bg-linear-to-t
                        from-gray-900 via-transparent to-transparent">
                        </div>
                        <div class="absolute top-4 right-4">
                            <span class="px-3 py-1 text-white text-xs
                            rounded-full font-semibold"
                            :class="publication.badgColor">
                                {{ publication.category }}
                            </span>
                        </div>
                    </div>
                    <!-- Publication Content -->
                    <div class="p-6">
                        <h3
                        class="text-xl font-bold text-white
                        group-hover:text-blue-400 transition-colors
                        duration-300">
                            {{ publication.title }}
                        </h3>
                        <p class="text-blue-100 text-sm leading-relaxed mb-4 whitespace-pre-line">
                            {{ publication.desc }}
                        </p>
                        <!-- Technologies -->
                        <div class="flex flex-wrap gap-2 mb-4">
                            <span
                            v-for="tech in publication.technolg"
                            :key="tech"
                            class="px-2 py-1 border rounded text-xs"
                            :class="tech.class">
                            {{ tech.name }}
                            </span>
                        </div>
                        <!-- Publication Links -->
                        <div class="flex gap-3">
                            <a 
                            v-for="link in publication.links"
                            :key="link.name"
                            :href="link.url"
                            :class="link.class"
                            class="flex items-center gap-2 transition-colors
                            duration-300 text-sm font-medium">
                            <component :is="link.icon" class="w-4 h-4"/>
                                {{ link.name }}
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>

<script setup>
import { ref } from 'vue';
import { 
    DocumentTextIcon, 
    CodeBracketIcon, 
    ArrowRightIcon,
    ChatBubbleLeftRightIcon
} from '@heroicons/vue/16/solid';

const publications = ref([
    {
        id: 1,
        title: "Evolving optimized transformer-hybrid systems for robust BCI signal processing using genetic algorithms",
        desc: `• Transformer-based BCIs boost robustness for weak learners but need expert tuning.
        • Rising complexity in BCI models demands automated architecture search.
        • Genetic algorithms evolve convolutional, transformer, and noise layers automatically.
        • Evolved models hit 89.3%±6.1% on Dataset I and 84.5%±9.6% on Dataset II.
        • Server-side embedding enables evolutionary personalization of EEG-BCI models.`,
        image: '/publication1.jpg',
        category: 'Journal Q1',
        bordColor: 'border-blue-500/20',
        badgColor: "bg-blue-500",
        technolg: [
            {
                name: 'Python', 
                class: 'bg-blue-500/20 border-blue-400/30 text-blue-200',
            },
            {
                name: 'PyTorch', 
                class: 'bg-cyan-500/20 border-cyan-400/30 text-cyan-200',
            },
            {
                name: 'High-Performance Computing', 
                class: 'bg-cyan-500/20 border-cyan-400/30 text-cyan-200',
            },
            {
                name: 'GitHub', 
                class: 'bg-blue-500/20 border-blue-400/30 text-blue-200',
            },
        ],
        links: [
            {name: 'DOI', url: "https://doi.org/10.1016/j.bspc.2025.107883", icon: DocumentTextIcon,
                class:'text-blue-400 hover:text-blue-300'
            },
        ]
    },
    {
        id: 2,
        title: "EEG-TCNTransformer: A Temporal Convolutional Transformer for Motor Imagery Brain–Computer Interfaces",
        desc: 'In brain–computer interface motor imagery (BCI-MI) systems, convolutional neural networks (CNNs) have traditionally dominated as the deep learning method of choice, demonstrating significant advancements in state-of-the-art studies. Recently, Transformer models with attention mechanisms have emerged as a sophisticated technique, enhancing the capture of long-term dependencies and intricate feature relationships in BCI-MI. This research investigates the performance of EEG-TCNet and EEG-Conformer models, which are trained and validated using various hyperparameters and bandpass filters during preprocessing to assess improvements in model accuracy. Additionally, this study introduces EEG-TCNTransformer, a novel model that integrates the convolutional architecture of EEG-TCNet with a series of self-attention blocks employing a multi-head structure. EEG-TCNTransformer achieves an accuracy of 83.41% without the application of bandpass filtering.',
        image: '/publication2.png',
        category: 'Journal Q2',
        bordColor: 'border-cyan-500/20',
        badgColor: "bg-cyan-500",
        technolg: [
            {
                name: 'Python', 
                class: 'bg-cyan-500/20 border-cyan-400/30 text-cyan-200',
            },
            {
                name: 'Pytorch', 
                class: 'bg-blue-500/20 border-blue-400/30 text-blue-200',
            },
            {
                name: 'High-Performance Computing', 
                class: 'bg-cyan-500/20 border-cyan-400/30 text-cyan-200',
            },
            {
                name: 'Git', 
                class: 'bg-blue-500/20 border-blue-400/30 text-blue-200',
            },
        ],
        links: [
            {name: 'DOI', url: "https://doi.org/10.3390/signals5030034", icon: DocumentTextIcon,
                class:'text-blue-400 hover:text-blue-300'
            },
            {name: 'Code', url: "https://github.com/PhucNguyenAH/EEG-TCNTransformer", icon: CodeBracketIcon,
                class:'text-cyan-400 hover:text-cyan-300'
            },
        ]
    },
    
])
</script>