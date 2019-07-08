<template>
    <div class="project">
        <div class="project-details">
            <div class="project-header">
                <div class="project-title">{{project.projectName}}</div>
                <div class="project-actions">
                    <div class="project-button" @click="$emit('requestModal', 'create', {'type': 'post', 'id': project.projectID ? project.projectID : $route.params.id})">Nieuw bericht</div>
                    <router-link 
                        class="project-button settings-button" 
                        v-if="isAdmin"
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
        <PageSelector v-bind:visiblePages="3" v-bind:totalEntries="count" v-bind:entriesPerPage="limit" v-on:pageChanged="pageChanged"/>
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
            isAdmin: false,
            project: {},
            posts: [],
            offset: 0,
            limit: 5,
            count: 0,
            userprojects: []
        }
    },
    methods: {
        fetchProject(){
            this.$store.dispatch('getProjectByID', this.$route.params.id)
            .then( response => this.project = response)
            .catch( error => console.log(error))
        },
        fetchPosts(limit, offset){
            this.$store.dispatch('getProjectPosts', {projectID: this.$route.params.id, limit: limit, offset: offset})
            .then( response => {
                this.posts = response.data;
                this.count = response.count;
            })
            .catch( error => console.log(error))
        },
        pageChanged(offset){
            this.offset = offset;
            this.fetchPosts(this.limit, this.offset);
            this.$store.dispatch('getUserProjects')
                .then(response => this.userprojects = response)
                .catch(error => console.log(error.response));
        },
        // projectRelation() {
        //     let index = this.userprojects.findIndex((el) => el.Project_projectID == this.project.projectID);
        //     let role = this.userprojects[index].projectuserRole; 
        //     (role == "OWNER" || role == "ADMIN") ? this.isAdmin = true : this.isAdmin = false;
        // }
    },
    created(){
        this.fetchProject();
        this.fetchPosts(this.limit, this.offset);
        this.$store.dispatch('getUserProjects')
            .then(response => this.userprojects = response)
            .catch(error => console.log(error.response));
    },
    watch: {
        userprojects: function() {
            let index = this.userprojects.findIndex((el) => el.Project_projectID == this.project.projectID);
            if (index > -1) {
                let role = this.userprojects[index].projectuserRole; 
                (role == "ADMIN" || role == "OWNER") ? this.isAdmin = true : this.isAdmin = false;
            } else {
                //FIXME: User should not be here
            }
        }
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
