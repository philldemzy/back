<template>
    <div class="flex">
        <h2 class="mt-6 text-red-700 text-xl lg:text-2xl">O0ps an error occured</h2>
        <svg xmlns="http://www.w3.org/2000/svg" class="lg:h-20 lg:w-16 h-16 w-14 lg:stroke-4 stroke-2 text-red-900" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
            <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
        </svg>
    </div>

    <button @click="reSubmit" class="flex text-zinc-900 text-md lg:text-lg p-2 space-x-3">
        <h4>click here to re-submit</h4> 
        <span class="inline-block">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="text-red-500 w-6 h-6">
                <path stroke-linecap="round" stroke-linejoin="round" d="M16.023 9.348h4.992v-.001M2.985 19.644v-4.992m0 0h4.992m-4.993 0l3.181 3.183a8.25 8.25 0 0013.803-3.7M4.031 9.865a8.25 8.25 0 0113.803-3.7l3.181 3.182m0-4.991v4.99" />
            </svg>
        </span>
    </button>
</template>

<script>
import { useGenStore } from '@/store/store'
import { useDataStore } from '@/store/data.js'

export default {
    name: 'Failure',

    setup() {
        const genStore = useGenStore()
        const dataStore = useDataStore()

        return {
            genStore,
            dataStore,
        }
    },

    methods: {
        async reSubmit(event) {
            //re submit, i.e make post request again
            event.preventDefault();

            const bodyData = {
                student: this.dataStore.studentId,
                answers: this.dataStore.pickedAns
            }

            // post method
            const res = await fetch(`${process.env.VUE_APP_ROOT_API}/mark`, {
                method: 'POST',
                headers: { "X-CSRFToken": `${this.genStore.token}` },
                body: JSON.stringify(bodyData)
            })
            const data = await res.json()
            this.genStore.setSubmitTaskId(data.task);

            this.$router.replace({path: '/submited'});
        },
    }
}
</script>
