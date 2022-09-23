import {createRouter, createWebHistory} from 'vue-router'

import Exam from '../views/Exam.vue'
import Submited from '../views/Submited'
import Index from '../views/Index.vue'
import Expln from '../views/Expln.vue'
import NewTest from '../views/NewTest.vue'
import TakeTest from '../views/TakeTest.vue'
import Examiner from '../views/Examiner.vue'
import NewTestStat from '../views/NewTestStat.vue'
import PrevEditExam from '../views/PrevEditExam.vue'

const routes = [
    {
        path: '/',
        name: Index,
        component: Index
    },
    {
        path: '/exam/:link',
        name: Exam,
        component: Exam
    },
    {
        path: '/check/:link',
        name: Examiner,
        component: Examiner
    },
    {
        path: '/submited',
        name: Submited,
        component: Submited
    },
    {
        path: '/new/test',
        name: NewTestStat,
        component: NewTestStat
    },
    {
        path: '/expln',
        name: Expln,
        component: Expln
    },
    {
        path: '/take_test/:link',
        name: TakeTest,
        component: TakeTest
    },
    {
        path: '/set_test',
        name: NewTest,
        component: NewTest
    },
    {
        path: '/preview/:link',
        name: PrevEditExam,
        component: PrevEditExam
    },
]

export const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes,
})
