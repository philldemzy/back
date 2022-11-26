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

        <div v-show="err && resp" class="flex justify-center pt-3">
            <h2 class="text-align-center text-md lg:text-xl text-semibold font-serif">{{ errorMsg }}</h2>
        </div>

        <div v-show="!err && resp" class="grid grid-col-1 p-5">
            <div class="flex">
                <h2 class="mt-5 text-green-700 text-xl lg:text-2xl">Success !!</h2>
                <svg xmlns="http://www.w3.org/2000/svg" class="lg:h-20 lg:w-16 h-16 w-14 lg:stroke-4 stroke-2 text-green-900" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7" />
                </svg>
            </div>
            <h5 class="text-align-center text-zinc-900 text-md lg:text-lg">Your test has been created successfully. <i class="uppercase">Please copy both links provided</i></h5>

            <div class="grid mt-4">
                <h3 class="font-mono"><span class="text-md lg:text-xl text-semibold font-serif">Examiner Link:</span> Link would be used to Check statistics, result of exam it can be used to edit the exam <u>only for examiner</u></h3>
                <div class="flex space-x-3 mt-1">
                    <span class="text-md font-serif pt-3">EXAMINER LINK</span>
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="mt-3 w-6 h-6">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M17.25 8.25L21 12m0 0l-3.75 3.75M21 12H3" />
                    </svg>
                    <span @click="goTo" class="text-semibold font-mono p-2 bg-dark1 opacity-90 text-white rounded lg:rounded-md">{{ genStore.newTest.examiner_link }}</span>
                </div>
            </div>
            <div class="grid mt-3">
                <h3 class="font-mono"><span class="text-md lg:text-xl text-semibold font-serif">Test Link: </span> Link would be used for students to navigate to take test <u>for students</u></h3>
                <div class="flex space-x-3 mt-1">
                    <span class="text-md font-serif pt-3">TEST LINK</span>
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="mt-3 w-6 h-6">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M17.25 8.25L21 12m0 0l-3.75 3.75M21 12H3" />
                    </svg>
                    <span class="text-semibold font-mono p-2 bg-dark1 opacity-90 text-white rounded lg:rounded-md">{{ genStore.newTest.test_link }}</span>
                </div>
            </div>
        
            <button @click="previewExam" class="p-3 border border-dark1 mt-4 md:w-1/3 md:mx-auto hover:-translate-y-1 dutation-500 transform ease-in-out">Preview Exam</button>
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
            err: false,
            errorMsg: null,
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
            fetch(`${process.env.VUE_APP_ROOT_API}/exam/setup/${this.genStore.newTest.task}`)
            .then((response) => response.json())
            .then((data) => {
                if (data.state == 'SUCCESS') {
                    this.resp = true
                    clearInterval(checkStat)
                    console.log(data)
                    if (data.info !== true) {
                        this.err = true;
                        this.errorMsg = data.info;
                    }
                }
                else if  (data.state == 'FAILURE') {
                    this.resp = true
                    this.err = true;
                    this.errorMsg = data.info;
                    clearInterval(checkStat)
                }
            });
        }, 500)
    },

    methods: {
        previewExam () {
            this.$router.push({path: `/preview/${this.genStore.newTest.examiner_link}`})
        },
    },
}
</script>
