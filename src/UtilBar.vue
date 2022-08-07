<template>
  <Details :details="details" />
  <nav class="lg:ml-1 mb-5 mt-4 grid grid-cols-5 gap-2 text-base lg:text-xl lg:mt-5 xl:mt-10">
    <Navs @question-changed="navToQuest" :questions="questions" :currentPage="currentPage" />
  </nav>
  <Submit/>
</template>

<script>
import Details from './components/Details.vue'
import Navs from './components/Navs.vue'
import Submit from './components/Submit.vue'
import './assets/tailwind.css'

export default {
  name: 'UtilBar',

  components: {
    Details,
    Navs,
    Submit,
  },

  props: {
    questions: Array,
    details: Object,
    currentPage: Number,
  },

  methods: {
    navToQuest (id, num) {
      this.currentPage = num;
      this.$emit('question-changed', id, num);
    },
  },

  emits: ["question-changed",],
}
</script>

