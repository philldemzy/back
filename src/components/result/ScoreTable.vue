<template>
    <div class="flex justify-center">
        <table class="table-auto w-full border-collapse">
            <thead class="bg-brown3">
                <tr>
                    <th>SN</th>
                    <th>Student Name</th>
                    <th>Student Id</th>
                    <th>Score</th>
                    <th>%Score</th>
                </tr>
            </thead>      
            <tbody>
                <ScoreRow v-for="result in results.students" :result="result" :key="result.student_id" :index="results.students.indexOf(result) + 1" :total="results.total_score"/>
            </tbody>
        </table>
    </div>
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
