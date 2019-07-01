<template>
    <div class="projectsettings">
        <h1>Project Instellingen</h1>
        <section>
            <label>Naam</label>
            <input type="text" v-model="project.projectName" placeholder="Naam">
            <label>Omschrijving</label>
            <textarea v-model="project.projectDescription" placeholder="Omschrijving"></textarea>
            <label>Zichtbaarheid</label>
            <select v-model="project.projectVisibility">
                <option value="PUBLIC">Openbaar</option>
                <option value="RESTRICTED">Beschermd</option>
                <option value="PRIVATE">Verborgen</option>
            </select>
            <div class="button" @click="updateDetails">Aanpassen</div>
            <span class="status">{{editStatus}}</span>
            <span class="status error">{{editError}}</span>
        </section>
            <h2>Gebruikers</h2>
        <section>
            <label>Gebruiker uitnodigen</label>
            <form action="#" @submit.prevent="inviteUser">
                <input type="text" v-model="inviteUserName" placeholder="Gebruikersnaam">
                <button class="button">Uitnodigen</button>
            </form>
            <span class="status">{{inviteStatus}}</span>
            <span class="status error">{{inviteError}}</span>
        </section>
        <section>
            <label>Gebruikers overzicht</label>
            <div class="table-wrapper">
                <table>
                    <tr>
                        <th>Naam</th>
                        <th>Type</th>
                        <th>Lid sinds</th>
                        <th>Acties</th>
                    </tr>
                    <tr :key="user.User_userID" v-for="user in users">
                        <td>{{user.user.userName}}</td>
                        <td>
                            {{userRole(user.projectuserRole)}}
                        </td>
                        <td>
                            {{user.projectuserJoined}}
                        </td>
                        <td>
                            <div class="user-button" title="Accepteren" @click="acceptUser(user.User_userID)"
                            v-if="user.projectuserRole == 'PENDING'"><i class="fa fa-check"></i></div>
                            <div class="user-button" title="Weigeren"
                            @click="$emit('requestModal', 'delete', {'type': 'projectuser', 'id': user.Project_projectID, 'userID': user.User_userID})"
                            v-if="user.projectuserRole == 'PENDING'"><i class="fa fa-times"></i></div>
                            <div class="user-button" title="Annuleren"
                            @click="$emit('requestModal', 'delete', {'type': 'projectuser', 'id': user.Project_projectID, 'userID': user.User_userID})"
                            v-if="user.projectuserRole == 'INVITED'"><i class="fa fa-minus"></i></div>
                            <div class="user-button" title="Promoveer naar administrator" @click="promoteUser(user.User_userID)"
                            v-if="user.projectuserRole == 'USER' && isOwner"><i class="fa fa-star"></i></div>
                            <div class="user-button" title="Degradeer naar gebruiker" @click="demoteUser(user.User_userID)"
                            v-if="user.projectuserRole == 'ADMIN' && isOwner"><i class="fa fa-star is-admin"></i></div>
                            <div class="user-button" title="Verwijder gebruiker van project"
                            @click="$emit('requestModal', 'delete', {'type': 'projectuser', 'id': user.Project_projectID, 'userID': user.User_userID})"
                            v-if="(user.projectuserRole == 'USER' && (isAdmin || isOwner)) || (user.projectuserRole == 'ADMIN' && isOwner) "><i class="fa fa-minus"></i></div>
                            <!-- <div class="user-button" title="Ban gebruiker van project"><i class="fa fa-ban"></i></div> -->
                        </td>
                    </tr>
                </table>
            </div>
        </section>
        <!-- <section>
            <div class="delete-button" v-if="isOwner" @click="$emit('requestModal', 'delete', {'type': 'project', 'id': project.projectID})">Project Verwijderen</div>
        </section> -->
    </div>
</template>

<script>
import { setTimeout } from 'timers';
export default {
    name: 'ProjectSettings',
    data() {
        return {
            project: {},
            users: [],
            inviteUserName: "",
            userprojects: [],
            isAdmin: false,
            isOwner: false,
            inviteStatus: "",
            editStatus: "",
            editError: "",
            inviteError: ""
        }
    },
    methods: {
        userRole(role) {
            switch(role) {
                case "USER": return "Gebruiker";
                case "ADMIN": return "Administrator";
                case "INVITED": return "Uitgenodigd";
                case "PENDING": return "Aangevraagd";
                case "OWNER": return "Eigenaar";
            }
        },
        fetchProject(){
            this.$store.dispatch('getProjectByID', this.$route.params.id)
            .then(response => this.project = response)
            .catch(error => console.log(error))
        },
        fetchProjectUsers(){
            this.$store.dispatch('getProjectUsers', this.$route.params.id)
            .then(response => this.users = response)
            .catch(error => console.log(error))
        },
        updateDetails(){
            this.$store.dispatch('updateProject', {
                projectID: this.project.projectID,
                name: this.project.projectName,
                description: this.project.projectDescription,
                visibility: this.project.projectVisibility
            })
            .then(response => {
                this.project = response
                this.editStatus = "Succesvol aangepast"
                setTimeout(() => this.editStatus = "", 3000);
            })
            .catch(error => {
                this.editError = "Aanpassen mislukt"
                setTimeout(() => this.editError = "", 3000);
            })
        },
        acceptUser(userID){
            this.$store.dispatch('updateProjectUser', {
                projectID: this.project.projectID,
                userID: userID,
                role: "USER"
            })
            .then(response => { 
                let index = this.users.findIndex(user => user.User_userID === response.User_userID);
                this.users[index].projectuserRole = "USER";
            })
            .catch(error => console.log(error))
        },
        promoteUser(userID){
            this.$store.dispatch('updateProjectUser', {
                projectID: this.project.projectID,
                userID: userID,
                role: "ADMIN"
            })
            .then(response => { 
                let index = this.users.findIndex(user => user.User_userID === response.User_userID);
                this.users[index].projectuserRole = "ADMIN";
            })
            .catch(error => console.log(error))
        },
        demoteUser(userID){
            this.$store.dispatch('updateProjectUser', {
                projectID: this.project.projectID,
                userID: userID,
                role: "USER"
            })
            .then(response => { 
                let index = this.users.findIndex(user => user.User_userID === response.User_userID);
                this.users[index].projectuserRole = "USER";
            })
            .catch(error => console.log(error))
        },
        inviteUser(){
            this.$store.dispatch('getUserByName', this.inviteUserName)
            .then(response => { 
                this.$store.dispatch('createProjectUser', {
                    projectID: this.project.projectID,
                    userID: response[0].userID,
                    role: "INVITED"
                })
                .then(response => { 
                    this.inviteStatus = "Gebruiker uitgenodigd";
                    setTimeout(() => this.inviteStatus = "", 3000);
                })
                .catch(error => { 
                    this.inviteError = "Uitnodigen mislukt, is de gebruiker al lid?";
                    setTimeout(() => this.inviteError = "", 3000);
                })
            })
            .catch(error => { 
                this.inviteError = "Gebruiker niet gevonden";
                    setTimeout(() => this.inviteError = "", 3000);
                // FIXME: handle other errors
            })

        },

    },
    created() {
        this.fetchProject();
        this.fetchProjectUsers();
        this.$store.dispatch('getUserProjects')
            .then(response => this.userprojects = response)
            .catch(error => console.log(error.response));
    },
    watch: {
        userprojects: function() {
            let index = this.userprojects.findIndex((el) => el.Project_projectID == this.project.projectID);
            if (index > -1) {
                let role = this.userprojects[index].projectuserRole; 
                if (role == "ADMIN") this.isAdmin = true;
                if (role == "OWNER") this.isOwner = true;
            } else {
                //FIXME: User should not be here
            }
        }
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

.status {
    display: block;
    float: right;
    padding: 4px 9px 6px;
    color: var(--black-smooth);
    font-size: 10pt;
    margin: 10px 3px 5px;
    user-select: none;
    transition-duration: 0.2s;
}

.error {
    color: var(--red);
    padding: 4px 0 6px;
    margin: 10px 0 5px;
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


.user-button {
    display: inline-block;
    width: 24px;
    height: 24px;
    cursor: pointer;
}


i {
    color: var(--gray-dark);
    transition-duration: 0.1s;
}

.is-admin {
    color: var(--yellow);
}

.fa-check:hover {
    color: var(--green);
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
