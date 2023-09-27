import { createRouter, createWebHistory } from 'vue-router'
import HomePageView from '/src/views/HomePageView.vue'

import FlagsView from '/src/views/FlagsView.vue'
import SceneStarterView from '/src/views/SceneStarterView.vue'
import FacialExpressionsView from '/src/views/FacialExpressionsView.vue'


const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomePageView
    },
    {
      path: '/flags',
      name: 'flags',
      component: FlagsView
    },
    {
      path: '/scene-starter',
      name: 'scenestarter',
      component: SceneStarterView
    },
    {
      path: '/facial-expressions',
      name: 'facialexpression',
      component: FacialExpressionsView
    }
  ]
})

export default router
