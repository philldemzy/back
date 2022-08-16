<template>
    <Status/>
</template>

<script>
import Status from '../components/status/Status.vue';
import { useGenStore } from '../store/store.js'

export default {
    name: 'Submited',

    setup() {
        const genStore = useGenStore();
    },

    components: {
        Status,
    },
}
</script>
