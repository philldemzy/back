<template>
  <div class="p-2 lg:p-0 text-base lg:text-xl md:ml-8 lg:ml-0 font-medium lg:font-semibold uppercase">
    <h4>{{ dataStore.details.title }}</h4>
    <h4>{{ dataStore.details.student_id }}</h4>
    <h4>{{ dataStore.details.student_name }}</h4>
    <h4>{{ dataStore.details.duration }}</h4>
  </div>
</template>

<script>
import { useDataStore } from '../store/data.js'

export default {
  name: 'Details',
  
  setup() {
    const dataStore = useDataStore()

    return {
      dataStore,
    }
  },
}
</script>

