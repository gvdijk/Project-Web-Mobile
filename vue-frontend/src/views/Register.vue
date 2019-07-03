<template>
  <div class="register">
    <h1>Registreren</h1>

    <form action="#" @submit.prevent="register">
      <label for="username">Gebruikersnaam</label>
      <input type="text" name="username" id="username" placeholder="Gebruikersnaam" v-model="username"> 

      <label for="password">Wachtwoord</label>
      <input type="password" name="password" id="password" placeholder="Wachtwoord"  v-model="password">

      <label for="confirmpass">Bevestig wachtwoord</label>
      <input type="password" name="confirmpass" id="confirmpass" placeholder="Bevestig Wachtwoord"  v-model="confirmpass">

      <button type="submit">Registreren</button>
    </form>
    <transition name="fade">
      <span class="error" v-show="error">{{errorMsg}}</span>
    </transition>
  </div>
</template>

<script>
export default {
  name: 'Register',
  data() {
    return{
      error: false,
      errorMsg: "",
      username: "",
      password: "",
      confirmpass: ""
    }
  },
  methods: {
    register(){
        // Check to see if username meets the requirements
        if(this.checkUsername()){
            // Check to see if password meets the requirements
            if(this.checkPassword()){
                this.$store.dispatch('registerUser', {user: this.username, pass: this.password})
                .then( response => {
                    this.$store.dispatch('loginUser', {user: this.username, pass: this.password})
                    this.$router.push({path: '/explore'})
                })
                .catch( error => {
                  this.errorMsg = error.data;
                  this.showError();
                });
            }else{ this.showError() }
        }else{ this.showError() }
    },
    checkUsername(){
        if(this.username.length < 3){
            this.errorMsg = "Accountnaam moet minstens 3 karakters lang zijn";
            return false;
        }else if(this.username.length > 20){
            this.errorMsg = "Accountnaam mag niet meer dan 20 karakters lang zijn";
            return false;
        }else if(!this.username.match(new RegExp("^[ A-Za-z0-9_-]*$"))){
            this.errorMsg = "Er mogen geen speciale karakters in de accountnaam voorkomen";
            return false;
        }else return true;
    },
    checkPassword(){
        if(this.password.length < 6){
            this.errorMsg = "Wachtwoord moet minstens 6 karakters lang zijn";
            return false;
        }else if(!this.password.match(new RegExp("[a-z]"))){
            this.errorMsg = "Wachtwoord moet ten minste 1 kleine letter bevatten";
            return false;
        }else if(!this.password.match(new RegExp("[A-Z]"))){
            this.errorMsg = "Wachtwoord moet ten minste 1 grote letter bevatten";
            return false;
        }else if(!this.password.match(new RegExp("[0-9]"))){
            this.errorMsg = "Wachtwoord moet ten minste 1 cijfer letter bevatten";
            return false;
        }else if(this.password != this.confirmpass){
            this.errorMsg = "Wachtwoorden komen niet overeen";
            return false;
        }else return true;
    },
    showError(){
        this.error = true;
        setTimeout(() => {this.error = false}, 5000)
    },
  },
}
</script>

<style scoped>
.register {
  font-weight: bold;
  color: var(--gray-darker);
  margin-top: 100px;
  width: 500px;
  max-width: 100%;
  margin-left: auto;
  margin-right: auto;
  margin-bottom: 100px;
}

.error {
  color: rgb(197, 64, 64);
}

.fade-enter-active, .fade-leave-active {
  transition: opacity 1s;
}
.fade-enter, .fade-leave-to {
  opacity: 0;
}

h1 {
  color: var(--green);
  text-align: left;
}

label {
  display: block;
  float: left;
  padding-top: 10px;
}

input {
    color: var(--gray-darker);
    width: 100%;
    height: 40px;
    font-size: 16px;
    padding: 4px 8px;
    outline: 0;
    border-radius: 3px;
    border: 1px solid var(--gray-bright);
    box-sizing: border-box;
}

input:focus {
    border: 1px solid var(--green);
}

button {
  width: 100px;
  height: 40px;
  float: right;
  margin-top: 30px;
  margin-bottom: 30px;
  font-size: 15px;
  background: var(--dark-green);
  color: var(--white-pure);
  border-radius: 3px;
  border-style: none;
  cursor: pointer;
  transition-duration: .5s;
}

button:hover {
  background: var(--green);
}
</style>
