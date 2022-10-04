<template>
    <Logo/>

    <div class="bg-brown2 space-y-4">
        <div class="grid grid-col-1 justify-items-center xl:justify-items-start xl:ml-96">
            <div class=" text-base lg:text-lg font-medium lg:font-semibold">
                <h2>{{ examDets.title }}</h2>
                <h2>{{ examDets.total_score }} Marks</h2>
                <h2>{{ displayDate(examDets.start_time) }}</h2>
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
import { utils, writeFile } from 'xlsx';

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
        setExcelFile() {
            //create excel file for download
            const wb = read(this.dataStore.results.students);
            const rows = utils.sheet_to_json(wb.Sheets[wb.SheetNames[0]]);
            const worksheet = utils.json_to_sheet(rows);
            const workbook = utils.book_new();
            utils.book_append_sheet(workbook, worksheet, "results");
            utils.sheet_add_aoa(worksheet, [["Id", "Name", "Score"]], { origin: "A1" });
            writeFile(workbook, "results.xlsx");
        },

        displayDate(date) {
            const days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];
            const months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
            const dispDate = new Date(date);
            const day = days[dispDate.getDay()];
            const month = months[dispDate.getMonth()];
            const hr = dispDate.getHours()
            const mins = dispDate.getMinutes()
            const time = hr > 12 ? `${hr - 12}:${mins} PM` : `${hr}:${mins} AM`;
            return `${day}, ${month} ${dispDate.getDate()}, ${dispDate.getFullYear()} ${time}`;
        },

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
            const worksheet = utils.json_to_sheet(this.dataStore.results.students);
            const workbook = utils.book_new();
            utils.book_append_sheet(workbook, worksheet, "results");
            utils.sheet_add_aoa(worksheet, [["Id", "Name", "Score"]], { origin: "A1" });
            writeFile(workbook, "results.xlsx");
        },

    },
}
</script>
