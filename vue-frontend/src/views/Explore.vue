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
    name: 'Explore',
    components: {
        ProjectTile
    },
    data() {
        return {
            projects: [
                {
                    id: 1,
                    title: 'Invisiline',
                    description: 'I have taken out my invisiline, and this is the album',
                    users: 34,
                    access: true,
                    created: 1539550165
                },
                {
                    id: 2,
                    title: 'Barbarapapa',
                    description: 'Vrouger hadden we nog echte TV series',
                    users: 2,
                    access: true,
                    created: 1549558165
                },
                {
                    id: 3,
                    title: 'De beste titel voor een lange beschrijving',
                    description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
                    users: 1,
                    access: false,
                    created: 1449558165
                },
            ]
        }
    },
}
</script>

<style scoped>

</style>
