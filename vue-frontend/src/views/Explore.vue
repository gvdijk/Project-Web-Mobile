<template>
    <div class="home">
        <div class="projects-view">
            <ProjectTile v-for="project in projects" :key="project.id" v-bind:project="project" />
        </div>
        <PageSelector v-bind:visiblePages="3" v-bind:totalEntries="count" v-bind:entriesPerPage="limit" v-on:pageChanged="pageChanged"/>
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
            offset: 0,
            limit: 5,
            count: 0,
        }
    },
    methods: {
        fetchProjects(offset, limit){
            this.$store.dispatch('getProjects', {offset: offset, limit: limit})
            .then( response => {
                this.projects = response.data;
                this.count = response.count
            })
            .catch( error => console.log(error))
        },
        pageChanged(offset){
            this.offset = offset;
            this.fetchProjects(this.offset, this.limit);
        },
    },
    created(){
        this.fetchProjects(this.offset, this.limit);
    }
}
</script>

<style scoped>

</style>
