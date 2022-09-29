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
            let duration = this.dataStore.examDet.ended;
            let _end = new Date()
            let update;

            let end = new Date(_end.getTime() + parseInt(duration) * 1000);

            update = setInterval( function() {
                let now = new Date();
                if (_end.length >= 0) {
                    let diff = end.getTime() - now.getTime();
                    if (diff <= 1) {
                        clearInterval(update);
                    }
                    //let hours = Math.floor( (diff % (1000 * 3600 * 24)) / (1000 * 3600) );
                    let minutes = Math.floor( (diff % (1000 * 3600)) / (1000 * 60) );
                    let seconds = Math.floor( (diff % (1000 * 60)) / 1000 );

                    //document.getElementById("hours").children[0].innerHTML = hours;
                    //document.getElementById("minutes").children[0].innerHTML = minutes;
                    //document.getElementById("seconds").children[0].innerHTML = seconds;
                    this.timeLeft = `${minutes} ${seconds}`
                }
            }, 1000)
            return update;
        }
    },
}
</script>
