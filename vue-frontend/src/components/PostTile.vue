<template>
    <div class="post-tile">
        <span class="post-title">{{ post.title }}</span>
        <span class="post-subtitle">{{ post.user.name }} | Geplaatst op {{ post.created }}<span v-if="post.edited"> | Laatst bewerkt op {{ post.edited }}</span></span>
        <span class="post-content" v-bind:class="{'post-content-extended': extended}">{{ post.description }}</span>
        <div class="post-actions"> 
            <div @click="viewLess" v-if="extended" class="description-extender">Lees minder...</div>
            <div @click="viewMore" v-else class="description-extender">Lees meer...</div>
            <router-link class="post-button" to="/Post">Bekijken</router-link>
        </div>
    </div>
</template>

<script>
export default {
    name: 'PostTile',
    data() {
        return {
            extended: false
        }
    },
    methods: {
        viewLess() { this.extended = false; },
        viewMore() { this.extended = true; }
    },
    props: ['post']
}
</script>

<style scoped>
.post-tile {
    width: 100%;
    padding: 8px 4px 4px 12px;
    border: 1px solid var(--gray-bright);
    border-radius: 6px;
    margin: 5px 0;
    box-sizing: border-box;
    overflow: hidden;
}

.post-title {
    display: block;
    font-size: 16pt;
    color: var(--black-smooth);
}

.post-subtitle {
    display: block;
    font-size: 9pt;
    color: var(--black-smooth);
    font-style: italic;
}

.post-content {
    display: block;
    font-size: 11pt;
    color: var(--black-smooth);
    height: 20px;
    overflow: hidden;
    margin: 3px 0;
}

.post-content-extended {
    height: auto;
}

.description-extender {
    color: var(--gray-soft);
    font-size: 9pt;
    cursor: pointer;
    display: inline-block;
    padding: 3px 1px 1px;
    box-sizing: border-box;
    user-select: none;
    -moz-user-select: -moz-none;
}

.post-actions {
    display: block;
    height: 22px;
    box-shadow: 0 -5px 12px -6px #eee;
}

.post-button {
    text-decoration: none;
    float: right;
    padding: 2px 9px 4px;
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

.post-button:hover {
    background-color: var(--green);
}
</style>
