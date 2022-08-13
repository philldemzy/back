<template>
  <div @click="questChanged" :class="[num === dataStore.currQuestNum ? 'bg-red-700 text-white' : 'bg-red-400 hover:bg-red-700 hover:text-white shadow-md ', 'p-1 sm:p-3 xl:p-3 rounded-md text-center cursor-pointer']">{{ num }}</div>
</template>

<script>
import { useDataStore } from '../store/data.js'

export default {
  name: 'Nav',

  props: {
    num: Number,
  },

  setup() {
    const dataStore = useDataStore()

    return {
      dataStore,
    }
  },

  methods: {
    questChanged () {
      const nav_ = document.getElementById("utilbar");
      const ques_ = document.getElementById("main");

      //hide nav show ques only for small screens
      if (window.innerWidth < 1024) {
        let navClass = nav_.className;
        let quesClass = ques_.className;
        ques_.className = quesClass.replace('hidden lg:', '');
        nav_.className = `hidden lg:${navClass}`;
      }

      this.dataStore.changeQues(this.num - 1);
      this.dataStore.changeShowMenu();
    },
  },
}
</script>
