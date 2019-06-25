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
        getProjects(context){
            return new Promise((resolve, reject) => 
                Axios.get(`http://127.0.0.1:5000/project`)
                .then(response => resolve(response.data))
                .catch(error => reject(error))
            )
        },
        getProjectByID(context, projectID){
            return new Promise((resolve, reject) => 
                Axios.get(`http://127.0.0.1:5000/project/${projectID}`)
                .then(response => resolve(response.data))
                .catch(error => reject(error))
            )
        },
        getProjectPosts(context, projectID){
            return new Promise((resolve, reject) => 
                Axios.get(`http://127.0.0.1:5000/project/${projectID}/posts`)
                .then(response => resolve(response.data))
                .catch(error => reject(error))
            )
        },
        getPostByID(context, postID){
            return new Promise((resolve, reject) => 
                Axios.get(`http://127.0.0.1:5000/post/${postID}`)
                .then(response => resolve(response.data))
                .catch(error => reject(error))
            )
        },
        getPostComments(context, postID){
            return new Promise((resolve, reject) => 
                Axios.get(`http://127.0.0.1:5000/post/${postID}/comments`)
                .then(response => resolve(response.data))
                .catch(error => reject(error))
            )
        },
    }
})
