<template>
    <div class="grid lg:grid-col-2">
        <!--
        <div class="shadow-lg rounded-lg overflow-hidden">
            <canvas class="p-5" id="chart"></canvas>
        </div>
        -->
        
        <div class="grid justify-end p-3">
            <span class="text-xs font-semibold">Top performers</span>
            <div class="flex p-1 space-x-3" v-for="best in bestAndWorst.best" :key="best.student_id">
                <span class="text-xs">{{ best.student_name }}</span>
                <span class="text-xs">{{ best.score }}</span>
            </div>
            <div class="h-3 lg:h-4"></div>
            <span class="text-xs font-semibold">Poorest performers</span>
            <div class="flex p-1 space-x-3" v-for="worst in bestAndWorst.worst" :key="worst.student_id">
                <span class="text-xs">{{ worst.student_name }}</span>
                <span class="text-xs">{{ worst.score }}</span>
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

    data() {
        return {
            bestAndWorst: {}
        }
    },

    created() {
        this.bestAndWorst = this.topAndLast(this.results)
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
        /** 
        const chartElement = document.getElementById('chart');
        new Chart(chartElement, chartData);
        */
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
