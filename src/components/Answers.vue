<template>
    <div v-for="option in question.options" :key="option.main" >
        <Answer @answer-picked="testOneTwo" :option="option" :pickedAns="pickedAns" />
    </div>
</template>

<script>
import Answer from './Answer.vue'

export default {
    name: 'Answers',

    props: {
        question: Object,
        pickedAns: String,
    },

    components: {
        Answer,
    },

    methods: {
        testOneTwo (ans) {
            const ans_ = ans;
            this.$emit('answer-picked', ans_, this.question.id)
        },
    },

    emits: ["answer-picked",],
}
</script>
