<template>
    <div class="post">
        <div class="post-details">
            <div class="post-header">
                <div class="post-title">{{post.postTitle}}</div>
                <div class="post-actions">
                    <div class="post-button"
                        @click="$emit('requestModal', 'create', {'type': 'comment', 'id': post.postID})">
                        Reageer
                    </div>
                    <div class="post-button edit-button" v-if="isAdmin || isOwner" 
                        @click="$emit('requestModal', 'edit', {'type': 'post', 'id': post.postID, 'text': post.postContent})">
                        Bewerken
                    </div>
                    <div class="post-button delete-button" v-if="isAdmin || isOwner" @click="$emit('requestModal', 'delete', {'type': 'post', 'id': post.id})">Verwijderen</div>
                </div>
            </div>
            <div class="post-description">{{post.postContent}}</div>
            <div class="post-stats">{{post.postUser}} | Geplaatst op {{post.postCreated}} | {{comments.length}} reacties <span v-if="post.postEdited"> | Laatst bewerkt op {{post.edited}}</span></div>
        </div>
        <div class="posts-view">
            <CommentTile v-for="comment in comments" :key="comment.id" v-bind:comment="comment" v-on:requestModal="commentModalRequest" />
        </div>
    </div>
</template>

<script>
import CommentTile from '../components/CommentTile.vue'
export default {
    name: 'Post',
    components: {
        CommentTile
    },
    data() {
        return {
            //TODO: Read owner/admin status
            isOwner: true,
            isAdmin: false,
            post: {},
            comments: []
        }
    },
    methods: {
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
        console.log(this.post);
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
