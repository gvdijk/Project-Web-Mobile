<template>
  <div class="register">
    <h1>Registreren</h1>

    <form action="#" @submit.prevent="register">
      <label for="username">Gebruikersnaam</label>
      <input type="text" name="username" id="username" placeholder="Gebruikersnaam">

      <label for="username">Wachtwoord</label>
      <input type="password" name="password" id="password" placeholder="Wachtwoord">

      <label for="username">Bevestig wachtwoord</label>
      <input type="password" name="confirmpass" id="confirmpass" placeholder="Bevestig Wachtwoord">

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
      errorMsg: ""
    }
  },
  methods: {
    register(){
      //Returns a promise that either resolves or rejects based on form input
      this.checkInput()
      //Promise resolved: form input was valid
      .then(response => {
        console.log("Register OK")
        //TODO: send http request to API for new user
      })
      //Promise rejected: form input was invalid
      .catch(error => {
        this.showError(error);
      })
    },
    checkInput(){
      return new Promise((resolve, reject) => {
        if(this.username.length < 3 || this.username.length > 15){
          reject("Username must be between 3 and 15 characters");
        }
        else{
          resolve();
        }
      })
    },
    showError(errormsg){
      this.error = true;
      this.errorMsg = errormsg;
    },
  },
}
</script>

<style scoped>
.register {
  font-weight: bold;
  color: var(--gray-darker);
  margin-top: 100px;
  max-width: 500px;
  margin-left: auto;
  margin-right: auto;
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
  padding-bottom: 15px;
  padding-top: 15px;
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
  width: 100%;
  margin-top: 40px;
  margin-bottom: 40px;
  padding: 14px 12px;
  font-size: 18px;
  background: var(--dark-green);
  color: var(--white-pure);
  border-radius: 3px;
  cursor: pointer;
  transition-duration: .5s;
}

button:hover {
  background: var(--green);
}
</style>
