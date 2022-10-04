<template>
    <div class="flex space-x-2 mr-3 mx-auto items-center">
        <div class="grid grid-rows-2 content-center">
            <span class="font-thin text-center text-sm">MINS</span>
            <span class="font-semibold text-xs text-center" id="minutesLeft"></span>
        </div>
        <div class="grid grid-rows-2 content-center">
            <span class="font-thin text-center text-sm">SECS</span>
            <span class="font-semibold text-xs text-center" id="secondsLeft"></span>
        </div>
    </div>
</template>

<script>
import { useDataStore } from '@/store/data';

export default{
    name: 'Counter',

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

            let update;

            update = setInterval( function() {
                try {
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
                    document.getElementById('minutesLeft').innerHTML = minutes
                    document.getElementById('secondsLeft').innerHTML = seconds
                }
                catch (err) {}
            }, 1000)
            return update;
        }
    },
}
</script>
