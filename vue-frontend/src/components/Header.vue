<template>
  <div class="header">
    <div class="logodiv">
      <img src="https://via.placeholder.com/70.png?text=logo" alt="logo">
    </div>
    <div class="searchdiv">
      <img src="https://www.pinclipart.com/picdir/middle/15-157737_lens-clipart-looking-glass-looking-glass-icon-png.png" alt="searchimage" class="searchimage">
      <input type="search" name="headerSearch" id="headerSearch" class="searchbar" v-model="searchQuery">
    </div>
    <div class="buttondiv">
      <button @click="login">Login</button>
      <button @click="register">Register</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Header',
  data() {
    return {
      searchQuery: "Search the website",
    }
  },
  methods: {
    login(){

    },
    register(){
      this.$router.push({path: '/register'});
    },
  },
}
</script>

<style scoped>
  .header{
    background-color: #eeeeee;
    padding: 20px;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
  }

  .searchbar{
    padding-left: 10px;
    height: 40px;
    width: 500px;
    border-radius: 3px;
    border: 0px;
  }

  .searchimage{
    height: 40px;
    border: 2px;
    border-radius: 3px;
  }

  .logodiv{
    width: 250px;
    margin-right: auto;
  }

  .searchdiv{
    display: flex;
  }

  .buttondiv{
    width: 250px;
    margin-left: auto;
    display: flex;
    justify-content: space-between;
    align-content: center;
  }

  button {
    width: 100px;
    height: 40px;
    font-size: 18px;
    font-weight: bold;
    background: #42b983;
    color: white;
    border-radius: 3px;
    cursor: pointer;
    transition-duration: .5s;
  }

  button:hover{
    background: #00d374;
  }
</style>
