<template>
    <div class="text-base lg:text-2xl text-semibold p-3 mt-7">
        {{ dataStore.currQuestion.question }}
    </div>
</template>

<script>
import { useDataStore } from '../../../store/data.js'

export default {
    name: 'Question',

    setup() {
        const dataStore = useDataStore()

        return {
            dataStore,
        }
    },
}
</script>
