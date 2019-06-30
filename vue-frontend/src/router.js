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
      meta: {
        title: "Register Page",
        requiresVisitor: true,
      },
      component: () => import(/* webpackChunkName: "about" */ './views/Register.vue')
    },
    {
      path: '/about',
      name: 'about',
      component: () => import(/* webpackChunkName: "about" */ './views/About.vue')
    },
    {
      path: '/project/:id',
      name: 'project',
      meta: {
        title: "Project",
        requiresAuthenticated: true,
      },
      component: () => import(/* webpackChunkName: "about" */ './views/Project.vue')
    },
    {
      path: '/project/:projectid/post/:id',
      name: 'post',
      meta: {
        title: "Bericht",
        requiresAuthenticated: true,
      },
      component: () => import(/* webpackChunkName: "about" */ './views/Post.vue')
    },
    {
      path: '/explore',
      name: 'explore',
      component: () => import(/* webpackChunkName: "about" */ './views/Explore.vue')
    },
    {
      path: '/project/:id/settings',
      name: 'projectsettings',
      meta: {
        title: "Project instellingen",
        requiresAuthenticated: true,
      },
      component: () => import(/* webpackChunkName: "about" */ './views/ProjectSettings.vue')
    },
    {
      path: '/new',
      name: 'newproject',
      meta: {
        title: "Project aanmaken",
        requiresAuthenticated: true,
      },
      component: () => import(/* webpackChunkName: "about" */ './views/NewProject.vue')
    },
    {
      path: '/profile',
      name: 'usersettings',
      meta: {
        title: "Profiel instellingen",
        requiresAuthenticated: true,
      },
      component: () => import(/* webpackChunkName: "about" */ './views/UserSettings.vue')
    }
  ]
})
