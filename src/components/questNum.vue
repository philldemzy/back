<template>
    <div class="w-full border-b border-dark1">
        <span class="text-semibold text-base lg:text-lg p-3 font-semibold">Question {{ curr }} of {{ total }}</span>
    </div>
</template>

<script>
export default {
    name: 'questNum',

    props: {
        curr: Number,
        total: Number,
    },
}
</script>
