<template>
    <div class="comment-tile">
        <div class="comment-details">
            <span class="comment-subtitle">
                {{ comment.commentUser }} | Geplaatst op {{ comment.commentCreated }}
                <span v-if="comment.commentEdited"> | Laatst bewerkt op {{ comment.commentEdited }}</span>
            </span>
            <div class="comment-button delete-button"
                v-if="isAdmin || isOwner" 
                 @click="$emit('requestModal', 'delete', {'type': 'comment', 'id': comment.commentID})">
                Verwijderen
            </div>
            <div class="comment-button edit-button"
                v-if="isAdmin || isOwner"
                @click="$emit('requestModal', 'edit', {'type': 'comment', 'id': comment.commentID, 'text': comment.commentContent})">
                Bewerken
            </div>
            <div class="comment-button"
                 @click="$emit('requestModal', 'create', {'type': 'child', 'postID': comment.commentPost, 'commentID': comment.commentID})">
                Reageer
            </div>
        </div>
        <span class="comment-content">{{ comment.commentContent }}</span>
        <CommentTile :key="child.id" v-for="child in children" v-bind:comment="child" v-on:requestModal="childCommentModalRequest" />
    </div>
</template>

<script>
export default {
    name: 'CommentTile',
    data() {
        return {
            //TODO: Read owner/admin status
            isOwner: true,
            isAdmin: false
        }
    },
    methods: {
        childCommentModalRequest(type, body) { this.$emit('requestModal', type, body); }
    },
    props: ['comment'],
    computed: {
        children: function () { 
            return this.comment.children 
        }
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
    font-size: 9pt;
    font-weight: 600;
    margin: 0 3px;
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
</style>
