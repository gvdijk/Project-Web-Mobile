<template>
    <div class="project">
        <div class="project-details">
            <div class="project-header">
                <div class="project-title">{{project.title}}</div>
                <div class="project-actions">
                    <div class="project-button" v-if="!userIsJoined && !project.access">Aanvragen</div>
                    <div class="project-button" v-if="!userIsJoined && project.access">Deelnemen</div>
                    <div class="project-button" v-if="userIsJoined">Nieuw bericht</div>
                    <div class="project-button" v-if="userIsJoined && userIsAdmin">Instellingen</div>
                </div>
            </div>
            <div class="project-description">{{project.description}}</div>
            <div class="project-stats">Er zijn {{project.posts}} berichten geplaatst door {{project.users}} gebruikers sinds {{project.created}}</div>
        </div>
        <div class="posts-view">
            <PostTile v-for="post in posts" :key="post.id" v-bind:post="post" />
        </div>
        <PageSelector/>
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
            project: {
                id: 1,
                title: 'Invisiline',
                    description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
                users: 34,
                posts: 325,
                access: true,
                created: 1539550165
            },
            posts: [],
            perPage: 5,
        }
    },
    methods: {
        fetchPosts(){
            this.$store.dispatch('getPosts')
            .then( response => {
                this.posts = response;
            })
            .catch( error => {
                console.log(error);
            })
        }
    },
    computed: {
        numberOfPages(){

        },
        paginatedPosts(){

        }
    },
    created(){
        // this.fetchPosts();
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
}

.project-button:hover {
    background-color: var(--green);
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
