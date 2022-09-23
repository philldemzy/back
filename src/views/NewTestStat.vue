<template>
    <Logo/>

    <div class="bg-brown2">
        <div class="flex justify-center pt-3">
            <div v-show="!resp" class="flex flex-row w-1/3 justify-center bg-brown3 p-3 px-5 rounded-md lg:rounded-lg">
                <svg class="animate-spin mt-1 -ml-1 mr-3 h-5 w-5 text-orange-900" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                    <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                    <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                </svg>
                <span class="text-lg text-stone-900">Processing...</span>
            </div>
        </div>

        <div v-show="resp" class="grid grid-col-1 p-5">
            <div class="flex">
                <h2 class="mt-5 text-green-700 text-xl lg:text-2xl">Success !!</h2>
                <svg xmlns="http://www.w3.org/2000/svg" class="lg:h-20 lg:w-16 h-16 w-14 lg:stroke-4 stroke-2 text-green-900" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7" />
                </svg>
            </div>
            <h5 class="text-align-center text-zinc-900 text-md lg:text-lg">Your test has been created successfully</h5>

            <div class="grid mt-4">
                <h3><span class="text-md lg:text-xl text-semibold">Examiner Link: </span> Link would be used to Check statistics and result of exam <u>only for examiner</u></h3>
                <div class="flex space-x-3 mt-1">
                    <span class="text-sm">EXAMINER LINK</span>
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="text-green-400 w-6 h-6">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M11.25 4.5l7.5 7.5-7.5 7.5m-6-15l7.5 7.5-7.5 7.5" />
                    </svg>
                    <span class="text-semibold">{{ genStore.newTest.examiner_link }}</span>
                </div>
            </div>
            <div class="grid mt-3">
                <h3><span class="text-md lg:text-xl text-semibold">Test Link: </span> Link would be used for students to navigate to take test <u>for students</u></h3>
                <div class="flex space-x-3 mt-1">
                    <span class="text-sm">TEST LINK</span>
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="text-green-400 w-6 h-6">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M11.25 4.5l7.5 7.5-7.5 7.5m-6-15l7.5 7.5-7.5 7.5" />
                    </svg>
                    <span @click="goTo" class="text-semibold">{{ genStore.newTest.test_link }}</span>
                </div>
            </div>
        
            <button @click="previewExam" class="p-3 border border-dark1 mt-4">Preview Exam</button>
        </div>
        <div class="h-5"></div>
    </div>

</template>

<script>
import Logo from '@/components/header/Logo.vue';
import { useGenStore } from '@/store/store';

export default{
    name: 'NewTestStat',

    components: {
        Logo
    },

    data() {
        return {
            resp: false,
        }
    },

    setup() {
        const genStore = useGenStore();
        return {
            genStore
        };
    },

    mounted() {
        const checkStat = setInterval( () => {
            fetch(`http://localhost:8000/exam/setup/${this.genStore.newTest.task}`)
            .then((response) => response.json())
            .then((data) => {
                if (data.state == 'SUCCESS') {
                    this.resp = true
                    clearInterval(checkStat)
                }
                else if  (data.state == 'FAILURE') {
                    this.resp = true
                    clearInterval(checkStat)
                }
            });
        }, 500)
    },

    methods: {
        goTo() {
            this.$router.push({path: `/take_test/${this.genStore.newTest.test_link}`})
        },
    },
}
//pRUPBOlTVm
</script>
