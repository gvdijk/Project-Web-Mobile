<template>
  <div id="app">
    <Header></Header>
    <Footer></Footer>
    <router-view/>
  </div>
</template>

<script>
import Header from './components/Header.vue';

export default {
  name: 'App',
  components: {
    Header,
  }
}
</script>


<style>
body{
  margin: 0;
}
</style>
