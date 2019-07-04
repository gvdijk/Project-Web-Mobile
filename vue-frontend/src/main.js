import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import './registerServiceWorker'
// import './sw'

Vue.config.productionTip = false

//Route guards
router.beforeEach((to, from, next) => {
    // Guard routes that require you to not be logged in
    // (Register page)
    if (to.matched.some(record => record.meta.requiresVisitor)){
       if (store.getters.authenticated) {
            next({
                path: '/'
            }) // make sure to always call next()!
        } else{
            next()
        }
    // Guard routes that require you to be logged in
    // (Profile settings, project settings and making a new project)
    } else if(to.matched.some(record => record.meta.requiresAuthenticated)){
        if (!store.getters.authenticated) {
            next({
                path: '/'
            }) // make sure to always call next()!
        } else{
          next()
        }
    } else {
    next()
    }
})

new Vue({
  store,
  router,
  render: h => h(App)
}).$mount('#app')
