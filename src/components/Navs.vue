<template>
  <div v-for="question in questions" :key="question.id">
    <Nav :num="questions.indexOf(question) + 1" :question="question" />
  </div>
</template>

<script>
  import Nav from './Nav.vue'

  export default {
    name: 'Navs',

    props: {
      questions: Array,
    },

    components: {
      Nav,
    },
  }
</script>
