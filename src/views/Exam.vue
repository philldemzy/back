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
        //return seconds from api not milliseconds
        const duration = this.dataStore.details.duration;
        //returns date in isoformat
        const start = this.dataStore.details.start_time;
        const start_time = new Date(start);
        console.log(`start time - ${start_time.getTime()}`)
        const total = start_time.getTime() + (parseInt(duration) * 1000)
        console.log(`total - ${total}`)
        const now = new Date()
        console.log(`now - ${now.getTime()}`)
        const diff = total - now.getTime()
        console.log(`diff - ${diff/1000}`)
        console.log(`now - start ${now.getTime() - start_time.getTime()}`)
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
}
</script>
