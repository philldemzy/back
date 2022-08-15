import {createRouter, createWebHistory} from 'vue-router'

import Exam from '../views/Exam.vue'
import Submited from '../views/Submited'

const routes = [
    {
        path: '/',
        name: Exam,
        component: Exam
    },
    {
        path: '/submited',
        name: Submited,
        component: Submited
    }
]

export const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes,
})
