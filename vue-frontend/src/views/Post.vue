<template>
    <div class="post">
        <div class="post-details">
            <div class="post-header">
                <div class="post-title">{{post.title}}</div>
                <div class="post-actions">
                    <div class="post-button"
                        @click="$emit('requestModal', 'create', {'type': 'comment', 'id': post.id})">
                        Reageer
                    </div>
                    <div class="post-button edit-button" v-if="isAdmin || isOwner" 
                        @click="$emit('requestModal', 'edit', {'type': 'post', 'id': post.id, 'text': post.description})">
                        Bewerken
                    </div>
                    <div class="post-button delete-button" v-if="isAdmin || isOwner" @click="$emit('requestModal', 'delete', {'type': 'post', 'id': post.id})">Verwijderen</div>
                </div>
            </div>
            <div class="post-description">{{post.description}}</div>
            <div class="post-stats">Geplaatst op {{post.created}} | {{comments.length}} reacties <span v-if="post.edited"> | Laatst bewerkt op {{post.edited}}</span></div>
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
    methods: {
        commentModalRequest(type, body) { this.$emit('requestModal', type, body); }
    },
    data() {
        return {
            //TODO: Read owner/admin status
            isOwner: true,
            isAdmin: false,
            post: {
                id: 1,
                title: 'Post 1',
                description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
                user: {
                    id: 12,
                    name: "Henk de Tank"
                },
                created: 1539550165,
                edited: 1539550265
            },
            comments: [
                {
                    id: 1,
                    description: 'Ik wou dit ook even duidelijk maken in een comment',
                    user: {
                        id: 12,
                        name: "Henk de Tank"
                    },
                    created: 1539550165,
                    edited: 1539550265,
                    children: []
                },
                {
                    id: 2,
                    description: 'Yes',
                    user: {
                        id: 13,
                        name: "Trollmeister"
                    },
                    created: 1549556165,
                    edited: null,
                    children: [
                        {
                            id: 8,
                            description: 'r/InclusiveOr',
                            user: {
                                id: 14,
                                name: "AncientRedditor"
                            },
                            created: 1549557165,
                            edited: null,
                            children: [
                                {
                                    id: 12,
                                    description: 'Dit is Reddit toch niet man',
                                    user: {
                                        id: 13,
                                        name: "Trollmeister"
                                    },
                                    created: 1549558165,
                                    edited: null,
                                    children: []
                                }
                            ]
                        },
                        {
                            id: 11,
                            description: 'Thanks, I hate it',
                            user: {
                                id: 17,
                                name: "Bananenfierljepper"
                            },
                            created: 1549557765,
                            edited: null,
                            children: []
                        }
                    ]
                },
                {
                    id: 3,
                    title: 'Comment 3',
                    description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
                    user: {
                        id: 18,
                        name: "KaleKarel"
                    },
                    created: 1449558165,
                    edited: null,
                    children: []
                }
            ]
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
