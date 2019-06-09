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
        getPosts(context, projectID){
            // JSON placeholder until our own API is implemented
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
        getProjects(){
            // JSON placeholder until our own API is implemented
            // Since JSON placeholder doesn't have projects, projects are simply posts as well for the time being
            return new Promise((resolve, reject) => {
                Axios.get('https://jsonplaceholder.typicode.com/posts')
                .then( response => {
                    resolve(response.data);
                })
                .catch ( error => {
                    reject(error);
                })
            })
        }
    }
})
