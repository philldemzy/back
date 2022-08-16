import {createRouter, createWebHistory} from 'vue-router'

import Exam from '../views/Exam.vue'
import Submited from '../views/Submited'
import Index from '../views/Index.vue'
import Expln from '../views/Expln.vue'
import NewTest from '../views/NewTest.vue'

const routes = [
    {
        path: '/',
        name: Index,
        component: Index
    },
    {
        path: '/exam',
        name: Exam,
        component: Exam
    },
    {
        path: '/submited',
        name: Submited,
        component: Submited
    },
    {
        path: '/expln',
        name: Expln,
        component: Expln
    },
    {
        path: '/set_test',
        name: NewTest,
        component: NewTest
    },
]

export const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes,
})
