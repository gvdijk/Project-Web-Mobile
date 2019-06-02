<template>
  <div id="app">
    <Header></Header>
    <router-view/>
    <Footer></Footer>
  </div>
</template>

<script>
import Header from './components/Header.vue';
import Footer from './components/Footer.vue';

export default {
  name: 'App',
  components: {
    Header,
    Footer
  }
}
</script>


<style>
:root {
    --violet:       #7b69cc;
    --blue:         #25a9df;
    --teal:         #50ccbc;
    --green:        #3dbd67;
    --yellow:       #ffc540;
    --orange:       #fc873b;
    --pink:         #e74668;
    --red:          #e84f56;
    
    --dark-violet:  #5f50a4;
    --dark-blue:    #2085bb;
    --dark-teal:    #22b59f;
    --dark-green:   #1e9b5d;
    --dark-yellow:  #ffb600;
    --dark-orange:  #f15d1c;
    --dark-pink:    #cc2d61;
    --dark-red:     #c12c42;

    --white-pure:   #ffffff;
    --white-base:   #f5f7f9;
    --white-soft:   #ebedf0;

    --gray-bright:  #bdc5c9;
    --gray-soft:    #929ba0;
    --gray-base:    #6f797d;
    --gray-dark:    #5f686c;
    --gray-darker:  #4d555b;
    
    --black-smooth: #2d3438;
    --black-soft:   #1b1f22;
    --black-mid:    #121516;
    --black-deep:   #090a0b;


    --max-width: 1100px;
    --header-height: 50px;
    --footer-height: 150px;
}

* {
    padding: 0;
    margin: 0;
}

body {
    position: relative;
    display: block;
    padding-top: 50px;
    padding-bottom: 150px;
    min-height: 100vh;
    background-color: var(--white-base);
    box-sizing: border-box;
}

#app {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    padding-top: 50px;
}
</style>
