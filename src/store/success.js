import { defineStore } from 'pinia'

export const useSuccessStore = defineStore({
    id: 'success',
    state: () => {
        return {
            success: 0,
            status_: null,
            retries: 0,
        }
    },

    actions: {
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
