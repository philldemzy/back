<template>
    <button @click="submit" class="uppercase p-2 text-base lg:text-xl border-2 border-slate-700 lg:mt-10 xl:mt-20 hover:bg-slate-700 hover:text-white lg:w-full">
        Submit
    </button>
</template>

<script>
export default {
    name: 'Submit',

    methods: {
        submit(event) {
            event.preventDefault();

            //making post request somewhere
            //

            this.$router.replace({path: '/submited'});
        },
    },
}
</script>
