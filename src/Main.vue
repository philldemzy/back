<template>
    <questNum :curr="questions.indexOf(currQuestion) + 1" :total="questions.length"/>
    <Question :question=currQuestion />
    <div class="lg:h-4"></div>
    <div class="relative flex justify-center">
        <section class="grid grid-cols-1 p-3 gap-6 place-items-stretch w-full">
            <Answers @answer-picked="testOneTwo" :pickedAns="pickedAns" :question=currQuestion />
        </section>
    </div>
    <div class="grid grid-cols-2 mx-4">
        <PrevNext @go-to-prev="$emit('go-to-prev')"  @go-to-next="$emit('go-to-next')" :questions="questions" :question=currQuestion />
    </div>
    <div class="h-0"></div>
</template>

<script>
import questNum from './components/questNum.vue'
import Question from './components/Question.vue'
import Answers from './components/Answers.vue'
import PrevNext from './components/PrevNext.vue'

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
