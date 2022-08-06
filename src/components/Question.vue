<template>
    <div class="text-base lg:text-2xl text-semibold p-3 mt-7">
        {{ question.question }}
    </div>
</template>

<script>
export default {
    name: 'Question',

    props: {
        question: Object,
    }
}
</script>
