<template>
    <button :class="[questions.indexOf(question) > 0 ? 'hover:bg-brown4 hover:text-white hover:border-0' : '','uppercase p-2 border font-semibold border-dark1 w-24']">previous</button>
    <button :class="[questions.indexOf(question) < questions.length - 1 ? 'hover:bg-brown4 hover:text-white hover:border-0' : '','place-self-end uppercase p-2 border font-semibold border-dark1 w-24']">next</button>
</template>

<script>
export default {
    name: 'PrevNext',

    props: {
        questions: Array,
        question: Object,
    },
}
</script>