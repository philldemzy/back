<template>
    <div class="grid lg:grid-col-2">
        <div class="shadow-lg rounded-lg overflow-hidden">
            <canvas class="p-5" id="chart"></canvas>
        </div>
        <div class="p-3">
            <span>Top performers</span>
            <div class="p-1 space-x-3" v-for="best in topAndLast.best" :key="best.student_id">
                <h4>{{ best.student_name }}</h4>
                <h4>{{ best.score }}</h4>
            </div>
            <div class="h-3 lg:h-4"></div>
            <span>Poorest performers</span>
            <div class="p-1 space-x-3" v-for="worst in topAndLast.worst" :key="worst.student_id">
                <h4>{{ worst.student_name }}</h4>
                <h4>{{ worst.score }}</h4>
            </div>
            
        </div>
    </div>
</template>

<script>
import Chart from 'chart.js'

export default{
    name: 'ScoreOverview',

    props: {
        results: Object,
    },

    mounted() {
        const chartData = {
            type: "pie",
            data: {
                labels: ["50% or more", "Less than 50%"],
                datasets: [
                    {
                        label: "Overview",
                        data: this.totalPass(this.results),
                        backgroundColor: [
                            "#876353",
                            "#0d0404",
                        ],
                        hoverOffset: 4,
                    },
                ],
            },
            options: {},
        }
        const chartElement = document.getElementById('chart');
        new Chart(chartElement, chartData);
    },

    methods: {
        totalPass(obj) {
            const passMrk = obj.total_score / 2;
            const totPass = obj.students.filter((student) => {
                if (student.score >= passMrk) {
                    return student;
                };
            });
            const totFail = obj.students.filter((student) => {
                if (student.score < passMrk) {
                    return student;
                };
            });
            return [totPass.length, totFail.length];
        },

        topAndLast(obj) {
            const first = obj.students.reduce(
                (biggest, student) => biggest.score > student.score ? biggest : student
            );

            const last = obj.students.reduce(
                (smallest, student) => smallest.score < student.score ? smallest : student
            );

            const best = obj.students.filter(
                (student) => student.score === first.score 
            );
            
            const worst = obj.students.filter(
                (student) => student.score === last.score
            )

            return {
                best: best,
                worst: worst
            }
        }
    }
}
</script>
