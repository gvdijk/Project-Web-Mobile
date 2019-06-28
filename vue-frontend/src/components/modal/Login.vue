<template>
    <div class="modal-content">
        <div class="modal-header">Inloggen</div>
        <div class="modal-text">
            <label>Gebruikersnaam</label>
            <input type="text" v-model="username" placeholder="Gebruikersnaam">
            <label>Wachtwoord</label>
            <input type="password" v-model="password" placeholder="Wachtwoord">
        </div>
        <div class="modal-actions">
            <div class="modal-button" @click="loginAction">Inloggen</div>
            <transition name="fade">
                <span class="error" v-show="error">{{ errorMsg }}</span>
            </transition>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Login',
    data() {
        return {
            username: "",
            password: "",
            error: false,
            errorMsg: "",
        }
    },
    methods: {
        loginAction() {
            console.log(`Login attempt with \r\n username: ${this.username} \r\n password: ${this.password}`);
            // Send login attempt to the api server
            this.$store.dispatch('loginUser', {user: this.username, pass: this.password})
            // Login succesfull
            .then( response => {
                this.$emit('closeModal');
                this.$router.push({path: '/explore'});
            })
            // Something wrong with the login
            .catch( error => {
                this.errorMsg = error;
                this.showError();
            });
        },
        showError(){
            this.error = true;
            setTimeout(() => {this.error = false}, 5000);
        }
    }
}
</script>

<style scoped>
    .error{
        padding: 16px;
        color: red;
    }

    .fade-enter-active, .fade-leave-active {
        transition: opacity 1s;
    }
    .fade-enter, .fade-leave-to {
        opacity: 0;
    }
</style>
