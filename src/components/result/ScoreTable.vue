<template>
    <table>
        <tr>
            <th>SN</th>
            <th>Student Name</th>
            <th>Student Id</th>
            <th>Score</th>
            <th>%Score</th>
        </tr>
        <ScoreRow v-for="result in results.students" :result="result" :key="result.student_id" :index="results.students.indexOf(result) + 1" :total="results.total_score"/>
    </table>
</template>

<script>
import ScoreRow from './ScoreRow.vue';

export default{
    name: 'ScoreTable',

    components: {
        ScoreRow,
    },

    props: {
        results: Object,
    },
}
</script>
