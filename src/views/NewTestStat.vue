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

        <div v-show="resp" class="p-5">
            <h2>Your exam has been processed successfully</h2>

            <span>Examiner Link to Check statistics and result of exam <i>only for examiner</i>: ngunrurhus44</span>
            <span>Test Link provided for students to take the exam: xjehsgu45</span>
        
            <button>Preview Exam</button>
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
            let data = this.checkStatus(this.genStore.newTestTaskId);
            if (data.state == 'SUCCESS') {
                this.resp = true
                clearInterval(checkStat)
            }
            else if  (data.state == 'FAILURE') {
                this.resp = true
                clearInterval(checkStat)
            }
        }, 500)
        
    },

    methods: {
        checkStatus(statusId) {
            const res = fetch(`http://localhost:8000/setup/${statusId}`)

            const data = res.json()
            return data;
        },
    },
}
</script>
