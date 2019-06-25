import Vue from 'vue'
import Vuex from 'vuex'
import Axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        JWT_Token: localStorage.getItem("JWT_Token") || null,
        userID: localStorage.getItem("userID") || null,
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
    },
    actions: {
        registerUser(context, payload){
            return new Promise((resolve, reject) => {
                console.log(payload.user + "    " + payload.pass)
                Axios.post('http://localhost:5000/user', {
                    name: payload.user,
                    password: payload.pass
                })
                .then( response => { resolve(response.data) })
                .catch ( error => { reject(error.response.data.error) })
            })
        },
        loginUser(context, payload){
            return new Promise((resolve, reject) => {
              Axios.post('http://localhost:5000/login', {
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
