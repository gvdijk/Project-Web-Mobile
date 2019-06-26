import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

axios.defaults.baseURL = 'http://localhost:5000/';

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        JWT_Token: localStorage.getItem("JWT_Token") || null,
        userID: localStorage.getItem("userID") || null,
        userProjects: {}
    },
    getters: {
        token(state){
            return state.JWT_Token;
        },
        userID(state){
            return state.userID;
        },
        authenticated(state){
            return state.JWT_Token !== null;
        },
        userProjects(state){
            return state.userProjects;
        }
    },
    mutations: {
        setToken(state, token){
            state.JWT_Token = token;
        },
        unsetToken(state){
            state.JWT_Token = null;
        },
        setUserID(state, id){
            state.userID = id;
        },
        unsetUserID(state){
            state.userID = null;
        },
        setUserProjects(state, projects){
            state.userProjects = projects;
        }
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
        getUserByID(context, userID){
            axios.defaults.headers.common['Authorization'] = 'Bearer ' + context.state.JWT_Token;
            console.log(userID);
            return new Promise((resolve, reject) => 
                axios.get(`/user/${userID}`)
                .then(response => resolve(response.data))
                .catch(error => reject(error))
            )
        },
        getUserProjects(context){
            axios.defaults.headers.common['Authorization'] = 'Bearer ' + context.state.JWT_Token;
            return new Promise((resolve, reject) => 
                axios.get(`/user/${context.state.userID}/projects`)
                .then(response => {
                    resolve(response.data);
                    context.commit('setUserProjects', response.data);
                })
                .catch(error => reject(error))
            )
        },
        getUserPosts(context){
            axios.defaults.headers.common['Authorization'] = 'Bearer ' + context.state.JWT_Token;
            return new Promise((resolve, reject) => 
                axios.get(`/user/${context.state.userID}/posts`)
                .then(response => resolve(response.data))
                .catch(error => reject(error))
            )
        },
        getUserComments(context){
            axios.defaults.headers.common['Authorization'] = 'Bearer ' + context.state.JWT_Token;
            return new Promise((resolve, reject) => 
                axios.get(`/user/${context.state.userID}/comments`)
                .then(response => resolve(response.data))
                .catch(error => reject(error))
            )
        },


        createProject(context, project) {
            axios.defaults.headers.common['Authorization'] = 'Bearer ' + context.state.JWT_Token;
            return new Promise((resolve, reject) => 
                axios.post(`/project`, {
                    name: project.name,
                    description: project.description,
                    visibility: project.visibility,
                    ownerID: context.state.userID
                })
                .then(response => resolve(response))
                .catch(error => reject(error))
            )
        },
        createPost(context, post) {
            axios.defaults.headers.common['Authorization'] = 'Bearer ' + context.state.JWT_Token;
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
            axios.defaults.headers.common['Authorization'] = 'Bearer ' + context.state.JWT_Token;
            return new Promise((resolve, reject) => 
                axios.post(`/post/${comment.postID}/comments`, {
                    content: comment.content,
                    parent: comment.parent,
                    userID: context.state.userID
                })
                .then(response => resolve(response))
                .catch(error => reject(error))
            )
        },



        updateProject(context, project) {
            axios.defaults.headers.common['Authorization'] = 'Bearer ' + context.state.JWT_Token;
            return new Promise((resolve, reject) => 
                axios.put(`/project/${project.projectID}`, {
                    title: project.name,
                    content: project.description,
                    visibility: project.visibility
                })
                .then(response => resolve(response.data))
                .catch(error => reject(error))
            )
        },
        updatePost(context, post) {
            axios.defaults.headers.common['Authorization'] = 'Bearer ' + context.state.JWT_Token;
            return new Promise((resolve, reject) => 
                axios.put(`/post/${post.id}`, {
                    content: post.text
                })
                .then(response => resolve(response.data))
                .catch(error => reject(error))
            )
        },
        updateComment(context, comment) {
            axios.defaults.headers.common['Authorization'] = 'Bearer ' + context.state.JWT_Token;
            return new Promise((resolve, reject) => 
                axios.put(`/comment/${comment.id}`, {
                    content: comment.text
                })
                .then(response => resolve(response.data))
                .catch(error => reject(error))
            )
        },

        
        deleteProject(context, projectID) {
            axios.defaults.headers.common['Authorization'] = 'Bearer ' + context.state.JWT_Token;
            return new Promise((resolve, reject) => 
                axios.delete(`/project/${projectID}`)
                .then(response => resolve(response.data))
                .catch(error => reject(error))
            )
        },
        deletePost(context, postID) {
            axios.defaults.headers.common['Authorization'] = 'Bearer ' + context.state.JWT_Token;
            return new Promise((resolve, reject) => 
                axios.delete(`/post/${postID}`)
                .then(response => resolve(response.data))
                .catch(error => reject(error))
            )
        },
        deleteComment(context, commentID) {
            axios.defaults.headers.common['Authorization'] = 'Bearer ' + context.state.JWT_Token;
            return new Promise((resolve, reject) => 
                axios.delete(`/comment/${commentID}`)
                .then(response => resolve(response.data))
                .catch(error => reject(error))
            )
        },



        registerUser(context, payload){
            return new Promise((resolve, reject) => {
                console.log(payload.user + "    " + payload.pass)
                axios.post('http://localhost:5000/user', {
                    name: payload.user,
                    password: payload.pass
                })
                .then(response => { resolve(response.data) })
                .catch (error => { reject(error.response.data.error) })
            })
        },
        loginUser(context, payload){
            return new Promise((resolve, reject) => {
              axios.post('http://localhost:5000/login', {
                name: payload.user,
                password: payload.pass,
              })
              .then(response => {
                let JWT_Token = response.data.jwt_token;
                let userID = response.data.id
                localStorage.setItem('JWT_Token', JWT_Token);
                localStorage.setItem('userID', userID);
                context.commit('setToken', JWT_Token);
                context.commit('setUserID', userID);
                resolve(response.data);
              })
              .catch(error => {
                reject(error.response.data.error);
              })
            })
          },
        logoutUser(context){
            context.commit('unsetToken');
            context.commit('unsetUserID');
            localStorage.removeItem("JWT_Token");
            localStorage.removeItem('userID');
        },

    }
})
