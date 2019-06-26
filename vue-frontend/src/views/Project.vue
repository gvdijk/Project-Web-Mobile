<template>
    <div class="project">
        <div class="project-details">
            <div class="project-header">
                <div class="project-title">{{project.projectName}}</div>
                <div class="project-actions">
                    <div class="project-button" v-if="!userIsJoined && !project.access">Aanvragen</div>
                    <div class="project-button" v-if="!userIsJoined && project.access">Deelnemen</div>
                    <div class="project-button" v-if="userIsJoined" @click="$emit('requestModal', 'create', {'type': 'post', 'id': project.projectID})">Nieuw bericht</div>
                    <router-link 
                        class="project-button settings-button" 
                        v-if="userIsJoined && userIsAdmin"
                        :to="{ path:`/project/${this.project.projectID}/settings`}">
                        Instellingen
                    </router-link>
                </div>
            </div>
            <div class="project-description">{{project.projectDescription}}</div>
            <div class="project-stats">Er zijn {{posts.length}} berichten geplaatst door {{project.users}} gebruikers sinds {{project.projectCreated}}</div>
        </div>
        <div class="posts-view">
            <PostTile v-for="post in posts" :key="post.postID" v-bind:post="post" />
        </div>
        <PageSelector v-bind:visiblePages="3" v-bind:totalEntries="posts.length" v-bind:entriesPerPage="5" v-on:pageChanged="pageChanged"/>
    </div>
</template>

<script>
import PostTile from '../components/PostTile.vue'
import PageSelector from '../components/PageSelector.vue'

export default {
    name: 'Project',
    components: {
        PostTile,
        PageSelector,
    },
    data() {
        return {
            userIsJoined: true,
            userIsAdmin: true,
            project: {},
            posts: [],
            startIndex: 0,
            endIndex: 0
        }
    },
    methods: {
        fetchProject(){
            this.$store.dispatch('getProjectByID', this.$route.params.id)
            .then( response => this.project = response)
            .catch( error => console.log(error))
        },
        fetchPosts(){
            this.$store.dispatch('getProjectPosts', this.$route.params.id)
            .then( response => this.posts = response)
            .catch( error => console.log(error))
        },
        pageChanged(startIndex, endIndex){
            this.startIndex = startIndex;
            this.endIndex = endIndex;
        }
    },
    computed: {
        paginatedPosts(){
            return this.posts.slice(this.startIndex, this.endIndex);
        }
    },
    created(){
        this.fetchProject();
        this.fetchPosts();
    }
}
</script>

<style scoped>
.project-details {
    margin-bottom: 20px;
    border-bottom: 4px solid var(--green);
}

.project-title {
    display: inline-block;
    font-size: 24pt;
    color: var(--green);
    margin-bottom: 5px;
}

.project-actions {
    display: block;
    float: right;
}

.project-button {
    display: inline-block;
    padding: 4px 9px 6px;
    background-color: var(--dark-green);
    color: var(--white-soft);
    font-size: 10pt;
    border: 1px solid var(--gray-brighter);
    border-radius: 3px;
    margin: 10px 3px 5px;
    cursor: pointer;
    user-select: none;
    -moz-user-select: -moz-none;
    text-decoration: none;
}

.project-button:hover {
    background-color: var(--green);
}

.settings-button {
    background-color: var(--dark-blue);
}

.settings-button:hover {
    background-color: var(--blue);
}

.project-description {
    display: block;
    color: var(--black-soft);
    font-size: 13pt;
    margin-bottom: 10px;
}

.project-stats {
    display: block;
    color: var(--gray-dark);
    font-size: 11pt;
    margin-bottom: 10px;
    font-style: italic;
}

</style>
