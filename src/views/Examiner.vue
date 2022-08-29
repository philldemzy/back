<template>
    <Logo/>
    
    <h2>{{ examDets.title }}</h2>
    <h2>{{ examDets.total_score }}</h2>
    <h2>{{ examDets.start_time }}</h2>
    <h2>{{ examDets.duration }}</h2>
    <ScoreOverview :results="useDataSCore.results"/>
    <ScoreTable :results="useDataSCore.results"/>

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
        const useDataScore = useDataStore();
        const link = useRoute().params.link;

        return {
            useDataScore,
            link,
        };
    },

    data() {
        return{
            examDets: {},
        }
    },

    mounted() {
        const data = this.fetchFile()
        if (data.students) {
            this.useDataScore.setResults(data)
        }
        else if (data.completed === 'not started') {
            this.examDets = data
            //display exam has not started
        }
        else {
            this.examDets = data
            // display exam in progress
        }
    },

    methods: {
        fetchFile() {
            //going to fetch
        },
    },
}
</script>
