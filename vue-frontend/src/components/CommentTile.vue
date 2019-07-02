<template>
    <div class="comment-tile">
        <div class="comment-details">
            <span class="comment-subtitle">
                {{ comment.user.userName }} | Geplaatst op {{ comment.commentCreated }}
                <span v-if="comment.commentEdited"> | Laatst bewerkt op {{ comment.commentEdited }}</span>
            </span>
            <div class="comment-button delete-button" 
                title="Verwijderen" 
                v-if="isAdmin || isOwner" 
                @click="$emit('requestModal', 'delete', {'type': 'comment', 'id': comment.commentID, 'cb': deletedComment})">
                <i class="fa fa-trash"></i>
            </div>
            <div class="comment-button edit-button" 
                title="Bewerken" 
                v-if="isAdmin || isOwner"
                @click="$emit('requestModal', 'edit', {'type': 'comment', 'id': comment.commentID, 'text': comment.commentContent, 'cb': editedComment })">
                <i class="fa fa-edit"></i>
            </div>
            <div class="comment-button" 
                title="Reageren" 
                @click="$emit('requestModal', 'create', {'type': 'child', 'id': comment.commentPost, 'parent': comment.commentID, 'cb': createdChild })">
                <i class="fa fa-reply"></i>
            </div>
        </div>
        <span class="comment-content">{{ comment.commentContent }}</span>
        <CommentTile :key="child.id" v-for="child in children" v-bind:comment="child" v-on:requestModal="childCommentModalRequest" />
    </div>
</template>

<script>
import { mapGetters } from 'vuex';
export default {
    name: 'CommentTile',
    data() {
        return {
            //TODO: Read admin status
            isAdmin: false
        }
    },
    methods: {
        childCommentModalRequest(type, body) { this.$emit('requestModal', type, body); },
        createdChild(response) {
            response.children = [];
            this.comment.children.push(response);
        },
        editedComment(response) {
            this.comment.commentContent = response.commentContent;
        },
        deletedComment(response) {
            this.comment.commentContent = "Deze reactie is verwijderd";
        }
    },
    props: ['comment'],
    computed: {
        children: function () { 
            return this.comment.children 
        },
        ...mapGetters(["userID"]),
        isOwner() { return this.userID == this.comment.user.userID || null }
    }
}
</script>

<style scoped>
.comment-tile {
    width: 100%;
    padding: 2px 4px 2px 12px;
    border: 1px solid var(--gray-bright);
    border-radius: 6px;
    margin: 5px 0;
    box-sizing: border-box;
    overflow: hidden;
}

.comment-details {
    display: block;
    min-height: 20px;
}

.comment-subtitle {
    display: inline-block;
    font-size: 8pt;
    color: var(--black-smooth);
    font-style: italic;
}

.comment-content {
    display: block;
    font-size: 11pt;
    color: var(--black-smooth);
    overflow: hidden;
    margin: 3px 0 6px;
}

.comment-button {
    float: right;
    padding: 1px 3px 3px;
    color: var(--dark-green);
    font-size: 11pt;
    font-weight: 600;
    margin: 0 1px;
    cursor: pointer;
    user-select: none;
    -moz-user-select: -moz-none;
    transition-duration: 0.1s;
}

.comment-button:hover {
    color: var(--green);
}

.edit-button {
    color: var(--dark-blue);
}

.edit-button:hover {
    color: var(--blue);
}

.delete-button {
    color: var(--dark-red);
}

.delete-button:hover {
    color: var(--red);
}



i {
    color: var(--gray-dark);
    transition-duration: 0.1s;
    padding: 2px;
}

.fa-reply:hover {
    color: var(--green);
}

.fa-edit:hover {
    color: var(--blue);
}

.fa-trash:hover {
    color: var(--red);
}

.fa-minus:hover {
    color: var(--orange);
}

</style>
