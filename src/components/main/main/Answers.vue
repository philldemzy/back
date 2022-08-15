<template>
    <div v-for="option in dataStore.currQuestion.options" :key="option.main" >
        <Answer @answer-picked="testOneTwo" :option="option" />
    </div>
</template>

<script>
import Answer from './Answer.vue'
import { useDataStore } from '../../../store/data.js'

export default {
    name: 'Answers',

    setup() {
        const dataStore = useDataStore()

        return {
            dataStore,
        }
    },

    components: {
        Answer,
    },

    methods: {
        testOneTwo (ans) {
            const answer = {
                id: this.dataStore.currQuestion.id,
                answer: ans
            };
            this.dataStore.addAnswer(answer);
        },
    },
}
</script>
