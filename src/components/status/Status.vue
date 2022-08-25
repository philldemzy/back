<template>
    <div class="flex flex-col items-center p-5 mt-48">
        <div v-show="dataStore.notDone" class="flex flex-row self-center bg-brown3 p-3 px-5 rounded-md lg:rounded-lg">
            <svg class="animate-spin mt-1 -ml-1 mr-3 h-5 w-5 text-orange-900" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
            </svg>
            <span class="text-lg text-stone-900">Submitting...</span>
        </div>
        <div v-show="dataStore.isSuccessfull" >
            <Success/>
        </div>
        
        <div v-show="dataStore.isUnsuccessful">
            <Failure/>
        </div>
    </div>
</template>

<script>
import Success from './status/Success.vue';
import Failure from './status/Failure.vue';
import { useGenStore } from '../../store/store.js'

export default {
    name: 'Status',

    setup() {
        const dataStore = useGenStore()

        return {
            dataStore,
        }
    },

    components: {
        Success,
        Failure
    },

    mounted() {
        //this.submitTestProgress(this.dataStore.submitTaskId)
    },

    methods: {
        submitTestProgress() {
            let myInterval = setInterval((task_id) => {
                console.log(task_id)
                const res = await fetch(`http://localhost:8000/mark/task_id`)
                const data = await res.json()
                if (data.state == "SUCCESS") {
                    dataStore.isSuccess();
                    this.clearInterval(myInterval)
                }
                else if (data.state == "FAILURE") {
                    dataStore.isFailed();
                    this.clearInterval(myInterval)
                }
            }, 500)
        },

        clearIntervals(func) {
            clearInterval(func)
        }
    },

}
</script>
