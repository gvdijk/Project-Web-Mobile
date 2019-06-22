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
        </div>
    </div>
</template>

<script>
export default {
    name: 'Login',
    data() {
        return {
            username: "",
            password: ""
        }
    },
    methods: {
        loginAction() {
            //TODO: Axios login action
             console.log(`Login attempt with \r\n username: ${this.username} \r\n password: ${this.password}`);
             if (/*login succesful */ false) {
                this.$emit('closeModal');
                //TODO: Update site content for user on login
             } else {
                 // Display login error
             }
        }
    }
}
</script>

<style scoped>

</style>
