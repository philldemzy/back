<template>
    <router-view></router-view>
</template>

<script>
import Header from './components/header/Header.vue'
import { useDataStore } from './store/data.js'

export default {
    name: 'App',

    components: {
        Header,
    },

    setup() {
        const dataStore = useDataStore()

        return {
            dataStore,
        }
    },
}
</script>
