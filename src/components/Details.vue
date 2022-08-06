<template>
  <div class="p-2 lg:p-0 text-base lg:text-xl md:ml-8 lg:ml-0 font-medium lg:font-semibold uppercase">
    <h4>{{ details.title }}</h4>
    <h4>{{ details.student_id }}</h4>
    <h4>{{ details.student_name }}</h4>
    <h4>{{ details.duration }}</h4>
  </div>
</template>

<script>
export default {
  name: 'Details',
  
  props: {
    details: Object
  }
}
</script>

