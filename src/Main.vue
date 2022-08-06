<template>
    <questNum :curr="questions.indexOf(questions[0]) + 1" :total="questions.length"/>
    <Question :question=questions[0] />
    <div class="lg:h-4"></div>
    <div class="relative flex justify-center">
        <section class="grid grid-cols-1 p-3 gap-6 place-items-stretch w-full">
            <Answers @answer-picked="testOneTwo" :pickedAns="pickedAns" :question=questions[0] />
        </section>
    </div>
    <div class="grid grid-cols-2 mx-4">
        <PrevNext :questions="questions" :question=questions[0] />
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
        testOneTwo (ans) {
            this.pickedAns = ans;
        }
    }
}
</script>
