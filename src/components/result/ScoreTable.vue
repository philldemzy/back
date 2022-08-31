<template>
    <div class="flex p-1 md:p-3 xl:w-3/4 xl:justify-center">
        <table class="table-auto w-full">
            <thead class="bg-brown3">
                <tr>
                    <th class="border-b border-dark1 text-left text-sm sm:text-base py-3 pl-2">SN</th>
                    <th class="border-b border-dark1 text-left text-sm sm:text-base">Student Name</th>
                    <th class="border-b border-dark1 text-left text-sm sm:text-base">Student Id</th>
                    <th class="border-b border-dark1 text-left text-sm sm:text-base">Score</th>
                    <th class="border-b border-dark1 text-left text-sm sm:text-base">%Score</th>
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
