<template>
    <svg xmlns="http://www.w3.org/2000/svg" class="lg:h-20 lg:w-16 h-16 w-14 lg:stroke-4 stroke-2 text-green-900" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
        <path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7" />
    </svg>
    <h2 class="text-align-center text-green-700 text-2xl lg:text-4xl">Success !!</h2>
    <h5 class="text-align-center text-zinc-900 text-md lg:text-xl">Your test has been submitted and graded successfully</h5>
    <router-link to="/" class="text-md lg:text-xl hover:shadow-lg">Go back to home</router-link>
</template>

<script>
export default {
    name: 'Success',
}
</script>
