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
                    <label class="my-4 text-lg lg:text-xl lg:w-1/6" for="exam_dur">Duration</label>
                    <input placeholder="IN MINUTES" type="text" id="exam_dur" name="exam_dur" class="hover:outline text-lg lg:text-2xl h-9 lg:h-14 border-1 border-dark1 rounded-sm w-full lg:w-3/4">
                </div>
                <div class="lg:flex">
                    <label class="my-4 text-lg lg:text-xl lg:w-1/6" for="test_instructions">Instructions</label>
                    <input type="text" id="test_instructions" name="test_instructions" class="hover:outline text-lg lg:text-2xl h-9 lg:h-14 border-1 border-dark1 rounded-sm w-full lg:w-3/4">
                </div>
                <div class="lg:flex">
                    <span class="my-4 text-lg lg:text-xl lg:w-1/6">Test File</span>
                    <label class="flex w-full lg:w-3/4" for="test_file">
                        <input type="file" id="test_file" name="exam_file" accept=".txt" class="hidden lg:h-14 h-9">
                        <div class="rounded-bl-md text-md lg:text-xl inline-block py-1 lg:py-3 align-middle text-center rounded-sm w-3/5 bg-white h-9 lg:h-14" id="imageName"></div>
                        <div class="text-clip overflow-hidden rounded-br-md text-md lg:text-xl border-1 border-dark1 inline-block py-1 lg:py-3 align-middle text-center hover:outline rounded-sm w-2/5 bg-gray-400 h-9 lg:h-14">Select File</div>
                    </label>
                </div>
                <div class="flex flex-row-reverse mt-6 lg:mt-0 sm:mt-8 lg:w-11/12">
                    <input type="submit" value="Submit" class="hover:-translate-y-0.5 bg-brown4 hover:bg-brown3 inline-block px-3 py-2 lg:px-5 lg:py-3 rounded-lg uppercase tracking-wider font-semibold text-sm text-white shadow-lg sm:text-base">
                </div>
            </form>
        </div>
    </div>
</template>

<script>
import Logo from '@/components/header/Logo.vue';

export default {
    name: 'NewTest',

    components: {
        Logo,
    },

    mounted() {
        this.fileChange();
    },

    methods: {
        fileChange() {
            let input = document.getElementById("test_file");
            let imageName = document.getElementById("imageName")

            input.addEventListener("change", ()=>{
                let inputImage = document.querySelector("input[type=file]").files[0];

                imageName.innerText = inputImage.name;
            })
        },
    },
}
</script>
