<template>
    <button @click="dataStore.goToPrev" :class="[dataStore.isPrev ? 'hover:bg-brown4 hover:text-white hover:border-0' : '','uppercase p-2 border font-semibold border-dark1 w-24']">previous</button>
    <button @click="dataStore.goToNext" :class="[dataStore.isNext ? 'hover:bg-brown4 hover:text-white hover:border-0' : '','place-self-end uppercase p-2 border font-semibold border-dark1 w-24']">next</button>
</template>

<script>
import { useDataStore } from '../../../store/data.js'

export default {
    name: 'PrevNext',

    setup() {
        const dataStore = useDataStore()

        return {
            dataStore,
        }
    },
}
</script>
