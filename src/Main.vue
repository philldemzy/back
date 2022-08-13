<template>
    <questNum />
    <Question :question=dataStore.currQuestion />
    <div class="lg:h-4"></div>
    <div class="relative flex justify-center">
        <section class="grid grid-cols-1 p-3 gap-6 place-items-stretch w-full">
            <Answers @answer-picked="testOneTwo" :pickedAns="pickedAns" />
        </section>
    </div>
    <div class="grid grid-cols-2 mx-4">
        <PrevNext/>
    </div>
    <div class="h-0"></div>
</template>

<script>
import questNum from './components/questNum.vue'
import Question from './components/Question.vue'
import Answers from './components/Answers.vue'
import PrevNext from './components/PrevNext.vue'
import { useDataStore } from './store/data.js'

export default {
    name: 'Main',

    props: {
        questions: Array,
        currQuestion: Object,
    },

    components: {
        questNum,
        Question,
        Answers,
        PrevNext,
    },

    data() {
        return {
            pickedAns: '-$#!',
        }
    },

    setup() {
        const dataStore = useDataStore()

        return {
            dataStore,
        }
    },

    methods: {
        testOneTwo (ans, id) {
            this.pickedAns = ans;
            console.log(id);
            this.$emit('answer-picked', ans, id);
        },
    },

    emits: ["go-to-prev", "go-to-next", "answer-picked"],
}
</script>
