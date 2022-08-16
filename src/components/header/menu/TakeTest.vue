<template>
    <div @click="testLink" class="cursor-pointer" id="open">
        <div class="rounded-lg lg:rounded-2xl float-right uppercase tracking-wider font-semibold text-sm m-1 text-dark1 border-2 border-dark1 text-center sm:text-base transform transition hover:bg-brown2 hover:shadow-2xl">
            <h2 class="p-2 lg:p-3">Take Test</h2>
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
    },
}
</script>
