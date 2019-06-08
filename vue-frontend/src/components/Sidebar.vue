<template>
    <aside v-bind:class="{'hide-aside': !extended}">
        <div class="side-extender" v-bind:class="{'left-float': !extended}">
            <div v-if="extended" @click="$emit('set-extended', false)">
                <span>&#171;</span>
            </div>
            <div v-else  @click="$emit('set-extended', true)">
                <span>&#187;</span>
            </div>
        </div>
        <div class="side-pane">
            <label @click="toggleInfoVisibility">Pagina specifiek</label>
            <div class="side-pane-content" v-if="extendedInfo">
                <!-- TODO: make content aware -->
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
            </div>
        </div>
        <div class="side-pane" v-if="authenticated">
            <label @click="toggleMyProjectsVisibility">Mijn Projecten</label>
            <div class="side-pane-content" v-if="extendedProjects">
                <router-link :key="project.id" v-for="project in myProjects" to="/Project"><a>{{project.title}}</a></router-link>
            </div>
        </div>
        <div class="side-pane" v-if="authenticated">
            <label @click="toggleRecentProjectsVisibility">Recente Projecten</label>
            <div class="side-pane-content" v-if="extendedRecent">
                <router-link :key="project.id" v-for="project in recentProjects" to="/Project"><a>{{project.title}}</a></router-link>
            </div>
        </div>
        <div class="side-pane">
           <label>Explore</label>
            <div class="side-pane-content">
                
            </div>
        </div>
    </aside>
</template>

<script>
export default {
    name: 'Sidebar',
    data() {
        return {
            authenticated: true,
            extendedInfo: true,
            extendedProjects: true,
            extendedRecent: true,
            myProjects: [
                {
                    id: 1,
                    title: 'Invisiline'
                },
                {
                    id: 2,
                    title: 'Barbarapapa'
                },
                {
                    id: 3,
                    title: 'De beste titel voor een lange beschrijving'
                }
            ],
            recentProjects: [
                {
                    id: 1,
                    title: 'Invisiline'
                },
                {
                    id: 2,
                    title: 'Barbarapapa'
                },
                {
                    id: 3,
                    title: 'De beste titel voor een lange beschrijving'
                }
            ]
        }
    },
    methods: {
        toggleInfoVisibility() { this.extendedInfo = !this.extendedInfo; },
        toggleMyProjectsVisibility() { this.extendedProjects = !this.extendedProjects; },
        toggleRecentProjectsVisibility() { this.extendedRecent = !this.extendedRecent; }
    },
    props: ['extended']
}
</script>

<style scoped>

aside {
    position: absolute;
    top: 0;
    left: 0;
    height: 100%;
    width: var(--side-full-width);
    background-color: var(--black-smooth);
    padding: var(--header-height) 0 var(--footer-height) 0;
    box-sizing: border-box;
    white-space: nowrap;
    transition-duration: 0.2s;
    z-index: 50;
}

.hide-aside  {
    width: 0px;
}

.side-pane {
    position: relative;
    display: block;
    border-bottom: 2px solid var(--gray-darker);
    padding: 5px;
    box-sizing: border-box;
    overflow-x: hidden;
}

.side-pane-content {
    padding: 0px 10px 3px 10px;
    box-sizing: border-box;
    color: var(--white-soft);
    font-size: 11pt;
    overflow: hidden;
}

.side-pane-content a {
    display: block;
    font-size: 11pt;
    color: var(--gray-soft);
    text-decoration: none;
    overflow: hidden;
}

.side-pane-content a:hover {
    color: var(--green);
}

.hide-aside .side-pane {
    display: none;
}

.side-pane label {
    display: block;
    color: var(--white-soft);
    font-size: 12pt;
    font-weight: 500;
    padding: 5px;
    box-sizing: border-box;
    cursor: pointer;
    transition-duration: 0.1s;
    height: 32px;
    user-select: none;
    -moz-user-select: -moz-none;
}

.side-pane label:hover {
    color: var(--green);
}

.side-extender {
    position: absolute;
    height: 24px;
    width: 24px;
    text-align: center;
    top: 0;
    margin-top: var(--header-height);
    left: var(--side-full-width);
    background-color: var(--gray-darker);
    border-bottom-right-radius: 4px;
    transition-duration: 0.2s;
    user-select: none;
    -moz-user-select: -moz-none;
}

.side-extender div {
    position: relative;
    width: 100%;
    height: 100%;
    cursor: pointer;
}

.side-extender div span {
    color: var(--white-soft);
    font-size: 18pt;
    line-height: 10pt;
    transition-duration: 0.1s;
}

.side-extender div span:hover {
    color: var(--green);
}

.left-float {
    left: 0px;
}

</style>
