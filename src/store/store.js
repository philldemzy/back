import { defineStore } from 'pinia'

export const useGenStore = defineStore({
    id: 'success',
    state: () => {
        return {
            success: 0,
            status_: null,
            retries: 0,
            submitTaskId: null,
        }
    },

    actions: {
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
            return state.success  === 1 && state.status_ === 'DONE';
        },

        isUnsuccessful: (state) => {
            return state.success  === 0 && state.status_ === 'DONE';
        },

        notDone: (state) => {
            return state.success  === 0 && state.status_ === null;
        },
    }
})
