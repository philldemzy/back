<template>
  <div class="font-['Trebuchet MS']">
    <h2 class="p-2 lg:p-3 font-bold text-xl sm:text-2xl tracking-tight">
      <b class="text-brown4">C</b>
      <b class="text-red-400">B</b>
      Easy
    </h2>
  </div>
  <Menu @change-show-menu="$emit('change-show-menu')" :showMenu="showMenu"/>
</template>

<script>
import Menu from './components/Menu.vue'
import './assets/tailwind.css'

export default {
  name: 'Header',

  emits: ["change-show-menu"],

  props: {
    showMenu: Boolean,
  },
  
  components: {
    Menu,
  },
}
</script>
