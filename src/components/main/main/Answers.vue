<template>
    <div v-for="option in dataStore.currQuestion.options" :key="option.main" >
        <Answer @answer-picked="changeAnswer" :option="option" />
    </div>
</template>

<script>
import Answer from './Answer.vue'
import { useDataStore } from '../../../store/data.js'
import { useRoute } from 'vue-router';

export default {
    name: 'Answers',

    setup() {
        const dataStore = useDataStore();
        const link = useRoute().params.link;

        return {
            dataStore,
            link
        }
    },

    components: {
        Answer,
    },

    methods: {
        changeAnswer (ans) {
            const answer = {
                id: this.dataStore.currQuestion.id,
                answer: ans,
            };
            // add answer to pinia store
            this.dataStore.addAnswer(answer);

            // change whole answers picked array in localstorage
            if (localStorage.getItem(`answers${this.link}`)) {
                localStorage.removeItem(`answers${this.link}`);
            }
            localStorage.setItem(`answers${this.link}`, JSON.stringify(this.dataStore.pickedAns));
        },
    },
}
</script>
