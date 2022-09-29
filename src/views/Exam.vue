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

        return {
            dataStore,
            genStore
        }
    },

    mounted() {
        this.countDown;
    },

    methods: {
        //submit after countdown
        countDown() {
            const duration = this.dataStore.details.duration;
            console.log(duration)
            setTimeout(() => {
                const bodyData = {
                    student: this.dataStore.studentId,
                    answers: this.dataStore.pickedAns
                }

                // post method
                const res = fetch(`http://localhost:8000/mark`, {
                    method: 'POST',
                    headers: { "X-CSRFToken": this.genStore.token },
                    body: JSON.stringify(bodyData)
                })
                const data = res.json()
                this.genStore.setSubmitTaskId(data.task);

                this.$router.replace({path: '/submited'});
            }, parseInt(duration));
        },
    },
}
</script>
