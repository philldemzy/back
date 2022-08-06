<template>
  <div @click="$emit('go-to-num', question.id)">
      <div class="p-1 sm:p-3 xl:p-3 bg-red-400 rounded-md shadow-md text-center hover:bg-red-700 hover:text-white cursor-pointer">{{ num }}</div>
      <span v-show="showId">{{ question.id }}</span>
  </div>
</template>

<script>
export default {
  name: 'Nav',

  props: {
    num: Number,
    question: Object,
  },

  data() {
    return {
      showId: false,
    }
  }
}
</script>
