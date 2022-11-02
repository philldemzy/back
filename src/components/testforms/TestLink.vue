<template>
    <div id="takeTest" class="hidden absolute opacity-80 w-52 lg:w-60 h-44 bg-dark1 top-13 lg:top-[59.5px] right-8">
        <button class="float-right mr-2 mt-2 text-gray-200">
            <svg @click="closeTestLink" xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z" clip-rule="evenodd" />
            </svg>
        </button>
        <form class="ml-3.5 lg:ml-8 mt-12" id="takeTestForm" action="">
            <div>
                <label for="test_link" class="uppercase text-sm text-gray-200 lg:text-md">Enter test link:</label>
                <input type="text" class="pb-1 text-black text-center w-5/6" id="test_link" name="test_link">
                <input @click="goToTest" type="submit" class="ml-[136.5px] rounded-b-sm bg-brown1 mt-2 p-1 text-gray-900" value="Enter">
            </div>
        </form>
    </div>
</template>

<script>
import { useDataStore } from '../../store/data.js'
import { useGenStore } from '@/store/store.js'

export default {
    name: 'TestLink',

    setup() {
        const dataStore = useDataStore();
        const genStore = useGenStore();

        return {
            dataStore,
            genStore,
        }
    },

    methods: {
        closeTestLink() {
            document.getElementById("takeTest").style.visibility = 'hidden';
        },

        async goToTest(event) {
            event.preventDefault();
            const testLink = document.getElementById("test_link").value;
            if (testLink) {
                this.$router.push({path: `/take_test/${testLink}`},);
            }
            else {
                this.closeTestLink()
            }
        },
    },
}
</script>
