<template>
    <div class="project-tile">
        <span class="project-title">{{ project.title }}</span>
        <span class="project-subtitle">{{ usersPlaceholder }} deelnemers | Gemaakt op {{ createdPlaceholder }}</span>
        <span class="project-content" v-bind:class="{'project-content-extended': extended}">{{ project.body }}</span>
        <div class="project-actions"> 
            <div @click="viewLess" v-if="extended" class="description-extender">Lees minder...</div>
            <div @click="viewMore" v-else class="description-extender">Lees meer...</div>
            <div class="project-button">Bekijken</div>
            <div v-if="project.access" class="project-button">Deelnemen</div>
            <div v-else class="project-button">Aanvragen</div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'ProjectTile',
    data() {
        return {
            extended: false,
            usersPlaceholder: 'x',
            createdPlaceholder: 'dd/mm/yyyy',
        }
    },
    // TODO: See if extentiosion is necessary
    methods: {
        viewLess() { this.extended = false; },
        viewMore() { this.extended = true; }
    },
    props: ['project']
}
</script>

<style scoped>
.project-tile {
    width: 100%;
    padding: 8px 4px 4px 12px;
    border: 1px solid var(--gray-bright);
    border-radius: 6px;
    margin: 5px 0;
    box-sizing: border-box;
}

.project-title {
    display: block;
    font-size: 16pt;
    color: var(--black-smooth);
}

.project-subtitle {
    display: block;
    font-size: 9pt;
    color: var(--black-smooth);
    font-style: italic;
}

.project-content {
    display: block;
    font-size: 11pt;
    color: var(--black-smooth);
    height: 20px;
    overflow: hidden;
    margin: 3px 0;
}

.project-content-extended {
    height: auto;
}

.description-extender {
    color: var(--gray-soft);
    font-size: 9pt;
    cursor: pointer;
    display: inline-block;
    padding: 3px 1px 1px
}

.project-actions {
    display: block;
    height: 22px;
    box-shadow: 0 -5px 12px -6px #eee;
    user-select: none;
    -moz-user-select: -moz-none;
}

.project-button {
    float: right;
    padding: 2px 9px 4px;
    background-color: var(--dark-green);
    color: var(--white-soft);
    font-size: 10pt;
    border: 1px solid var(--gray-brighter);
    border-radius: 3px;
    margin: 0 3px;
    cursor: pointer;
    transition-duration: 0.1s;
}

.project-button:hover {
    background-color: var(--green);
}
</style>
