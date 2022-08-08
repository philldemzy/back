<template>
  <Nav v-for="question in questions" :key="question.id" @question-changed="navToQuest" :num="questions.indexOf(question) + 1" :question="question" :currentPage="currentPage"/>
</template>

<script>
  import Nav from './Nav.vue'

  export default {
    name: 'Navs',

    props: {
      questions: Array,
      currentPage: Number,
    },

    components: {
      Nav,
    },

    methods: {
      navToQuest(id, num) {
        const id_ = id;
        const num_ = num;
        this.$emit('question-changed', id_, num_);
      },
    },

    emits: ["question-changed",],
  }
</script>
