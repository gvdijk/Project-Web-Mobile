<template>
    <div class="project-tile">
        <span class="project-title">{{ project.projectName }}</span>
        <span class="project-subtitle">Aangemaakt op {{ project.projectCreated }}</span>
        <span class="project-content" v-bind:class="{'project-content-extended': extended}">{{ project.projectDescription }}</span>
        <div class="project-actions"> 
            <div @click="viewLess" v-if="extended" class="description-extender">Lees minder...</div>
            <div @click="viewMore" v-else class="description-extender">Lees meer...</div>
            <router-link v-if="accessible" class="project-button" :to="{ path:`/project/${this.project.projectID}`}"><a>Bekijken</a></router-link>
            <div v-if="isPending" class="project-button disabled">Aangevraagd</div>
            <div v-if="isInvited" class="project-button disabled">Uitgenodigd</div>
            <div v-if="joinVisible" @click="participateInProject" class="project-button">Deelnemen</div>
            <div v-if="requestVisible" @click="requestParticipationInProject" class="project-button">Aanvragen</div>
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
            joinVisible: false,
            requestVisible: false,
            isInvited: false,
            isPending: false,
            accessible: false
        }
    },
    
    methods: {
        viewLess() { this.extended = false; },
        viewMore() { this.extended = true; },
        participateInProject(){
            if (!this.$store.getters.authenticated) {
                this.$emit('requestModal', 'login', {});
                return;
            }
            this.$store.dispatch('createProjectUser', {
                projectID: this.project.projectID,
                role: "USER"
            })
            .then(response => this.$router.push({path: `/project/${this.project.projectID}`}))
            .catch(error => console.log(error.response))
        },
        requestParticipationInProject(){
            if (!this.$store.getters.authenticated) {
                this.$emit('requestModal', 'login', {});
                return;
            }
            this.$store.dispatch('createProjectUser', {
                projectID: this.project.projectID,
                role: "PENDING"
            })
            .then(response => {
                console.log(response);
                this.requestVisible = false;
                this.isPending = true;
            })
            .catch(error => console.log(error.response))
        },
        infoChanged() {
            let index = this.userprojects.findIndex((el) => el.Project_projectID == this.project.projectID);
    
            this.joinVisible = false;
            this.requestVisible = false;
            this.accessible = false;
            this.isInvited = false;
            this.isPending = false;
            
            if (index > -1) {
                let role = this.userprojects[index].projectuserRole; 

                if (role == "INVITED") {
                    this.isInvited = true;
                } else if (role == "PENDING") {
                    this.isPending = true;
                } else {
                    this.accessible = true;
                }
            } else {
                if (this.project.projectVisibility == "PUBLIC") {
                    this.joinVisible = true;
                } else {
                    this.requestVisible = true;
                }
            }
        }
    },
    props: ['project', 'userprojects'],
    created() {
        this.infoChanged();
    },
    watch: {
        project: function() {this.infoChanged()},
        userprojects: function() {this.infoChanged()}
    }
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
    text-decoration: none;
    transition-duration: 0.1s;
}

.project-button:hover {
    background-color: var(--green);
}

.disabled {
    cursor: default;
    background-color: var(--gray-dark);
}
.disabled:hover {
    background-color: var(--gray-dark);
}

</style>
