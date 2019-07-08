<template>
    <div class="home">
        <h1>Explore</h1>
        <h3>Ontdek projecten om aan deel te nemen</h3>
        <div class="projects-view">
            <ProjectTile 
                v-for="project in projects" 
                :key="project.id" 
                v-bind:project="project" 
                v-bind:userprojects="userprojects" 
                ref="projectTile"
                v-on:requestModal="exploreModalRequest" 
            />
        </div>
        <PageSelector v-bind:visiblePages="3" v-bind:totalEntries="count" v-bind:entriesPerPage="limit" v-on:pageChanged="pageChanged"/>
    </div>
</template>

<script>
import ProjectTile from '../components/ProjectTile.vue'
import PageSelector from '../components/PageSelector.vue'
import { mapGetters } from 'vuex'

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
            userprojects: []
        }
    },
    methods: {
        exploreModalRequest(type, body) { this.$emit('requestModal', type, body); },
        fetchProjects(offset, limit){
            this.$store.dispatch('getProjects', {
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
            this.$store.dispatch('getUserProjects')
                .then(response => this.userprojects = response)
                .catch(error => console.log(error.response));
        }
    },
    created(){
        this.fetchProjects(this.offset, this.limit);
        this.$store.dispatch('getUserProjects')
            .then(response => this.userprojects = response)
            .catch(error => console.log(error.response));
    },
    computed: {
        ...mapGetters(["authenticated"])
    },
    watch: {
        authenticated: function() {
        this.$store.dispatch('getUserProjects')
            .then(response => this.userprojects = response)
            .catch(error => console.log(error.response));
        }
    }
}
</script>

<style scoped>
    h1{
        color: var(--green);
    }

    h3{
        color: var(--green);
    }
</style>
