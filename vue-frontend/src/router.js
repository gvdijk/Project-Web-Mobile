import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/register',
      name: 'register',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "about" */ './views/Register.vue')
    },
    {
      path: '/about',
      name: 'about',
      component: () => import(/* webpackChunkName: "about" */ './views/About.vue')
    },
    {
      path: '/project',
      name: 'project',
      component: () => import(/* webpackChunkName: "about" */ './views/Project.vue')
    },
    {
      path: '/post',
      name: 'post',
      component: () => import(/* webpackChunkName: "about" */ './views/Post.vue')
    },
    {
      path: '/explore',
      name: 'explore',
      component: () => import(/* webpackChunkName: "about" */ './views/Explore.vue')
    },
    {
      path: '/projectsettings',
      name: 'projectsettings',
      component: () => import(/* webpackChunkName: "about" */ './views/ProjectSettings.vue')
    },
    {
      path: '/usersettings',
      name: 'usersettings',
      component: () => import(/* webpackChunkName: "about" */ './views/UserSettings.vue')
    }
  ]
})
