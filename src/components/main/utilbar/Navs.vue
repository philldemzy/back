<template>
  <Nav v-for="question in dataStore.questions" :key="question.id" :num="dataStore.questions.indexOf(question) + 1" />
</template>

<script>
  import { useDataStore } from '../../../store/data.js'
  import Nav from './Nav.vue'

  export default {
    name: 'Navs',

    setup() {
      const dataStore = useDataStore()

      return {
        dataStore,
      }
    },

    components: {
      Nav,
    },
  }
</script>
