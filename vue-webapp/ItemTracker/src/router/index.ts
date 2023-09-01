import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../pages/Home.vue'
import CharacterView from '../pages/Character.vue'
import LoginView from '../pages/Login.vue'
import AboutView from '../pages/About.vue'

import { useUserStore } from '../stores/user-session'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'About',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: AboutView
    },
    {
      path: '/dm-info',
      name: 'For DMs',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: HomeView
    },
    {
      path: '/login',
      name: 'login',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: LoginView
    },
    {
      path: '/character',
      name: 'Character',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: CharacterView
    }
  ]
})

router.beforeEach(async (to, from) => {
  const userSession = useUserStore();

  if (
    // make sure the user is authenticated
    !userSession.loggedIn &&
    // ❗️ Avoid an infinite redirect
    to.name !== 'login'
  ) {
    // redirect the user to the login page
    return { name: 'login' }
  }
})

export default router
