<template>

</template>

<script>
import { useGenStore } from '@/store/store'
export default{
    name: 'NewTestStat',

    setup() {
        const genStore = useGenStore();
        return {
            genStore
        };
    },

    mounted() {
        const checkStat = setInterval(this.checkStatus(this.genStore.newTestTaskId), 500)
        if (checkStat.state == 'SUCCESS') {
            clearInterval(checkStat)
        }

        
    },

    methods: {
        checkStatus(statusId) {
            const res = fetch(`http://localhost:8000/setup/${statusId}`)

            const data = res.json()
            return data;
        },
    },
}
</script>
