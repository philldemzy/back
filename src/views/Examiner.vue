<template>
    <Logo/>

    <div class="bg-brown2 space-y-4">
        <div class="grid grid-col-1 justify-items-center xl:justify-items-start xl:ml-96">
            <div class=" text-base lg:text-lg font-medium lg:font-semibold">
                <h2>{{ examDets.title }}</h2>
                <h2>{{ examDets.total_score }} Marks</h2>
                <h2>{{ examDets.start_time }}</h2>
                <h2>{{ examDets.duration }}</h2>
            </div>
        </div>
        <ScoreOverview v-if="done" :results="dataStore.results"/>
        <ScoreTable v-if="done" :results="dataStore.results"/>
        <p v-show="!done" class="text-center text-sm px-5 font-mono">Sorry Examination has not ended yet. You can only get the results after examination has been done.</p>
        <div v-show="!done" class="grid grid-col-1 justify-items-center xl:justify-items-start xl:ml-96 pb-5">
            <div @click="goToEdit" class="p-3 bg-brown3 rounded-2xl hover:-translate-y-1">
                Edit Exam
            </div>
        </div>
        
        <div v-if="done" class="grid grid-col-1 justify-items-center xl:justify-items-start xl:ml-96 pb-5">
            <div class="">
                <button  @click="setExcelFile" class="p-3 bg-brown3 rounded-2xl hover:-translate-y-1"> DOWNLOAD </button>
            </div>
        </div>
    </div>
    <div class="h-5"></div>
</template>

<script>
import ScoreTable from '@/components/result/ScoreTable.vue';
import ScoreOverview from '@/components/result/ScoreOverview.vue';
import Logo from '@/components/header/Logo.vue';
import { useDataStore } from '@/store/data';
import { useRoute } from 'vue-router';
import { writeXLSX } from 'xlsx';

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
            done: false
        }
    },

    created() {
        this.fetchFile(this.link)
    },

    methods: {
        goToEdit() {
            this.$router.push({path: `/preview/${this.link}`})
        },

        async fetchFile(link) {
            //going to fetch
            const res = await fetch(`http://localhost:8000/check/${link}`)
            const data = await res.json()
            this.examDets = data;
            if (data.students) {
                this.dataStore.setResults(data)
                this.done = true
            }
        },

        setExcelFile() {
            //create excel file for download
            const worksheet = XLSX.utils.json_to_sheet(rows);
            const workbook = XLSX.utils.book_new();
            XLSX.utils.book_append_sheet(workbook, worksheet, "results");
            XLSX.utils.sheet_add_aoa(worksheet, [["Id", "Name", "Score"]], { origin: "A1" });
            XLSX.writeFile(workbook, "results.xlsx");
        },

        getFile() {
            return {
                title: 'GET 101',
                total_score: 70,
                start_time: '2022-08-25T15:55:00+00:00',
                duration: '30 mins',
                /*completed: false*/
                students: [
                    {student_id: "16/67am/076", student_name: 'Ayandele Demilade', score: 70},
                    {student_id: "16/67am/070", student_name: 'Dele lade', score: 70},
                    {student_id: "16/67am/046", student_name: 'Bukola Fola', score: 35},
                    {student_id: "16/67am/167", student_name: 'Joke Bolaji', score: 60},
                    {student_id: "16/67am/089", student_name: 'Frank Paul', score: 41},
                    {student_id: "16/67am/111", student_name: 'Olamide j k', score: 21},
                    {student_id: "16/67am/104", student_name: 'Sy Brandon', score: 32},
                    {student_id: "16/67am/278", student_name: 'JA Bantu', score: 54},
                    {student_id: "16/67am/090", student_name: 'Williams Demola', score: 26},
                    {student_id: "16/67am/073", student_name: 'Faruk Muhammed', score: 69},
                ]
            }
        }
    },
}
</script>
