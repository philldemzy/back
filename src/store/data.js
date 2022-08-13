import { defineStore } from 'pinia'

export const useDataStore = defineStore({
    id: 'data',
    state: () => {
        return {
            details: {},
            questions: [],
            currQuestion: {},
            showMenu: true,
            currentPage: 0,
            pickedAns: [],
        }
    },

    actions: {
        addAnswer(answer) {
            this.pickedAns = this.pickedAns.filter((elemnt) => {
                return elemnt.id !== answer.id;
            });
            this.pickedAns.push(answer);
        },

        changeShowMenu() {
            this.showMenu = !this.showMenu;
        },

        changeQues(index) {
            this.currQuestion = this.questions[index];
        },

        goToPrev() {
            const index = this.questions.indexOf(this.currQuestion);
            if (index > 0) {
                this.currQuestion = this.questions[index - 1];
                this.currentPage--;
            }
        },

        goToNext() {
            const index = this.questions.indexOf(this.currQuestion);
            if (index < this.questions.length - 1) {
                this.currQuestion = this.questions[index + 1];
                this.currentPage++;
            }
        },

        setDetails(data) {
            this.details = {
                title: data.title,
                student_id: data.student_id,
                student_name: data.name,
                duration: data.duration,
            }
        },

        setQuestions(arr) {
            this.questions = arr
        },

        setCurrQuestion() {
            this.currQuestion = this.questions[0]
        },
    },

    getters: {
        isAnswered: (state) => {
            const answered = state.pickedAns.find((elemnt) => {
                return elemnt.id === state.currQuestion.id
            });
            
            if (answered) {
                return answered.answer;
            }
            return undefined;
        },

        isNext: (state) => {
            return state.questions.indexOf(state.currQuestion) < state.questions.length - 1
        },

        isPrev: (state) => {
            return state.questions.indexOf(state.currQuestion) > 0
        },

        currQuestNum: (state) => {
            return state.questions.indexOf(state.currQuestion) + 1
        },

        totalQuestNum: (state) => {
            return state.questions.length
        }
    }
})
