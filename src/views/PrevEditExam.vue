<template>
    <Logo/>
    <PrevExam/>
</template>

<script>
import Logo from '@/components/header/Logo.vue';
import PrevExam from '@/components/editexam/PrevExam.vue';

export default{
    name: 'PrevEditExam',

    components: {
        Logo,
        PrevExam
    },
}
</script>
