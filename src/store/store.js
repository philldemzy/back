import { defineStore } from 'pinia'

export const useGenStore = defineStore({
    id: 'success',
    state: () => {
        return {
            success: false,
            status_: null,
            retries: 0,
            submitTaskId: null,
            newTest: {},
            token: sessionStorage.getItem('token') ? sessionStorage.getItem('token') : null,
        }
    },

    actions: {
        setToken(token) {
            this.token = token;
        },

        setNewTest(task) {
            this.newTest = task;
        },

        setSubmitTaskId(task_id) {
            this.submitTaskId = task_id;
        },

        isSuccess() {
            this.success = true;
            this.status_ = 'DONE';
        },

        isFailed() {
            this.status_ = 'DONE';
            this.retries++;
        },
    },

    getters: {
        isSuccessfull: (state) => {
            return state.success  === true && state.status_ === 'DONE';
        },

        isUnsuccessful: (state) => {
            return state.success  === false && state.status_ === 'DONE';
        },

        notDone: (state) => {
            return state.success  === false && state.status_ === null;
        },
    }
})
