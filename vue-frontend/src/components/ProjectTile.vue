<template>
    <div class="project-tile">
        <span class="project-title"> {{ project.title }} </span>
        <span class="project-subtitle"> {{ project.users }} deelnemers | Gemaakt op {{ project.created }} </span>
        <span class="project-content"> {{ project.description }} </span>
        <div class="project-actions"> 
            <div v-if="project.access" class="project-button">Deelnemen</div>
            <div v-else class="project-button">Aanvragen</div>
            <div class="project-button">Bekijk</div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'ProjectTile',
    props: ['project']
}
</script>

<style scoped>
.project-tile {
    width: 100%;
    padding: 8px 12px;
    border: 1px solid var(--gray-bright);
    border-radius: 6px;
    margin: 5px 0;
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
}

.project-actions {
    display: block;
    text-align: right;
}

.project-button {
    display: inline-block;
    padding: 2px 9px 4px;
    background-color: var(--dark-green);
    color: var(--white-soft);
    border: 1px solid var(--gray-brighter);
    border-radius: 3px;
    margin: 0 3px;
    cursor: pointer;
}

.project-button:hover {
    background-color: var(--green);
}
</style>
