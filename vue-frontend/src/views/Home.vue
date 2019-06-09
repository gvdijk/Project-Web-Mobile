<template>
    <div class="home">
        <div class="projects-view">
            <ProjectTile v-for="project in projects" :key="project.id" v-bind:project="project" />
        </div>
    </div>
</template>

<script>
import ProjectTile from '../components/ProjectTile.vue'

export default {
    name: 'Home',
    components: {
        ProjectTile
    },
    data() {
        return {
            projects: [],
        }
    },
    methods: {
        fetchPosts(){
            this.$store.dispatch('getProjects')
            .then( response => {
                this.projects = response;
            })
            .catch( error => {
                console.log(error);
            })
        },
    },
    created(){
        this.fetchPosts();
    }
}
</script>

<style scoped>

</style>
