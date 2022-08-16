<template>
    <div class="grid grid-cols-2 mx-6 md:mx-24 lg:mx-6">
        <div class="font-['Trebuchet MS']">
            <h2 class="p-2 lg:p-3 font-bold text-xl sm:text-2xl tracking-tight">
                <b class="text-brown4">C</b>
                <b class="text-red-400">B</b>
                Easy
            </h2>
        </div>
        <TakeTest/>
    </div>

    <TestLink/>

    <div class="bg-brown3 grid lg:grid-cols-2 2xl:grid-cols-5 lg:mb-3 justify-center">
        <div class="hidden relative lg:block 2xl:col-span-3">
            <img class="inset-0 w-full 2xl:w-5/6 lg:pt-12 lg:pl-8  xl:p-12 2xl:pr-0 object-cover object-center" src="@/assets/cbt.jpg" alt="Woman workcationing on the beach">
        </div>
        <div class="px-8 py-12 lg:py-5 max-w-md sm:max-w-xl lg:px-12 lg:py-24 lg:max-w-full lg:mt-16 xl:mt-24 2xl:ml-0 2xl:pl-0 2xl:mt-32 2xl:col-span-2">
            <div class="xl:max-w-xl">
                <img class="mt-6 rounded-lg shadow-xl sm:mt-8 sm:h-64 sm:w-full sm:object-cover object-center lg:hidden" src="@/assets/cbt.jpg" alt="cbt">
            </div>
            <h1 class="mt-6 text-2xl font-bold text-gray-900 sm:mt-8 sm:text-4xl lg:text-3xl xl:text-4xl">
                Making computer-based test simple to set up.
            </h1>
            <p class="mt-2 text-gray-800 sm:mt-4 sm:text-xl">
                Do you want to give your students an online test? To process the test without
                going to the hassle of building a platform from scratch for the test, follow this step.
                <br class="hidden lg:inline">
                <i>With simply a single".txt" file containing all the questions' information in a specified format,</i>
            </p>
            <div class="mt-4 sm:mt-6 float-right">
                <router-link  to="/expln" class="inline-block px-5 py-3 rounded-lg bg-brown4 uppercase tracking-wider font-semibold text-sm text-white shadow-lg sm:text-base transform transition hover:bg-brown3 hover:shadow-2xl hover:-translate-y-0.5">
                    Get started
                </router-link>
            </div>
        </div>
    </div>
</template>

<script>
import TestLink from '@/components/testforms/TestLink.vue';
import TakeTest from '@/components/header/menu/TakeTest.vue';
export default {
    name: "Index",
    components: {
        TestLink,
        TakeTest
    }
}
</script>
