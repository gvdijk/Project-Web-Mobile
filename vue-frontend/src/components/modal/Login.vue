<template>
    <div class="modal-content">
        <form action="#" @submit.prevent="loginAction">
            <div class="modal-header">Inloggen</div>
            <div class="modal-text">
                <label>Gebruikersnaam</label>
                <input type="text" v-model="username" placeholder="Gebruikersnaam">
                <label>Wachtwoord</label>
                <input type="password" v-model="password" placeholder="Wachtwoord">
                <label>
                    Nog geen account? 
                    <span class="register-link" to="/register" @click="goToRegister">Registreer hier</span>
                </label>
            </div>
            <div class="modal-actions">
                <button class="modal-button" type="submit">Inloggen</button>
                <transition name="fade">
                    <span class="error" v-show="error">{{ errorMsg }}</span>
                </transition>
            </div>
        </form>
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
        goToRegister() {
            this.$emit('closeModal');
            this.$router.push({path: '/register'});
        },
        loginAction() {
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

    .register-link {
        color: var(--white-soft);
        cursor: pointer;
        text-decoration: underline;
    }

    .register-link:hover {
        color: var(--green);
    }

</style>
