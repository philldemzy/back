<template>
    <Logo/>

    <div class="bg-brown2 space-y-4">
        <div class="grid grid-col-1 justify-items-center">
            <div class="text-base lg:text-lg font-medium lg:font-semibold">
                <h2>{{ examDets.title }}</h2>
                <h2>{{ examDets.total_score }} Marks</h2>
                <h2>{{ examDets.start_time }}</h2>
                <h2>{{ examDets.duration }}</h2>
            </div>
        </div>
        <ScoreTable :results="dataStore.results"/>
        <!----><ScoreOverview :results="dataStore.results"/>
    </div>
    <!--
    <button @click="fetchFile"> Button for downloading test report in excel format </button>
    -->
</template>

<script>
import ScoreTable from '@/components/result/ScoreTable.vue';
import ScoreOverview from '@/components/result/ScoreOverview.vue';
import Logo from '@/components/header/Logo.vue';
import { useDataStore } from '@/store/data';
import { useRoute } from 'vue-router';

export default{
    name: 'Examiner',

    components: {
        Logo,
        ScoreOverview,
        ScoreTable,
    },

    setup() {
        const dataStore = useDataStore();
        const link = useRoute().params.link;

        return {
            dataStore,
            link,
        }
    },

    data() {
        return{
            examDets: {},
        }
    },

    mounted() {
        //const data = this.fetchFile()
        const data = this.getFile()
        this.examDets = data;
        if (data.students) {
            this.dataStore.setResults(data)
        }
        else if (data.completed === 'not started') {
            //display exam has not started
        }
        else {
            // display exam in progress
        }
    },

    methods: {
        fetchFile() {
            //going to fetch
        },

        getFile() {
            return {
                title: 'GET 101',
                total_score: 70,
                start_time: '2022-08-25T15:55:00+00:00',
                duration: '30 mins',
                students: [
                    {student_id: "16/67am/076", student_name: 'Ayandele Demilade', score: 70},
                    {student_id: "16/67am/070", student_name: 'Dele lade', score: 65},
                    {student_id: "16/67am/046", student_name: 'Bukola Fola', score: 35},
                    {student_id: "16/67am/167", student_name: 'Joke Bolaji', score: 60},
                    {student_id: "16/67am/089", student_name: 'Frank Paul', score: 41},
                    {student_id: "16/67am/111", student_name: 'Olamide j k', score: 53},
                    {student_id: "16/67am/104", student_name: 'Sy Brandon', score: 58},
                    {student_id: "16/67am/278", student_name: 'JA Bantu', score: 54},
                    {student_id: "16/67am/090", student_name: 'Williams Demola', score: 67},
                    {student_id: "16/67am/073", student_name: 'Faruk Muhammed', score: 69},
                ]
            }
        }
    },
}
</script>
