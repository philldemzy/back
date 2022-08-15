<template>
    <div class="w-full border-b border-dark1">
        <span class="text-semibold text-base lg:text-lg p-3 font-semibold">Question {{ dataStore.currQuestNum }} of {{ dataStore.totalQuestNum }}</span>
    </div>
</template>

<script>
import { useDataStore } from '../../../store/data.js'

export default {
    name: 'questNum',

    setup() {
        const dataStore = useDataStore()

        return {
            dataStore,
        }
    },
}
</script>
