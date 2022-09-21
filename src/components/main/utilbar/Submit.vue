<template>
    <button @click="submit" class="uppercase p-2 text-base lg:text-xl border-2 border-slate-700 lg:mt-10 xl:mt-20 hover:bg-slate-700 hover:text-white lg:w-full">
        Submit
    </button>
</template>

<script>
import { useGenStore } from '@/store/store'
import { useDataStore } from '@/store/data.js'

export default {
    name: 'Submit',

    setup() {
        const genStore = useGenStore()
        const dataStore = useDataStore()

        return {
            genStore,
            dataStore,
        }
    },

    methods: {
        submit(event) {
            event.preventDefault();

            const bodyData = {
                student: this.dataStore.studentId,
                answers: this.dataStore.pickedAns
            }

            // post method
            const res = fetch(`http://localhost:8000/mark`, {
                method: 'POST',
                headers: { "X-CSRFToken": this.token },
                body: JSON.stringify(bodyData)
            })
            const data = res.json()
            this.genStore.setSubmitTaskId(data);

            this.$router.replace({path: '/submited'});
        },
    },
}
</script>
