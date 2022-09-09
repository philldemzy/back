<template>
    <div class="cursor-pointer" id="open">
        <div class="flex rounded-msm lg:rounded-md float-right uppercase tracking-wider font-semibold text-xs mt-2 text-dark1 border-2 border-dark1 text-center sm:text-sm transform transition">
            <h2 @click="testLink" class="p-1 lg:p-2 hover:bg-brown2 hover:shadow-2xl">Take Test</h2>
            <div class="border-r-2 border-dark1"></div>
            <h2 @click="checkTest" class="p-1 lg:p-2 hover:bg-brown2 hover:shadow-2xl">Check Test</h2>
        </div>
    </div>
</template>

<script>
export default {
    name: 'TakeTest',

    methods: {
        testLink() {
            document.getElementById("takeTest").style.display = 'block';
            document.getElementById("takeTest").style.visibility = 'visible';
            let a = document.getElementById("takeTest").className;
            document.getElementById("takeTest").className = `${a} ease-in duration-300`;
        },

        checkTest() {
            document.getElementById("checkTest").style.display = 'block';
            document.getElementById("checkTest").style.visibility = 'visible';
            let a = document.getElementById("checkTest").className;
            document.getElementById("checkTest").className = `${a} ease-in duration-300`;
        }
    },
}
</script>
