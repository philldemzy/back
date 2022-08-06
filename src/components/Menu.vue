<template>
  <div class="lg:hidden relative bg-brown1">
    <span id="menu1" @click="onClick($event)" v-show="showMenu">
      <svg xmlns="http://www.w3.org/2000/svg" class="absolute top-1 right-2 h-10 w-10 stroke-2" viewBox="0 0 20 20" fill="currentColor">
        <path fill-rule="evenodd" d="M3 4a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zm0 4a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zm0 4a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zm0 4a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1z" clip-rule="evenodd" />
      </svg>
    </span>
    <span id="menu2" @click="onClick($event)" v-show="!showMenu">
      <svg xmlns="http://www.w3.org/2000/svg" class="absolute top-1 right-2 h-10 w-10 stroke-2" viewBox="0 0 20 20" fill="currentColor">
        <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd" />
      </svg>
    </span>
  </div>
</template>

<script>
export default {
  name: 'Menu',

  data() {
    return {
      showMenu: true,
    }
  },

  methods: {
    onClick(event) {
      const current_ = event.target.parentElement;

      const nav_ = document.getElementById("utilbar");
      const ques_ = document.getElementById("main");
      
      if (this.showMenu) {
        this.showMenu = !this.showMenu

        //hide ques show nav
        let navClass = nav_.className;
        let quesClass = ques_.className;
        ques_.className = `hidden lg:${quesClass}`;
        nav_.className = navClass.replace('hidden lg:', '');
      }
      else {
        this.showMenu = !this.showMenu

        //hide nav show ques
        let navClass = nav_.className;
        let quesClass = ques_.className;
        ques_.className = quesClass.replace('hidden lg:', '');
        nav_.className = `hidden lg:${navClass}`;
      }
    },
  }
}
</script>
