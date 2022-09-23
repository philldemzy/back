<template>
    <div class="flex">
        <h2 class="mt-5 text-green-700 text-xl lg:text-2xl">Success !!</h2>
        <svg xmlns="http://www.w3.org/2000/svg" class="lg:h-20 lg:w-16 h-16 w-14 lg:stroke-4 stroke-2 text-green-900" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
            <path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7" />
        </svg>
    </div>
    <h5 class="text-align-center text-zinc-900 text-md lg:text-lg">Your test has been submitted and graded successfully</h5>
    <router-link to="/" class="grid mt-3 text-base lg:text-lg hover:shadow-lg">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="place-self-center text-green-500 w-6 h-6">
            <path stroke-linecap="round" stroke-linejoin="round" d="M6 12L3.269 3.126A59.768 59.768 0 0121.485 12 59.77 59.77 0 013.27 20.876L5.999 12zm0 0h7.5" />
        </svg>
    </router-link>
</template>

<script>
export default {
    name: 'Success',
}
</script>
