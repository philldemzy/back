<template>
    <div class="bg-brown2">
        <div class="grid grid-col-1 justify-items-center xl:justify-items-start xl:ml-96">
            <div class=" text-base lg:text-lg font-medium lg:font-semibold">
                <h2>{{ exam.name }}</h2>
                <h2>{{ exam.mark }} Marks</h2>
                <h2>{{ displayDate(exam.start_time) }}</h2>
                <h2>{{ exam.duration }}</h2>
            </div>
            <h2 class="my-3 text-sm font-mono">EXAM questions, answers and options can be edited from here</h2>
        </div>

        <div class="w-full p-3">
            <span class="text-semibold text-lg lg:text-xl p-3 font-semibold">{{ questions.length }} Questions </span>
        </div>

        <div class="bg-brown3 space-y-2">
            <div v-for="question in questions" :key="question.id" class="hover:shadow-lg p-3 lg:w-2/3">
                <div class="flex text-base lg:text-lg text-semibold p-3 mt-1">
                    <span class="hidden">{{ question.id }}</span>
                    <span class="md:text-base text-sm">{{ question.question }}</span>
                    <svg @click="getQuestion" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="ml-20 my-auto transition ease-in-out hover:translate-y-1 stroke-1 duration-500 hover:scale-125 w-4 h-4 lg:w-6 lg:h-6">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M16.862 4.487l1.687-1.688a1.875 1.875 0 112.652 2.652L10.582 16.07a4.5 4.5 0 01-1.897 1.13L6 18l.8-2.685a4.5 4.5 0 011.13-1.897l8.932-8.931zm0 0L19.5 7.125M18 14v4.75A2.25 2.25 0 0115.75 21H5.25A2.25 2.25 0 013 18.75V8.25A2.25 2.25 0 015.25 6H10" />
                    </svg>
                </div>
                <div class="ml-5 relative flex justify-left">
                    <section class="grid grid-cols-1 p-3 space-y-2 place-items-stretch w-full">
                        <div v-for="option in question.options" :key="option.id" :class="[ question.answer === option.option ? 'bg-amber-900 text-orange-50 border-orange-50' : 'border-dark1' ,'flex border min-w-min justify-between cursor-pointer hover:shadow-lg text-left min-h-max']">
                            <div class="hidden">{{ option.id }}</div>
                            <p class="text-sm lg:text-base font-light p-3">{{ option.option }}</p>
                            <svg @click="getOption" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="my-auto mr-5 transition ease-in-out hover:translate-y-1 stroke-1 duration-500 hover:scale-125 w-4 h-4 lg:w-6 lg:h-6">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M16.862 4.487l1.687-1.688a1.875 1.875 0 112.652 2.652L10.582 16.07a4.5 4.5 0 01-1.897 1.13L6 18l.8-2.685a4.5 4.5 0 011.13-1.897l8.932-8.931zm0 0L19.5 7.125M18 14v4.75A2.25 2.25 0 0115.75 21H5.25A2.25 2.25 0 013 18.75V8.25A2.25 2.25 0 015.25 6H10" />
                            </svg>
                        </div>
                    </section>
                </div>
                <div class="flex">
                    <span class="hidden"> {{ question.id }} </span>
                    <span class="mt-1 font-medium">ANSWER: </span>
                    <span class="ml-3 text-align-center font-light text-lg">{{ isAnswer(question) }}</span>
                    <svg @click="getAnswer" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="ml-20 my-auto transition ease-in-out hover:translate-y-1 stroke-1 duration-500 hover:scale-125 w-4 h-4 lg:w-6 lg:h-6">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M16.862 4.487l1.687-1.688a1.875 1.875 0 112.652 2.652L10.582 16.07a4.5 4.5 0 01-1.897 1.13L6 18l.8-2.685a4.5 4.5 0 011.13-1.897l8.932-8.931zm0 0L19.5 7.125M18 14v4.75A2.25 2.25 0 0115.75 21H5.25A2.25 2.25 0 013 18.75V8.25A2.25 2.25 0 015.25 6H10" />
                    </svg>
                </div>
                <div class="w-full border-b border-dark1"></div>
            </div>
            <div id="editExam" class="hidden fixed bottom-2 w-full">
                <div class="grid relative justify-items-end w-full lg:w-2/3 mr-5 space-y-3 px-4">
                    <svg @click="closeEditForm" xmlns="http://www.w3.org/2000/svg" class="justify-self-end h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                        <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z" clip-rule="evenodd" />
                    </svg>
                    <form action="" class="flex w-full mx-auto h-10 lg:h-14 transition -translate-y-2 duration-500 opacity-90">
                        <input type="text" id="edit" class="w-2/3">
                        <button @click="mainEditExam" class="px-2 w-1/3 lowercase bg-dark1 text-white">submit</button>
                    </form>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { useRoute } from 'vue-router';

export default{
    name: 'PrevExam',

    data() {
        return {
            exam: {},
            questions: [],
            targetInfo: {},
            token: null,
        }
    },

    setup() {
        //const dataStore = useDataStore();
        const link = useRoute().params.link;

        return {
            link,
        }
    },

    created () {
        this.fetchData(this.link);
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

        closeEditForm() {
            let styleClass = document.getElementById('editExam').className
            document.getElementById('editExam').className = `hidden ${styleClass}`
        },

        isAnswer(question) {
            const index = question.options.findIndex((elemn) => {
                return elemn === question.answer
            })

            const ans = index !== -1 ? 'No Answer': question.answer
            return ans
        },

        fetchData(link) {
            fetch(`http://localhost:8000/prev/${link}`)
            .then((response) => response.json())
            .then((data) => {
                this.exam = {
                    name: data.name,
                    start_time: data.start_time,
                    duration: data.duration,
                    mark: data.mark,
                };
                this.questions = data.questions;
                this.token = data.token;
            })
        },

        mainEditExam(event) {
            event.preventDefault();
            const data = document.getElementById('edit').value
            let styleClass = document.getElementById('editExam').className
            document.getElementById('editExam').className = `hidden ${styleClass}`
            if (data.length < 1) {
                return;
            }
            this.targetInfo.data = data;
            document.getElementById('edit').value = '';
            if (this.editExam(this.targetInfo)) {
                this.targetInfo = {};
            }
        },

        getQuestion(event){
            const id = event.target.parentElement.firstChild.innerHTML;
            if (typeof(id) !== 'string' || id.length < 1) {
                alert('An error occured, please retry')
                return;
            }
            let styleClass = document.getElementById('editExam').className
            document.getElementById('editExam').className = styleClass.replace('hidden', '')
            this.targetInfo = {
                type: 'question',
                id: id,
            }
        },

        getOption(event) {
            const id = event.target.parentElement.firstChild.innerHTML;
            if (typeof(id) !== 'string' || id.length < 1) {
                alert('An error occured, please retry')
                return;
            }
            let styleClass = document.getElementById('editExam').className
            document.getElementById('editExam').className = styleClass.replace('hidden', '')
            this.targetInfo = {
                type: 'option',
                id: id,
            }
        },

        getAnswer(event) {
            const id = event.target.parentElement.firstChild.innerHTML;
            if (typeof(id) !== 'string' || id.length < 1) {
                alert('An error occured, please retry')
                return;
            }
            let styleClass = document.getElementById('editExam').className
            document.getElementById('editExam').className = styleClass.replace('hidden', '')
            this.targetInfo = {
                type: 'answer',
                id: id,
            }
            console.log(this.targetInfo)
        },

        editExam(bodyData) {
            //this function would be called by another function 
            fetch(`http://localhost:8000/prev/${this.link}`, {
                method: 'PUT',
                headers: { "X-CSRFToken": this.token },
                body: JSON.stringify(bodyData)
            })
            .then((response) => response.json())
            .then((data) => {
                if (data.type == 'question') {
                    const index = this.questions.findIndex(quest => {
                        return quest.id === data.id;
                    });
                    if (index !== -1) {
                        this.questions[index].question = data.data;
                    }
                }

                else if (data.type == 'option') {
                    let qIndex;
                    let oIndex;
                    for (let i=0; i<this.questions.length; i++) {
                        const index = this.questions[i].options.findIndex(opt => {
                            return opt.id === data.id;
                        });
                        if (index !== -1) {
                            qIndex = i;
                            oIndex = index;
                            break;
                        }
                    }
                    if (oIndex !== -1) {
                        this.questions[qIndex].options[oIndex].option = data.data;
                    }
                }

                else if (data.type == 'answer') {
                    const index = this.questions.findIndex(quest => {
                        return quest.id === data.id;
                    });
                    if (index !== -1) {
                        this.questions[index].answer = data.data;
                    }
                }
            })
            return true;
        },
    },
}
</script>
