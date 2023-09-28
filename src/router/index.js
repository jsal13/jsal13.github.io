import { createRouter, createWebHashHistory } from 'vue-router'
import HomePageView from '/src/views/HomePageView.vue'

import FlagsView from '/src/views/FlagsView.vue'
import SceneStarterView from '/src/views/SceneStarterView.vue'
import FacialExpressionsView from '/src/views/FacialExpressionsView.vue'
import BassPracticeView from '/src/views/BassPracticeView.vue'
import VocalPracticeView from '/src/views/VocalPracticeView.vue'

const router = createRouter({
  history: createWebHashHistory(),
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
    },
    {
      path: '/bass-practice',
      name: 'basspractice',
      component: BassPracticeView
    },
        {
      path: '/vocal-practice',
      name: 'vocalpractice',
      component: VocalPracticeView
    }
  ]
})

export default router
