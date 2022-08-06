<template>
    <header id="header" class="sticky grid grid-cols-2 mx-6">
        <Header />
    </header>
    <main class="grid lg:grid-rows-6 lg:grid-flow-col">
        <div id="utilbar" class="hidden lg:block lg:row-span-6 bg-brown2 grid p-3 md:space-x-10 lg:-space-x-1 justify-center">
            <UtilBar :details="details" :questions="questions" />
        </div>
        
        <div id="main" class="block bg-brown3 lg:col-span-5 lg:row-span-6 space-y-10 border-y">
            <Main :questions="questions" />
        </div>
        
    </main>
</template>

<script>
import Header from './Header.vue'
import UtilBar from './UtilBar.vue'
import Main from './Main.vue'

export default {
    name: 'App',

    components: {
        Header,
        UtilBar,
        Main,
    },
    
    data() {
        return {
            details: {},
            questions: [],
        }
    },

    methods: {
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

        getData() {
            const data = {
                name: 'Ayandele Demilade',
                title: 'GET 101',
                duration: '1 hr',
                start_time: '12:30 PM',
                student_id: 'MATRIC NO?',
                questions: [
                    {
                        id: 1,
                        question: 'A Container used in carrying farm product is ___',
                        options: ['Cutlass', 'basket', 'hoe'],
                    },
                    {
                        id: 2,
                        question: 'A Container used in carrying farm product is ___',
                        options: ['Cutlass', 'basket', 'is any instrument held in the hand and used for work on the Farm is any instrument held in the hand and used for work on the Farm '],
                    },
                    {
                        id: 3,
                        question: 'Weeds are ___',
                        options: ['planted plants', 'timber tree', 'unwanted plants'],
                    },
                    {
                        id: 4,
                        question: '___ is not a vegetable',
                        options: ['Onion', 'Carrot', 'Mango'],
                    },
                    {
                        id: 5,
                        question: '___ is the surface of the earth on which plants grow and animals live',
                        options: ['Land', 'Labour', 'Management'],
                    }
                ]
            };
            return data;
        },

        changeAnswer(ans) {
            this.isActive = ans;
        },
    },

    created() {
        this.questions = this.doOptions(this.shuffuleQuest(this.getData().questions)),

        this.details = {
            title: this.getData().title,
            student_id: this.getData().student_id,
            student_name: this.getData().name,
            duration: this.getData().duration,
        }
    },
}
</script>