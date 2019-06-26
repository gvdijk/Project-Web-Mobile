import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

axios.defaults.baseURL = 'http://localhost:5000/';

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        userID: 1
    },
    getters: {

    },
    mutations: {

    },
    actions: {
        getProjects(context){
            return new Promise((resolve, reject) => 
                axios.get(`/project`)
                .then(response => resolve(response.data))
                .catch(error => reject(error))
            )
        },
        getProjectByID(context, projectID){
            return new Promise((resolve, reject) => 
                axios.get(`/project/${projectID}`)
                .then(response => resolve(response.data))
                .catch(error => reject(error))
            )
        },
        getProjectPosts(context, projectID){
            return new Promise((resolve, reject) => 
                axios.get(`/project/${projectID}/posts`)
                .then(response => resolve(response.data))
                .catch(error => reject(error))
            )
        },
        getPostByID(context, postID){
            return new Promise((resolve, reject) => 
                axios.get(`/post/${postID}`)
                .then(response => resolve(response.data))
                .catch(error => reject(error))
            )
        },
        getPostComments(context, postID){
            return new Promise((resolve, reject) => 
                axios.get(`/post/${postID}/comments`)
                .then(response => resolve(response.data))
                .catch(error => reject(error))
            )
        },
        getProjectUsers(context, projectID){
            return new Promise((resolve, reject) => 
                axios.get(`/project/${projectID}/users`)
                .then(response => resolve(response.data))
                .catch(error => reject(error))
            )
        },



        createPost(context, post) {
            return new Promise((resolve, reject) => 
                axios.post(`/project/${post.projectID}/posts`, {
                    userID: context.state.userID,
                    title: post.title,
                    content: post.content  
                })
                .then(response => resolve(response))
                .catch(error => reject(error))
            )
        },
        createComment(context, comment) {
            return new Promise((resolve, reject) => 
                axios.post(`/post/${comment.postID}/comments`, {
                    content: comment.content,
                    parent: comment.postID,
                    userID: context.state.userID
                })
                .then(response => resolve(response))
                .catch(error => reject(error))
            )
        },

    }
})
