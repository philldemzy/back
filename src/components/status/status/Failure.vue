<template>
    <svg xmlns="http://www.w3.org/2000/svg" class="h-20 w-16 stroke-4 text-red-900" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
        <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
    </svg>
    <h2 class="text-align-center text-red-800 text-2xl lg:text-4xl">O0ps !!</h2>
    <h5 @click="reSubmit" class="text-align-center text-zinc-900 text-md lg:text-xl">click here to re-submit</h5>
</template>

<script>
export default {
    name: 'Failure',

    methods: {
        reSubmit() {
            //re submit, i.e make post request again
        },
    }
}
</script>
