<template>
    <div id="app">
        <Modal
            v-if="modalActive"
            v-bind:modaltype="modalType"
            v-bind:modaldata="modalData"
            v-on:closeModal="onModalClose" 
        />
        <Sidebar v-on:set-extended="onExtentionChange" v-bind:extended="sidebarExtended" />
        <Header v-on:requestModal="openModal" />
        <div class="all-content">
            <router-view v-on:requestModal="openModal" />
        </div>
        <Footer />
    </div>
</template>

<script>
import Header from './components/Header.vue';
import Footer from './components/Footer.vue';
import Sidebar from './components/Sidebar.vue';
import Modal from './components/modal/Modal.vue';

export default {
    name: 'App',
    components: {
        Header,
        Footer,
        Sidebar,
        Modal
    },
    data() {
        return {
            sidebarExtended: false,
            modalType: null,
            modalData: {},
            modalActive: false
        }
    },
    methods: {
        onExtentionChange(state) { this.sidebarExtended = state; },
        onModalClose() { this.modalActive = false; },
        openModal(type, data) {
            this.modalType = type;
            this.modalData = data;
            this.modalActive = true;
        }
    },
    mounted() {
        setTimeout(() => this.sidebarExtended = false, 1000);
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
    --footer-height: 180px;
    --side-full-width: 200px;

    --font-fam: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

* {
    padding: 0;
    margin: 0;
}

body {
    position: relative;
    display: block;
    padding-top: var(--header-height);
    padding-bottom: var(--footer-height);
    min-height: 100vh;
    background-color: var(--white-base);
    box-sizing: border-box;
    overflow-x: hidden;
}

#app {
    font-family: var(--font-fam);
}

.all-content {
    position: relative;
    width: var(--max-width);
    max-width: 100%;
    left: 50%;
    transform: translateX(-50%);
    padding: 30px 20px;
    box-sizing: border-box;
}


h1 {
    font-size: 24pt;
    color: var(--green);
    font-weight: 600;
}

h2 {
    font-size: 20pt;
    color: var(--green);
    font-weight: 500;
}

h3 {
    font-size: 16pt;
    color: var(--green);
    font-weight: 400;
}


</style>
