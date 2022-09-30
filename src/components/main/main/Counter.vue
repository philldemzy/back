<template>
    {{ timeLeft }}
</template>

<script>
import { useDataStore } from '@/store/data';

export default{
    name: 'Counter',

    data() {
        return {
            timeLeft: String,
        }
    },

    setup() {
        const dataStore = useDataStore();

        return {
            dataStore
        }
    },

    mounted() {
        this.countDown()
    },

    methods: {
        countDown() {
            //return seconds from api not milliseconds
            const duration = this.dataStore.details.duration;
            //returns date in isoformat
            const start = this.dataStore.details.start_time;
            const before = new Date(start)
            const seconds = duration * 1000
            const future = new Date(before.getTime() + seconds)

            update = setInterval( function() {
                const now = new Date();
                let diff = future.getTime() - now.getTime()
                if (diff <= 1) {
                    clearInterval(update);
                }
                let hours = Math.floor( (diff % (1000 * 3600 * 24)) / (1000 * 3600) );
                let minutes = Math.floor( (diff % (1000 * 3600)) / (1000 * 60) );
                let seconds = Math.floor( (diff % (1000 * 60)) / 1000 );

                //display all in only minutes and seconds no hours
                if (hours > 0) {
                    minutes += (hours * 60)
                }

                this.timeLeft = `${minutes} ${seconds}`
            }, 1000)
            return update;
        }
    },
}
</script>
