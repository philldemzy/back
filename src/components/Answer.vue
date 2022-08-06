<template>
    <div @click="$emit('answer-picked', option.main);" :class="[option.main === pickedAns ? 'bg-amber-900 text-orange-50 border-orange-50' : 'border-dark1 hover:shadow-lg' ,'flex border min-w-min cursor-pointer text-left min-h-max']">
        <div :class="[option.main === pickedAns ? 'bg-amber-900 text-orange-50 border-orange-50' : 'border-dark1' ,'text-lg lg:text-2xl font-semibold border-r p-2 md:p-3 lg:p-4 inline-block align-middle']">{{ option.alpha }}</div>
        <p class="text-sm md:text-base lg:text-xl p-3">{{ option.main }}</p>
    </div>
</template>

<script>
export default {
    name: 'Answer',

    props: {
        option: Object,
        pickedAns: String,
    },
}
</script>
