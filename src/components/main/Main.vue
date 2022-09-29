<template>
    <questNum />
    <Counter/>
    <Question />
    <div class="lg:h-4"></div>
    <div class="relative flex justify-center">
        <section class="grid grid-cols-1 p-3 gap-6 place-items-stretch w-full">
            <Answers />
        </section>
    </div>
    <div class="grid grid-cols-2 mx-4">
        <PrevNext/>
    </div>
    <div class="h-0"></div>
</template>

<script>
import questNum from './main/questNum.vue'
import Question from './main/Question.vue'
import Answers from './main/Answers.vue'
import PrevNext from './main/PrevNext.vue'
import Counter from './main/Counter.vue'
import { useDataStore } from '../../store/data.js'

export default {
    name: 'Main',

    components: {
        questNum,
        Question,
        Answers,
        PrevNext,
        Counter
    },

    setup() {
        const dataStore = useDataStore()

        return {
            dataStore,
        }
    },
}
</script>
