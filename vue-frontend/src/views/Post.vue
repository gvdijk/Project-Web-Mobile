<template>
    <div class="post">
        <div class="post-details">
            <div class="post-header">
                <div class="post-title">{{post.postTitle}}</div>
                <div class="post-actions">
                    <div class="post-button"
                        @click="$emit('requestModal', 'create', {'type': 'comment', 'id': post.postID, 'cb': addComment})">
                        Reageer
                    </div>
                    <div class="post-button edit-button" v-if="isOwner" 
                        @click="$emit('requestModal', 'edit', {'type': 'post', 'id': post.postID, 'text': post.postContent})">
                        Bewerken
                    </div>
                    <div class="post-button delete-button" v-if="isAdmin || isOwner" @click="$emit('requestModal', 'delete', {'type': 'post', 'id': post.postID, 'projectID': post.postProject, 'cb': deletedPost})">Verwijderen</div>
                </div>
            </div>
            <div class="post-description">{{post.postContent}}</div>
            <div class="post-stats">{{post.user.userName}} | {{comments.length}} reacties | Geplaatst op {{post.postCreated}} <span v-if="post.postEdited"> | Laatst bewerkt op {{post.postEdited}}</span></div>
        </div>
        <div class="posts-view">
            <CommentTile v-for="comment in comments" :key="comment.id" v-bind:comment="comment" v-bind:isAdmin="isAdmin" v-on:requestModal="commentModalRequest" />
        </div>
    </div>
</template>

<script>
import CommentTile from '../components/CommentTile.vue';
import { mapGetters } from 'vuex';

export default {
    name: 'Post',
    components: {
        CommentTile
    },
    data() {
        return {
            //TODO: Read admin status
            isAdmin: false,
            post: {
                user: {}
            },
            comments: [],
            userprojects: []
        }
    },
    methods: {
        addComment(response) {
            response.children = [];
            this.comments.push(response);
        },
        deletedPost(response) {
            this.$router.push({path: `/project/${this.post.postProject}`});
        },
        fetchPost(){
            this.$store.dispatch('getPostByID', this.$route.params.id)
            .then( response => this.post = response)
            .catch( error => console.log(error))
        },
        fetchComments(){
            this.$store.dispatch('getPostComments', this.$route.params.id)
            .then( response => this.comments = response)
            .catch( error => console.log(error))
        },
        commentModalRequest(type, body) { this.$emit('requestModal', type, body); }
    },
    created() {
        this.fetchPost();
        this.fetchComments();
        this.$store.dispatch('getUserProjects')
            .then(response => this.userprojects = response)
            .catch(error => console.log(error.response));
    },
    computed: {
        ...mapGetters(["userID"]),
        isOwner() { return this.userID == this.post.user.userID || null }
    },
    watch: {
        userprojects: function() {
            let index = this.userprojects.findIndex((el) => el.Project_projectID == this.post.postProject);
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
.post-details {
    margin-bottom: 20px;
    border-bottom: 4px solid var(--green);
}

.post-title {
    display: inline-block;
    font-size: 24pt;
    color: var(--green);
    margin-bottom: 5px;
}

.post-actions {
    display: block;
    float: right;
}

.post-button {
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
    transition-duration: 0.1s;
}

.post-button:hover {
    background-color: var(--green);
}

.post-description {
    display: block;
    color: var(--black-soft);
    font-size: 13pt;
    margin-bottom: 10px;
}

.post-stats {
    display: block;
    color: var(--gray-dark);
    font-size: 11pt;
    margin-bottom: 10px;
    font-style: italic;
}

.edit-button {
    background-color: var(--dark-blue);
}

.edit-button:hover {
    background-color: var(--blue);
}

.delete-button {
    background-color: var(--dark-red);
}

.delete-button:hover {
    background-color: var(--red);
}

</style>
