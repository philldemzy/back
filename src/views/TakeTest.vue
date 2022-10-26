<template>
    <Logo/>

    <div class="grid bg-brown2 justify-items-center">
        <div id="exam_dets" class="grid gap-y-2 p-2.5 lg:p-6 lg:w-2/3">
            <div class="flex space-x-4 lg:space-x-6 w-3/4 lg:w-full">
                <h4 class="text-lg lg:text-2xl w-1/2">Title</h4>
                <span class="lg:w-3/4 w-1/2 text-sm lg:text-md inline-block mt-2 uppercase font-medium">{{ dataStore.examDet.name }}</span>
            </div>
            <div v-show="dataStore.examDet.instructions" class="flex space-x-4 lg:space-x-6 w-3/4 lg:w-full">
                <h4 class="text-lg lg:text-2xl w-1/2">Instructions</h4>
                <span class="lg:w-3/4 w-1/2 text-sm lg:text-md inline-block mt-2 uppercase font-medium">{{ dataStore.examDet.instructions }}</span>
            </div>
            <div class="flex space-x-4 lg:space-x-6 w-3/4 lg:w-full">
                <h4 class="text-lg lg:text-2xl w-1/2">Time</h4>
                <span class="lg:w-3/4 w-1/2 text-sm lg:text-md inline-block mt-2 uppercase font-medium">{{ displayDate(dataStore.examDet.start_time) }}</span>
            </div>
            <div class="flex space-x-4 lg:space-x-6 w-3/4 lg:w-full">
                <h4 class="text-lg lg:text-2xl w-1/2">Score</h4>
                <span class="lg:w-3/4 w-1/2 text-sm lg:text-md inline-block mt-2 uppercase font-medium">{{ dataStore.examDet.mark }}</span>
            </div>
            <div class="flex space-x-4 lg:space-x-6 w-3/4 lg:w-full">
                <h4 class="text-lg lg:text-2xl w-1/2">Duration</h4>
                <span class="lg:w-3/4 w-1/2 text-sm lg:text-md inline-block mt-2 uppercase font-medium">{{ dataStore.examDet.duration }}</span>
            </div>
            <div class="pt-3 flex lg:space-x-6 w-3/4 lg:w-full">
                <p id="countdown" style="visibility: hidden;" class="text-lg lg:text-2xl w-1/2">{{ dataStore.examDet.ended }}</p>
                <div id="count" class="flex lg:w-3/4 w-1/2">
                    <div id="days" class="grid grid-rows-2 pr-3">
                        <span class="flex justify-center text-2xl lg:text-3xl">0</span>
                        <span class="flex justify-center text-sm lg:text-md">days</span>
                    </div>
                    <h2 id="first" class="text-md lg:text-lg font-black mt-2 pr-3">:</h2>
                    <div id="hours" class="grid grid-rows-2 pr-3">
                        <span class="flex justify-center text-2xl lg:text-3xl">0</span>
                        <span class="flex justify-center text-sm lg:text-md">hours</span>
                    </div>
                    <h2 class="text-md lg:text-lg font-black mt-2 pr-3">:</h2>
                    <div id="minutes" class="grid grid-rows-2 pr-3">
                        <span class="flex justify-center text-2xl lg:text-3xl">0</span>
                        <span class="flex justify-center text-sm lg:text-md">minutes</span>
                    </div>
                    <h2 class="text-md lg:text-lg font-black mt-2 pr-3">:</h2>
                    <div id="seconds" class="grid grid-rows-2 pr-3">
                        <span class="flex justify-center text-2xl lg:text-3xl">0</span>
                        <span class="flex justify-center text-sm lg:text-md">seconds</span>
                    </div>
                </div>
            </div>
            <form method="post" class="pt-7 lg:space-y-3">
                <div class="lg:flex lg:space-x-20">
                    <label class="my-4 lg:mt-0 text-lg lg:text-2xl lg:w-1/5" for="student_id">Student Id</label>
                    <input type="text" id="student_id" name="student_id" class="rounded-t-sm lg:rounded-t-md hover:border text-lg lg:text-2xl h-9 lg:h-14 border-dark1 rounded-sm w-full lg:w-3/4">
                </div>
                <div class="lg:flex lg:space-x-20">
                    <label class="my-4 lg:mt-0 text-lg lg:text-2xl lg:w-1/5" for="student_name">Student Name</label>
                    <input type="text" id="student_name" name="student_name" class="rounded-b-sm lg:rounded-b-md hover:border text-lg lg:text-2xl h-9 lg:h-14 border-dark1 rounded-sm w-full lg:w-3/4">
                </div>
                <div class="flex flex-row-reverse mt-6 lg:mt-0 sm:mt-8 lg:w-full">
                    <input @click="submitTakeTest" type="submit" value="Start Exam" class="hover:-translate-y-0.5 bg-brown4 hover:bg-brown3 inline-block px-3 py-2 lg:px-5 lg:py-3 rounded-lg uppercase tracking-wider font-semibold text-sm text-white shadow-lg sm:text-base">
                </div>
            </form>
        </div>

        <div id="404_exam" class="hidden grid bg-brown2 justify-items-center">
            <img class="w-1/3 h-52" src="https://banner2.cleanpng.com/20180511/pee/kisspng-http-404-error-web-browser-5af65b7e3e0fb0.9779316415260947182542.jpg" alt="404 Error">
            <h1 class="font-serif text-light text-lg lg:text-2xl">Exam not found, please cross check exam link.</h1>
        </div>
    </div>
</template>

<script>
import Logo from '@/components/header/Logo.vue';
import { useRoute } from 'vue-router';
import { useDataStore } from '../store/data.js'
import { useGenStore } from '@/store/store.js';

export default {
    name: "TakeTest",

    components: {
        Logo,
    },

    data() {
        return {
            theFunc: Number,
            time_: '',
        }
    },

    setup() {
        const dataStore = useDataStore();
        const genStore = useGenStore();
        const link = useRoute().params.link;

        return {
            dataStore,
            genStore,
            link
        }
    },

    created() {
        this.fetchData(this.link)
    },

    watch: {
        time_(newTime, oldTime) {
            this.examCountDown(newTime)
        }
    },
 
    methods: {
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

        async submitTakeTest(event) {
            event.preventDefault();

            //get value of all inputs
            let studentId = document.getElementById("student_id").value;
            let studentName = document.getElementById("student_name").value;

            //put all into formdata
            let formData = new FormData();
            formData.append('student_id', studentId);
            formData.append('student_name', studentName);

            this.dataStore.setStudentId({
                test_link: this.link,
                student_id: studentId,
                student_name: studentName
            })

            //send data abd get response save in datastore
            const allData = await this.getExam(formData);
            if (!allData.expired && !allData.not_time) {
                //save in local storage
                localStorage.setItem(`test${this.link}`, JSON.stringify(allData));
                localStorage.setItem(`studentInfo${this.link}`, JSON.stringify(this.dataStore.studentId));

                this.dataStore.setQuestions(this.doOptions(this.shuffuleQuest(allData.questions))),
                this.dataStore.setDetails(allData),
                this.dataStore.setCurrQuestion()

                clearInterval(this.theFunc);
                document.getElementById("student_id").value = null;
                document.getElementById("student_name").value = null;

                this.$router.push({path: `/exam/${this.link}`});
            }
            else if (allData.expired) {
                alert(`${allData.expired}`);
            }

            else if (allData.not_time) {
                document.getElementById('count').remove();
                alert(`${allData.not_time}`);
            }

        },

        // fetch data
        async fetchData(testLink) {
            //get method
            const res = await fetch(`${process.env.VUE_APP_ROOT_API}/take/${testLink}`)
            const data = await res.json()
            if (data.name) {
                this.time_ = data.ended
                this.dataStore.setExamDet(await data);
            }
            //display 404 exam for loading exam get details of exam before and in exam if exam not there get
            else if (data.error) {
                document.getElementById('exam_dets').style.display = 'none';
                document.getElementById('404_exam').style.display = 'block';
                alert('Error Exam was not found.')
            }
        },

        async getExam(formData) {
            // post method
            let headers = new Headers();
            headers.append('X-CSRFToken', `${this.genStore.token}`);

            const res = await fetch(`${process.env.VUE_APP_ROOT_API}/take/${this.link}`, {
                method: 'POST',
                body: formData,
                headers: headers,
                credentials: 'include'
            })
            const data = await res.json()
            return data
        },

        shuffuleQuest(arr) {
            for (let i = arr.length - 1; i > 0; i--) {
                const j = Math.floor(Math.random() * (i + 1));
                const temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
            return arr;
        },

        doOptions(arrObj) {
            const alphabet = 'ABCDEF';
            const retrnArr = arrObj.map(
                (ques) => {
                    this.shuffuleQuest(ques.options);
                    const optns = ques.options.map((option, index) => ({
                        main:option,
                        alpha:alphabet[index]
                    }));
                    ques.options = optns;
                    return ques;
                });
            return retrnArr;
        },

        examCountDown(_end) {
            let update;

            if (_end !== true) {
                let end = new Date(_end);

                update = setInterval( function() {
                    try {
                        let now = new Date();
                        let diff = end.getTime() - now.getTime();
                        if (diff <= 1) {
                            document.getElementById("count").innerHTML = "EXAM IN PROGRESS";
                            clearInterval(update);
                        }
                        let days = Math.floor( diff / (1000 * 3600 * 24) );
                        let hours = Math.floor( (diff % (1000 * 3600 * 24)) / (1000 * 3600) );
                        let minutes = Math.floor( (diff % (1000 * 3600)) / (1000 * 60) );
                        let seconds = Math.floor( (diff % (1000 * 60)) / 1000 );

                        if (days == 0) {
                            document.getElementById("days").style.display = "none";
                            document.getElementById("first").style.display = "none";
                        }

                        if (document.getElementById("days").style.display != "none") {
                            document.getElementById("days").children[0].innerHTML = days;
                        }
                        document.getElementById("hours").children[0].innerHTML = hours;
                        document.getElementById("minutes").children[0].innerHTML = minutes;
                        document.getElementById("seconds").children[0].innerHTML = seconds;
                    }
                    catch (err) {}
                }, 1000)
                return update;
            }
            else {
                document.getElementById("count").innerHTML = "EXAM ENDED";
                document.getElementById("count").className = "text-lg lg:text-xl font-bold";
            }
        }
    }
}
</script>
