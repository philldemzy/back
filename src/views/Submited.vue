<template>
    <Status/>
</template>

<script>
import Status from '../components/status/Status.vue';
import { useSuccessStore } from '../store/success.js'

export default {
    name: 'Submited',

    setup() {
        const successStore = useSuccessStore();
    },

    components: {
        Status,
    },
}
</script>
