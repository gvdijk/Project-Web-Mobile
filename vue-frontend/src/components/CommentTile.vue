<template>
    <div class="comment-tile">
        <div class="comment-details">
            <span class="comment-subtitle">{{ comment.user.name }} | Geplaatst op {{ comment.created }}<span v-if="comment.edited"> | Laatst bewerkt op {{ comment.edited }}</span></span>
            <div v-if="isAdmin || isOwner" class="comment-button">Bewerken</div>
            <div v-if="isAdmin || isOwner" class="comment-button delete-button">Verwijderen</div>
        </div>
        <span class="comment-content">{{ comment.description }}</span>
        <CommentTile :key="child.id" v-for="child in children" v-bind:comment="child" />
    </div>
</template>

<script>
export default {
    name: 'CommentTile',
    data() {
        return {
            isOwner: false,
            isAdmin: false
        }
    },
    components: {
        
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
    padding: 1px 6px 3px;
    background-color: var(--dark-green);
    color: var(--white-soft);
    font-size: 10pt;
    border: 1px solid var(--gray-brighter);
    border-radius: 3px;
    margin: 0 3px;
    cursor: pointer;
    user-select: none;
    -moz-user-select: -moz-none;
}

.comment-button:hover {
    background-color: var(--green);
}

.delete-button {
    background-color: var(--dark-red);
}

.delete-button:hover {
    background-color: var(--red);
}
</style>
