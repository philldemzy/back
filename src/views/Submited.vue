<template>
    <Logo/>
    <Status/>
</template>

<script>
import Status from '../components/status/Status.vue';
import Logo from '@/components/header/Logo.vue';

export default {
    name: 'Submited',

    components: {
        Status,
        Logo
    },
}
</script>
