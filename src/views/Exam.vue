<template>
    <header id="header" class="sticky grid grid-cols-2 mx-6">
        <Header />
    </header>
    <main class="grid lg:grid-cols-10 lg:w-full">
        <div id="utilbar" class="hidden lg:block lg:col-span-2 bg-brown2 grid p-3 md:space-x-10 lg:-space-x-1 justify-center">
            <UtilBar />
        </div>

        <div id="main" class="block bg-brown3 lg:col-span-8 space-y-10 border-y">
            <Main />
        </div>
    </main>
</template>

<script>
import Header from '@/components/header/Header.vue'
import UtilBar from '../components/main/UtilBar.vue'
import Main from '../components/main/Main.vue'
import { useDataStore } from '../store/data.js'
import { useGenStore } from '@/store/store.js'
import { useRoute } from 'vue-router';

export default {
    name: 'Exam',

    components: {
        UtilBar,
        Main,
        Header
    },

    setup() {
        const dataStore = useDataStore()
        const genStore = useGenStore()
        const link = useRoute().params.link;
        let allData;

        if (dataStore.questions.length < 1 && !dataStore.details.title) {
            allData = JSON.parse(localStorage.getItem(`test${link}`));
        }

        return {
            dataStore,
            genStore,
            link,
            allData
        }
    },

    mounted() {
        if (this.dataStore.questions.length < 1 && !this.dataStore.details.title) {
            console.log(this.allData)
            this.dataStore.setDetails(this.allData);
            this.dataStore.setCurrQuestion();
            this.dataStore.setQuestions(this.doOptions(this.shuffuleQuest(this.allData.questions)));
        }

        //return seconds from api not milliseconds
        const duration = this.dataStore.details.duration;
        //returns date in isoformat
        const start = this.dataStore.details.start_time;
        
        const before = new Date(start)
        const seconds = duration * 1000
        const future = new Date(before.getTime() + seconds)
        const now = new Date();

        const diff = future.getTime() - now.getTime()
        console.log((diff/1000) / 60);
        setTimeout(() => {
            const bodyData = {
                student: this.dataStore.studentId,
                answers: this.dataStore.pickedAns
            }
            console.log(this.dataStore.studentId)
            // post method
            fetch(`http://localhost:8000/mark`, {
                method: 'POST',
                headers: { "X-CSRFToken": this.genStore.token },
                body: JSON.stringify(bodyData)
            })
            .then((response) => response.json())
            .then((data) => {
                this.genStore.setSubmitTaskId(data.task);
            });
            this.$router.replace({path: '/submited'});
        }, diff)
    },

    methods: {
        shuffuleQuest(arr) {
            for (let i = arr.length - 1; i > 0; i--) {
                const j = Math.floor(Math.random() * (i + 1));
                const temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
            return arr;
        },

        doOptions(arrObj) {
            const alphabet = 'ABCDEF';
            const retrnArr = arrObj.map(
                (ques) => {
                    this.shuffuleQuest(ques.options);
                    const optns = ques.options.map((option, index) => ({
                        main:option,
                        alpha:alphabet[index]
                    }));
                    ques.options = optns;
                    return ques;
                });
            return retrnArr;
        }
    },
}
</script>
