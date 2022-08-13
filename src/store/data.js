import { defineStore } from 'pinia'

export const useDataStore = defineStore({
    id: 'data',
    state: () => {
        return {
            details: {},
            questions: [],
            currQuestion: {},
            showMenu: true,
            currentPage: 1,
            pickedAns: [],
        }
    },

    actions: {
        changeShowMenu() {
            this.showMenu = !this.showMenu;
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

        setQuestions(arr) {
            this.questions = arr
        },

        setCurrQuestion() {
            this.currQuestion = this.questions[0]
        },
    },

    getters: {
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
