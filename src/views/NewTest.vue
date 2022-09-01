<template>
    <Logo/>
    <div class="bg-[#facea2] w-full grid px-6 sm:px-14 lg:px-0">
        <div class="w-4/5 mx-5 my-4">
            <form method="post" class="flex flex-col w-full space-y-4 justify-items-center">
                {% csrf_token %}
                <div class="lg:flex">
                    <label class="my-4 text-lg lg:text-xl lg:w-1/6" for="test_name">Title</label>
                    <input type="text" id="test_name" name="exam_name" class="hover:outline text-lg lg:text-2xl h-9 lg:h-14 border-1 border-dark1 rounded-sm w-full lg:w-3/4">
                </div>
                <div class="lg:flex">
                    <label class="my-4 text-lg lg:text-xl lg:w-1/6" for="final_score">Final Score</label>
                    <input type="text" id="final_score" name="score" class="hover:outline text-lg lg:text-2xl h-9 lg:h-14 border-1 border-dark1 rounded-sm w-full lg:w-3/4">
                </div>
                <div class="lg:flex">
                    <label class="my-4 text-lg lg:text-xl lg:w-1/6" for="test_date">Date</label>
                    <input type="date" id="test_date" name="exam_date" class="hover:outline text-lg lg:text-2xl h-9 lg:h-14 border-1 border-dark1 rounded-sm w-full lg:w-3/4">
                </div>
                <div class="lg:flex">
                    <label class="my-4 text-lg lg:text-xl lg:w-1/6" for="exam_start_time">Start Time</label>
                    <input type="time" id="exam_start_time" name="exam_start_time" class="hover:outline text-lg lg:text-2xl h-9 lg:h-14 border-1 border-dark1 rounded-sm w-full lg:w-3/4">
                </div>
                <div class="lg:flex">
                    <label class="my-4 text-lg lg:text-xl lg:w-1/6" for="exam_dur">Duration Hours</label>
                    <input placeholder="Total Hours" type="text" id="exam_dur_hr" name="exam_dur" class="hover:outline text-lg lg:text-2xl h-9 lg:h-14 border-1 border-dark1 rounded-sm w-full lg:w-3/4">
                </div>
                <div class="lg:flex">
                    <label class="my-4 text-lg lg:text-xl lg:w-1/6" for="exam_dur">Duration Minutes</label>
                    <input placeholder="Remaining Minutes" type="text" id="exam_dur_mins" name="exam_dur" class="hover:outline text-lg lg:text-2xl h-9 lg:h-14 border-1 border-dark1 rounded-sm w-full lg:w-3/4">
                </div>
                <div class="lg:flex">
                    <label class="my-4 text-lg lg:text-xl lg:w-1/6" for="test_instructions">Instructions</label>
                    <input type="text" id="test_instructions" name="test_instructions" class="hover:outline text-lg lg:text-2xl h-9 lg:h-14 border-1 border-dark1 rounded-sm w-full lg:w-3/4">
                </div>
                <div class="lg:flex">
                    <span class="my-4 text-lg lg:text-xl lg:w-1/6">Test File</span>
                    <label class="flex w-full lg:w-3/4" for="test_file">
                        <input type="file" id="test_file" name="exam_file" accept=".txt" class="hidden lg:h-14 h-9">
                        <div class="rounded-bl-md text-md lg:text-xl inline-block py-1 lg:py-3 align-middle text-center rounded-sm w-3/5 bg-white h-9 lg:h-14" id="fileName"></div>
                        <div class="text-clip overflow-hidden rounded-br-md text-md lg:text-xl border-1 border-dark1 inline-block py-1 lg:py-3 align-middle text-center hover:outline rounded-sm w-2/5 bg-gray-400 h-9 lg:h-14">Select File</div>
                    </label>
                </div>
                <div class="flex flex-row-reverse mt-6 lg:mt-0 sm:mt-8 lg:w-11/12">
                    <input @click="submitNewTest" type="submit" value="Submit" class="hover:-translate-y-0.5 bg-brown4 hover:bg-brown3 inline-block px-3 py-2 lg:px-5 lg:py-3 rounded-lg uppercase tracking-wider font-semibold text-sm text-white shadow-lg sm:text-base">
                </div>
            </form>
        </div>
    </div>
</template>

<script>
import Logo from '@/components/header/Logo.vue';
import { useGenStore } from '@/store/store';

export default {
    name: 'NewTest',

    components: {
        Logo,
    },

    setup() {
        const genStore = useGenStore();
        return {
            genStore
        };
    },

    mounted() {
        this.fileChange();
    },

    methods: {
        async submitNewTest(event) {
            event.preventDefault();

            //get value of all inputs
            let file = document.querySelector("input[type=file]").files[0];
            let testName = document.getElementById("test_name").value;
            let testScore = document.getElementById("final_score").value;
            let testDurHr = document.getElementById("exam_dur_hr").value;
            let testDurMins = document.getElementById("exam_dur_mins").value;
            let testInstructions = document.getElementById("test_instructions").value;
            let testDate = document.getElementById("test_date").value;
            let testStartTime = document.getElementById("exam_start_time").value;

            //put all into formdata
            let formData = new FormData();
            formData.append('test_name', testName);
            formData.append('final_score', testScore);
            formData.append('exam', file);
            formData.append('test_instructions', testInstructions);
            formData.append('hours', testDurHr);
            formData.append('minutes', testDurMins);
            formData.append('time', testDate.slice(2).split("-").reverse().join(':') + ':' + testStartTime);

            //make post request
            // post method
            const res = await fetch(`http://localhost:8000/exam/setup`, {
                method: 'POST',
                headers: {},
                body: formData
            })
            const data = await res.json();
            this.genStore.setNewTestTaskId(data.task);
            this.$router.push({path: '/new/test'});
        },

        fileChange() {
            let input = document.getElementById("test_file");
            let fileName = document.getElementById("fileName")

            input.addEventListener("change", ()=>{
                let inputFile = document.querySelector("input[type=file]").files[0];

                fileName.innerText = inputFile.name;
            })
        },
    },
}
</script>
