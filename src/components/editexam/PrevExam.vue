<template>
    <div class="bg-brown2">
        <div class="grid grid-col-1 justify-items-center xl:justify-items-start xl:ml-96">
            <div class=" text-base lg:text-lg font-medium lg:font-semibold">
                <h2>{{ exam.name }}</h2>
                <h2>{{ exam.mark }} Marks</h2>
                <h2>{{ exam.start_time }}</h2>
                <h2>{{ exam.duration }}</h2>
            </div>
        </div>

        <div class="w-full p-3">
            <span class="text-semibold text-lg lg:text-xl p-3 font-semibold">{{ questions.length }} Questions </span>
        </div>

        <div class="bg-brown3 space-y-2">
            <div v-for="question in questions" :key="question.id" class="hover:shadow-lg p-3">
                <div class="text-base lg:text-lg text-semibold p-3 mt-1">
                    <span>{{ question.question }}</span>
                    <span class="hidden">{{ question.id }}</span>
                </div>
                <div class="ml-5 relative flex justify-left">
                    <section class="grid grid-cols-1 p-3 space-y-2 place-items-stretch w-full">
                        <div v-for="option in question.options" :key="option.id" class="flex border border-dark1 min-w-min cursor-pointer hover:shadow-lg text-left min-h-max">
                            <div class="hidden">{{ option.id }}</div>
                            <p class="text-sm lg:text-base p-3">{{ option.option }}</p>
                        </div>
                    </section>
                </div>
            </div>
            <div class="w-full border-b border-dark1"></div>
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

        getEdit(){
            const data = document.getElementById('change').value;
        },

        editExam(id, type, data) {
            //this function would be called by another function 
            const bodyData = {
                type: type,
                id: id,
                data: data
            };

            fetch(`http://localhost:8000/prev/${link}`, {
                method: 'PUT',
                headers: { "X-CSRFToken": this.token },
                body: JSON.stringify(bodyData)
            })
            .then((response) => response.json())
            .then((data) => {
                console.log(data);
                if (data.type == 'question') {
                    const index = questions.findIndex(quest => {
                        return quest.id === data.id;
                    });
                    if (index !== -1) {
                        questions[index].question = data.data;
                    }
                }

                else if (data.type == 'option') {
                    const index = questions.options.findIndex(opt => {
                        return opt.id === data.id;
                    });
                    if (index !== -1) {
                        questions.options[index].option = data.data;
                    }
                }

                else if (data.type == 'option') {
                    const index = questions.findIndex(quest => {
                        return quest.id === data.id;
                    });
                    if (index !== -1) {
                        questions[index].answer = data.data;
                    }
                }
                
            })
        },
    },
}
</script>
