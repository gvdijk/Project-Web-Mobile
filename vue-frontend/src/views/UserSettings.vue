<template>
    <div class="usersettings">
        <h1>{{user.userName}} Instellingen</h1>
        <section>
            <label>Projecten overzicht</label>
            <div class="table-wrapper">
                <table>
                    <tr>
                        <th>Project</th>
                        <th>Status</th>
                        <th>Lid sinds</th>
                        <th>Acties</th>
                    </tr>
                    <tr :key="project.projectID" v-for="project in projects">
                        <td>
                            <router-link class="router-link" :to="{ path:`/project/${project.project.projectID}`}">{{project.project.projectName}}</router-link>
                        </td>
                        <td>
                            {{userRole(project.projectuserRole)}}
                        </td>
                        <td>
                            {{project.projectuserJoined}}
                        </td>
                        <td>
                            <div class="user-button" title="Accepteren" 
                            v-if="project.projectuserRole == 'INVITED'"
                            @click="acceptInvite(project.Project_projectID)"><i class="fa fa-check"></i></div>
                            <div class="user-button" title="Weigeren" 
                            v-if="project.projectuserRole == 'INVITED'"
                            @click="$emit('requestModal', 'delete', {'type': 'projectuser', 'id': project.project.projectID, 'userID': null})"><i class="fa fa-times"></i></div>
                            <div class="user-button" title="Instellingen" 
                            v-if="project.projectuserRole == 'OWNER' || project.projectuserRole == 'ADMIN'"
                            @click="goToSettings(project)"><i class="fa fa-cog"></i></div>
                            <div class="user-button" title="Verlaten" 
                            v-if="project.projectuserRole != 'INVITED'"
                            @click="$emit('requestModal', 'delete', {'type': 'projectuser', 'id': project.project.projectID, 'userID': false, 'cb': deletedProject})"><i class="fa fa-minus"></i></div>
                        </td>
                    </tr>
                </table>
            </div>
        </section>
        <section>
            <label>Berichten overzicht</label>
            <div class="table-wrapper">
                <table>
                    <tr>
                        <th>Bericht</th>
                        <th>Project</th>
                        <th>Geplaatst</th>
                        <th>Acties</th>
                    </tr>
                    <tr :key="post.postID" v-for="post in posts">
                        <td><router-link class="router-link" :to="{ path:`/project/${post.project.projectID}/post/${post.postID}`}">{{post.postTitle}}</router-link></td>
                        <td>
                            <router-link class="router-link" :to="{ path:`/project/${post.project.projectID}`}">{{post.project.projectName}}</router-link>
                        </td>
                        <td>
                            {{post.postCreated}}
                        </td>
                        <td>
                            <div class="user-button" title="Reageren" 
                            @click="$emit('requestModal', 'create', {'type': 'comment', 'id': post.postID})"><i class="fa fa-reply"></i></div>
                            <div class="user-button" title="Bewerken"
                            @click="$emit('requestModal', 'edit', {'type': 'post', 'id': post.postID, 'text': post.postContent})"><i class="fa fa-edit"></i></div>
                            <div class="user-button" title="Verwijderen"
                            @click="$emit('requestModal', 'delete', {'type': 'post', 'id': post.postID, 'cb': deletedPost})"><i class="fa fa-times"></i></div>
                        </td>
                    </tr>
                </table>
            </div>
        </section>
        <section>
            <label>Reacties overzicht</label>
            <div class="table-wrapper">
                <table>
                    <tr>
                        <th>Reacties</th>
                        <th>Bericht</th>
                        <th>Geplaatst</th>
                        <th>Acties</th>
                    </tr>
                    <tr :key="comment.commentID" v-for="comment in comments">
                        <td><router-link class="router-link" :to="{ path:`/project/${comment.post.postProject}/post/${comment.post.postID}`}">{{comment.commentContent}}</router-link></td>
                        <td>
                            <router-link class="router-link" :to="{ path:`/project/${comment.post.postProject}/post/${comment.post.postID}`}">{{comment.post.postTitle}}</router-link>
                        </td>
                        <td class="date-col">
                            {{comment.commentCreated}}
                        </td>
                        <td>
                            <div class="user-button" title="Reageren" 
                            @click="$emit('requestModal', 'create', {'type': 'child', 'id': comment.commentPost, 'parent': comment.commentID})"><i class="fa fa-reply"></i></div>
                            <div class="user-button" title="Bewerken"
                            @click="$emit('requestModal', 'edit', {'type': 'comment', 'id': comment.commentID, 'text': comment.commentContent})"><i class="fa fa-edit"></i></div>
                            <div class="user-button" title="Verwijderen"
                            @click="$emit('requestModal', 'delete', {'type': 'comment', 'id': comment.commentID, 'cb': deletedComment})"><i class="fa fa-times"></i></div>
                        </td>
                    </tr>
                </table>
            </div>
        </section>
        <!-- <section>
            <div class="delete-button" @click="$emit('requestModal', 'delete', {'type': 'user', 'id': userID})">Account Verwijderen</div>
        </section> -->
    </div>
</template>

<script>
import { mapGetters } from 'vuex';
export default {
    name: 'UserSettings',
    data() {
        return {
            user: {},
            projects: [],
            posts: [],
            comments: []
        }
    },
    computed: {
        ...mapGetters(["userID"])
    },
    methods: {
        goToSettings(project) {
            this.$router.push({path: `/project/${project.project.projectID}/settings`});
        },
        userRole(role) {
            switch(role) {
                case "USER": return "Gebruiker";
                case "ADMIN": return "Administrator";
                case "INVITED": return "Uitgenodigd";
                case "PENDING": return "Aangevraagd";
                case "OWNER": return "Eigenaar";
            }
        },
        deletedProject(projectID) {
            let index = this.projects.findIndex(project => project.projectID === projectID);
            this.comments.splice(index, 1);
        },
        deletedPost(postID) {
            let index = this.posts.findIndex(post => post.postID === postID);
            this.posts.splice(index, 1);
        },
        deletedComment(commentID) {
            let index = this.comments.findIndex(comment => comment.commentID === commentID);
            this.comments.splice(index, 1);
        },
        acceptInvite(projectID) {
            this.$store.dispatch('updateProjectUser', {
                projectID: projectID,
                userID: null,
                role: "USER"
            })
            .then(response => { 
                let index = this.projects.findIndex(project => project.Project_projectID === response.Project_projectID);
                this.projects[index].projectuserRole = "USER";
            })
            .catch(error => console.log(error.response))
        },
        fetchUser(){
            this.$store.dispatch('getUser')
            .then(response => this.user = response)
            .catch(error => console.log(error.response))
        },
        fetchUserProjects(){
            this.$store.dispatch('getUserProjects')
            .then(response => this.projects = response)
            .catch(error => console.log(error.response))
        },
        fetchUserPosts(){
            this.$store.dispatch('getUserPosts')
            .then(response => this.posts = response)
            .catch(error => console.log(error.response))
        },
        fetchUserComments(){
            this.$store.dispatch('getUserComments')
            .then(response => this.comments = response)
            .catch(error => console.log(error.response))
        },
        updateDetails(){
            this.$store.dispatch('updateProject', {
                projectID: this.project.projectID,
                name: this.project.projectName,
                description: this.project.projectDescription,
                visibility: this.project.projectVisibility
            })
            .then(response => this.project = response)
            .catch(error => console.log(error))
        },

    },
    created() {
        this.fetchUser();
        this.fetchUserProjects();
        this.fetchUserPosts();
        this.fetchUserComments();
    },
    computed: {
        // commentPost(comment) {
        //     console.log(comment);
        //     return comment.post.postTitle || null;
        // }
    }
}
</script>

<style scoped>

section {
    padding-bottom: 36px;
}

.table-wrapper {
    overflow-x: auto;
}

.button {
    display: block;
    float: right;
    padding: 4px 9px 6px;
    background-color: var(--dark-green);
    color: var(--white-soft);
    font-size: 10pt;
    border: 2px solid var(--gray-brighter);
    border-radius: 3px;
    margin: 10px 3px 5px;
    cursor: pointer;
    user-select: none;
    text-decoration: none;
    -moz-user-select: -moz-none;
    transition-duration: 0.2s;
}

.button:hover {
    background-color: var(--green);
}

.delete-button {
    display: block;
    float: right;
    padding: 5px 12px 7px;
    background-color: var(--dark-red);
    color: var(--white-soft);
    font-size: 12pt;
    border: 2px solid var(--gray-brighter);
    border-radius: 3px;
    cursor: pointer;
    user-select: none;
    text-decoration: none;
    -moz-user-select: -moz-none;
    transition-duration: 0.2s;
}

.delete-button:hover {
    background-color: var(--red);
}

label {
    display: block;
    font-weight: 300;
    color: var(--gray-dark);
    font-size: 13pt;
    margin: 10px 0 3px;
}

input {
    width: 100%;
    height: 36px;
    font-size: 14px;
    padding: 4px 8px;
    outline: 0;
    border-radius: 3px;
    border: 1px solid var(--gray-bright);
    color: var(--black-deep);
    box-sizing: border-box;
}

select {
    font-size: 14px;
    padding: 4px 8px;
    outline: 0;
}

textarea {
    display: block;
    width: 100%;
    font-family: var(--font-fam);
    font-size: 14px;
    padding: 4px 8px;
    box-sizing: border-box;
    margin-top: 5px;
    outline: 0;
    border-radius: 3px;
    border: 1px solid var(--gray-bright);
    box-sizing: border-box;
    color: var(--black-deep);
    max-width: 100%;
    min-width: 100%;
}

input:focus {
    border: 1px solid var(--green);
}

textarea:focus {
    border: 1px solid var(--green);
}

table {
    width: 100%;
}

tr {
    /* border-bottom: 1px solid var(--gray-bright); */
}

th {
    text-align: left;
    border-bottom: 1px solid var(--gray-bright);
    color: var(--dark-green);
}

td {
    color: var(--black-smooth);
    font-style: italic;
    font-size: 10pt;
    min-width: 90px;
    border-bottom: 1px solid var(--gray-bright);
    padding: 0 2px 4px;
    word-break: break-all;
    word-break: break-word;
    overflow: hidden;
    max-width: 60vw;
}

td:first-child {
    min-width: 240px;
    width: 500px;
}

td:last-child {
    min-width: 80px;
    width: 80px;
    max-width: 80px;
}

.router-link {
    text-decoration: none;
    color: var(--black-mid);
    cursor: pointer;
    transition-duration: 0.1s;
    font-style: normal;
    font-size: 12pt;
}

.router-link:hover {
    color: var(--green);
}

.user-button {
    display: inline-block;
    width: 24px;
    height: 24px;
    cursor: pointer;
    font-size: 12pt;
}


i {
    color: var(--gray-dark);
    transition-duration: 0.1s;
    padding: 2px;
}

.is-admin {
    color: var(--yellow);
}

.fa-check:hover,
.fa-reply:hover {
    color: var(--green);
}

.fa-edit:hover,
.fa-cog:hover {
    color: var(--blue);
}

.fa-star:hover {
    color: var(--yellow);
}

.fa-times:hover,
.is-admin:hover,
.fa-ban:hover {
    color: var(--red);
}

.fa-minus:hover {
    color: var(--orange);
}

</style>
