<template>
    <div class="home">
        <Newsfeed v-if="loggedIn" />
        <Welcome v-else />
    </div>
</template>

<script>
import Welcome from '../components/Welcome.vue';
import Newsfeed from '../components/Newsfeed.vue';

export default {
    name: 'Home',
    components: {
        Welcome,
        Newsfeed
    },
    data() {
        return {
            loggedIn: false
        }
    },
    methods: {
        
    }
}
</script>

<style scoped>

</style>
