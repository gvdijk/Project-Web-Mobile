import Vue from 'vue'
import Vuex from 'vuex'
import Axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    
    },
  getters: {
    
    },
  mutations: {

    },
  actions: {
    getPosts(context){
        return new Promise((resolve, reject) => {
            Axios.get('https://jsonplaceholder.typicode.com/posts')
            .then( response => {
                resolve(response.data);
            })
            .catch ( error => {
                reject(error);
            })
        })
    },
    }
})
