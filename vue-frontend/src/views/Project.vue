<template>
    <div class="project">
        <div class="posts-view">
            <PostTile v-for="post in posts" :key="post.id" v-bind:post="post" />
        </div>
    </div>
</template>

<script>
import PostTile from '../components/PostTile.vue'
export default {
    name: 'Project',
    components: {
        PostTile
    },
    data() {
        return {
            posts: [
                {
                    id: 1,
                    title: 'Post 1',
                    description: 'Ik wou dit even duidelijk maken',
                    user: 11,
                    created: 1539550165,
                    edited: 1539550265
                },
                {
                    id: 2,
                    title: 'Post 2',
                    description: '',
                    user: 12,
                    created: 1549558165,
                    edited: null
                },
                {
                    id: 3,
                    title: 'Post 3',
                    description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
                    user: 11,
                    created: 1449558165,
                    edited: null
                }
            ]
        }
    },
    methods: {
        
    }
}
</script>

<style>

</style>
