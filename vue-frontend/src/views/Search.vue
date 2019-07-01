<template>
    <div class="home">
        <h1>Zoekresultaten</h1>
        <h3>Zoekresultaten voor {{searchQuery}}</h3>
        <div class="projects-view">
            <ProjectTile v-for="project in projects" 
                :key="project.id" 
                v-bind:project="project" 
                v-bind:userprojects="userprojects" 
                ref="projectTile"
                v-on:requestModal="searchModalRequest" 
            />
        </div>
        <PageSelector v-bind:visiblePages="3" v-bind:totalEntries="count" v-bind:entriesPerPage="limit" v-on:pageChanged="pageChanged"/>
    </div>
</template>

<script>
import ProjectTile from '../components/ProjectTile.vue'
import PageSelector from '../components/PageSelector.vue'

export default {
    name: 'Search',
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
            userprojects: []
        }
    },
    methods: {
        searchModalRequest(type, body) { this.$emit('requestModal', type, body); },
        fetchProjects(offset, limit){
            this.$store.dispatch('getProjects', {
                name: this.$route.query.q,
                offset: offset, 
                limit: limit
            })
            .then( response => {
                this.projects = response.data;
                this.count = response.count;
            })
            .catch( error => console.log(error))
        },
        pageChanged(offset){
            this.offset = offset;
            this.fetchProjects(this.offset, this.limit);
        }
    },
    created(){
        this.fetchProjects(this.offset, this.limit);
        this.$store.dispatch('getUserProjects')
            .then(response => {this.userprojects = response; console.log(response)})
            .catch(error => console.log(error.response))
    },
    computed: {
        searchQuery: function() { return `"${this.$route.query.q}"` }
    },
    watch: {
        searchQuery: function() {
            this.projects = [];
            this.fetchProjects(this.offset, this.limit);
        }
    }
}
</script>

<style scoped>
    h1{
        color: var(--dark-green);
    }

    h3{
        color: var(--dark-green);
    }
</style>
