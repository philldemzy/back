<template>
  <div @click="$emit('question-changed', question.id, num)">
    <div :class="[num === currentPage ? 'bg-red-700 text-white' : 'bg-red-400 hover:bg-red-700 hover:text-white shadow-md ', 'p-1 sm:p-3 xl:p-3 rounded-md text-center cursor-pointer']">{{ num }}</div>
  </div>
</template>

<script>
export default {
  name: 'Nav',

  props: {
    num: Number,
    question: Object,
    currentPage: Number,
  },

  data() {
    return {
      showId: false,
    }
  }
}
</script>
