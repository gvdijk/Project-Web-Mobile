<template>
    <div class="home">
        <div class="projects-view">
            <ProjectTile v-for="project in paginatedProjects" :key="project.id" v-bind:project="project" />
        </div>
    <PageSelector v-bind:visiblePages="3" v-bind:totalEntries="projects.length" v-bind:entriesPerPage="5" v-on:pageChanged="pageChanged"/>
    </div>
</template>

<script>
import ProjectTile from '../components/ProjectTile.vue'
import PageSelector from '../components/PageSelector.vue'

export default {
    name: 'Explore',
    components: {
        ProjectTile,
        PageSelector,
    },
    data() {
        return {
            projects: [],
            startIndex: 0,
            endIndex: 0
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
        pageChanged(startIndex, endIndex){
            this.startIndex = startIndex;
            this.endIndex = endIndex;
        },
    },
    computed: {
        paginatedProjects(){
            return this.projects.slice(this.startIndex, this.endIndex);
        },
    },
    created(){
        this.fetchPosts();
    }
}
</script>

<style scoped>

</style>
