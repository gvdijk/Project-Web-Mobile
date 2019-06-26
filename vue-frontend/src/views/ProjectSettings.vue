<template>
    <div class="projectsettings">
        <h1>Project Instellingen</h1>
        <section>
            <label>Naam</label>
            <input type="text" :value="project.projectName">
            <label>Omschrijving</label>
            <textarea :value="project.projectDescription"></textarea>
            <button type="submit">Aanpassen</button>
        </section>
        <section>
            <label>Gebruikers</label>
            <table>
                <tr :key="user.User_userID" v-for="user in users">
                    <td>{{user.User_userID}}</td>
                    <td>
                        
                    </td>
                    <td>
                        <div class="user-button"></div>
                    </td>
                </tr>
            </table>
            <button type="submit">Aanpassen</button>
        </section>
    </div>
</template>

<script>
export default {
    name: 'ProjectSettings',
    data() {
        return {
            project: {},
            users: []
        }
    },
    methods: {
        fetchProject(){
            this.$store.dispatch('getProjectByID', this.$route.params.id)
            .then( response => this.project = response)
            .catch( error => console.log(error))
        },
        fetchProjectUsers(){
            this.$store.dispatch('getProjectUsers', this.$route.params.id)
            .then( response => this.users = response)
            .catch( error => console.log(error))
        }
    },
    created() {
        this.fetchProject();
        this.fetchProjectUsers();

    }
}
</script>

<style scoped>

h1 {
    font-size: 24pt;
    color: var(--green);
    font-weight: 500;
}

section {
    border-bottom: 1px solid var(--gray-base);
    padding-bottom: 64px;
}

button {
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

button:hover {
    background-color: var(--green);
}

label {
    display: block;
    font-weight: 300;
    color: var(--gray-dark);
    font-size: 13pt;
    margin: 6px 0 3px;
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
    border-bottom: 1px solid var(--gray-bright);
}

.user-button {
    width: 28px;
    height: 28px;
}

.old-box {
    display: none;
}

.new-box {
    display: inline-block;
    width: 16px;
    height: 16px;
    background-color: var(--gray-base);
    cursor: pointer;
}

.new-box:hover {
    background-color: var(--gray-bright);
}

</style>
