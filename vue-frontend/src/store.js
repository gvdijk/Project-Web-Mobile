import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import router from './router'

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
        getProjects(context, payload){
            let limit = payload.limit.toString();
            let offset = payload.offset.toString();
            let str = '?offset='+offset+'&limit='+limit
            if (payload.name) str += `&name=${payload.name}`
            return new Promise((resolve, reject) =>
                axios.get(`/project` + str)
                .then(response => resolve(response.data))
                .catch(error => reject(error))
            )
        },
        getProjectByID(context, projectID){
            axios.defaults.headers.common['Authorization'] = 'Bearer ' + context.state.JWT_Token;
            return new Promise((resolve, reject) => 
                axios.get(`/project/${projectID}`)
                .then(response => resolve(response.data))
                .catch(error => reject(error))
            )
        },
        getProjectPosts(context, payload){
            axios.defaults.headers.common['Authorization'] = 'Bearer ' + context.state.JWT_Token;
            let projectID = payload.projectID
            let limit = payload.limit.toString();
            let offset = payload.offset.toString();
            let str = '?offset='+offset+'&limit='+limit
            return new Promise((resolve, reject) => 
                axios.get(`/project/${projectID}/posts` + str)
                .then(response => resolve(response.data))
                .catch(error => reject(error))
            )
        },
        getPostByID(context, postID){
            axios.defaults.headers.common['Authorization'] = 'Bearer ' + context.state.JWT_Token;
            return new Promise((resolve, reject) => 
                axios.get(`/post/${postID}`)
                .then(response => resolve(response.data))
                .catch(error => reject(error))
            )
        },
        getPostComments(context, postID){
            axios.defaults.headers.common['Authorization'] = 'Bearer ' + context.state.JWT_Token;
            return new Promise((resolve, reject) => 
                axios.get(`/post/${postID}/comments`)
                .then(response => resolve(response.data))
                .catch(error => reject(error))
            )
        },
        getProjectUsers(context, projectID){
            axios.defaults.headers.common['Authorization'] = 'Bearer ' + context.state.JWT_Token;
            return new Promise((resolve, reject) => 
                axios.get(`/project/${projectID}/users`)
                .then(response => resolve(response.data))
                .catch(error => reject(error))
            )
        },
        getUser(context){
            axios.defaults.headers.common['Authorization'] = 'Bearer ' + context.state.JWT_Token;
            return new Promise((resolve, reject) => 
                axios.get(`/user/${context.state.userID}`)
                .then(response => resolve(response.data))
                .catch(error => {
                    context.dispatch('checkTokenExpiration', error.response);
                    reject(error);
                })
            )
        },
        getUserByName(context, name){
            axios.defaults.headers.common['Authorization'] = 'Bearer ' + context.state.JWT_Token;
            return new Promise((resolve, reject) => 
                axios.get(`/user?name=${name}`)
                .then(response => resolve(response.data))
                .catch(error => {
                    context.dispatch('checkTokenExpiration', error.response);
                    reject(error);
                })
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
                .catch(error => {
                    context.dispatch('checkTokenExpiration', error.response);
                    reject(error);
                })
            )
        },
        getUserPosts(context){
            axios.defaults.headers.common['Authorization'] = 'Bearer ' + context.state.JWT_Token;
            return new Promise((resolve, reject) => 
                axios.get(`/user/${context.state.userID}/posts`)
                .then(response => resolve(response.data))
                .catch(error => {
                    context.dispatch('checkTokenExpiration', error.response);
                    reject(error);
                })
            )
        },
        getUserComments(context){
            axios.defaults.headers.common['Authorization'] = 'Bearer ' + context.state.JWT_Token;
            return new Promise((resolve, reject) => 
                axios.get(`/user/${context.state.userID}/comments`)
                .then(response => resolve(response.data))
                .catch(error => {
                    context.dispatch('checkTokenExpiration', error.response);
                    reject(error);
                })
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
                .catch(error => {
                    context.dispatch('checkTokenExpiration', error.response);
                    reject(error);
                })
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
                .catch(error => {
                    context.dispatch('checkTokenExpiration', error.response);
                    reject(error);
                })
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
                .catch(error => {
                    context.dispatch('checkTokenExpiration', error.response);
                    reject(error);
                })
            )
        },
        createProjectUser(context, project) {
            axios.defaults.headers.common['Authorization'] = 'Bearer ' + context.state.JWT_Token;
            return new Promise((resolve, reject) => 
                axios.post(`/project/${project.projectID}/users`, {
                    user: project.userID ? project.userID : context.state.userID,
                    role: project.role,
                })
                .then(response => resolve(response))
                .catch(error => {
                    context.dispatch('checkTokenExpiration', error);
                    reject(error);
                })
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
                .catch(error => {
                    context.dispatch('checkTokenExpiration', error.response);
                    reject(error);
                })
            )
        },
        updatePost(context, post) {
            axios.defaults.headers.common['Authorization'] = 'Bearer ' + context.state.JWT_Token;
            return new Promise((resolve, reject) => 
                axios.put(`/post/${post.id}`, {
                    content: post.text
                })
                .then(response => resolve(response.data))
                .catch(error => {
                    context.dispatch('checkTokenExpiration', error.response);
                    reject(error);
                })
            )
        },
        updateComment(context, comment) {
            axios.defaults.headers.common['Authorization'] = 'Bearer ' + context.state.JWT_Token;
            return new Promise((resolve, reject) => 
                axios.put(`/comment/${comment.id}`, {
                    content: comment.text
                })
                .then(response => resolve(response.data))
                .catch(error => {
                    context.dispatch('checkTokenExpiration', error.response);
                    reject(error);
                })
            )
        },
        updateProjectUser(context, projectUser) {
            axios.defaults.headers.common['Authorization'] = 'Bearer ' + context.state.JWT_Token;
            return new Promise((resolve, reject) => 
                axios.put(`/project/${projectUser.projectID}/users`, {
                    user: projectUser.userID ? projectUser.userID : context.state.userID,
                    role: projectUser.role
                })
                .then(response => resolve(response.data))
                .catch(error => {
                    context.dispatch('checkTokenExpiration', error.response);
                    reject(error);
                })
            )
        },

        
        deleteProject(context, projectID) {
            axios.defaults.headers.common['Authorization'] = 'Bearer ' + context.state.JWT_Token;
            return new Promise((resolve, reject) => 
                axios.delete(`/project/${projectID}`)
                .then(response => resolve(response.data))
                .catch(error => {
                    context.dispatch('checkTokenExpiration', error.response);
                    reject(error);
                })
            )
        },
        deletePost(context, postID) {
            axios.defaults.headers.common['Authorization'] = 'Bearer ' + context.state.JWT_Token;
            return new Promise((resolve, reject) => 
                axios.delete(`/post/${postID}`)
                .then(response => resolve(response.data))
                .catch(error => {
                    context.dispatch('checkTokenExpiration', error.response);
                    reject(error);
                })
            )
        },
        deleteComment(context, commentID) {
            axios.defaults.headers.common['Authorization'] = 'Bearer ' + context.state.JWT_Token;
            return new Promise((resolve, reject) => 
                axios.delete(`/comment/${commentID}`)
                .then(response => resolve(response))
                .catch(error => {
                    context.dispatch('checkTokenExpiration', error.response);
                    reject(error);
                })
            )
        },
        deleteProjectUser(context, projectUser) {
            axios.defaults.headers.common['Authorization'] = 'Bearer ' + context.state.JWT_Token;
            return new Promise((resolve, reject) => 
                axios.delete(`/project/${projectUser.projectID}/users`, {
                    data: {
                        user: projectUser.userID ? projectUser.userID : context.state.userID
                    }
                })
                .then(response => resolve(response.data))
                .catch(error => {
                    console.log(error);
                    context.dispatch('checkTokenExpiration', error.response);
                    reject(error);
                })
            )
        },



        registerUser(context, payload){
            return new Promise((resolve, reject) => {
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



        checkTokenExpiration(context, response){
            if(response.status === 401){
                if(response.data.msg === "Token has expired"){
                    context.dispatch('logoutUser');
                    console.log("User has been logged out because login token expired")
                    router.push({path: '/'});
                }
            }
        }
    }
})
