<template>
    <div class="newproject">
        <h1>Nieuw Project Aanmaken</h1>
        <section>
            <form action="#" @submit.prevent="createAction">
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
                <button type="submit" v-bind:class="{'disabled': disabled}">Aanmaken</button>
            </form>
        </section>
    </div>
</template>

<script>
export default {
    name: 'NewProject',
    data() {
        return {
            project: {
                projectName: "",
                projectDescription: "",
                projectVisibility: "PUBLIC"
            },
            disabled: false
        }
    },
    methods: {
        createAction() {
            if (!this.disabled) {
                this.$store.dispatch('createProject', {
                    name: this.project.projectName,
                    description: this.project.projectDescription,
                    visibility: this.project.projectVisibility
                })
                .then(response => this.$router.push(`/project/${response.data.projectID}`))
                .catch(error => {
                    if (error.response) {
                        // The request was made and the server responded with a status code
                        // that falls out of the range of 2xx
                    } else if (error.request) {
                        // The request was made but no response was received
                        // `error.request` is an instance of XMLHttpRequest in the browser and an instance of
                        // http.ClientRequest in node.js
                        this.disabled = true;
                    } else {
                        // Something happened in setting up the request that triggered an Error
                    }
                })
            }
        }
    }
}
</script>

<style scoped>

h1 {
    font-size: 24pt;
    color: var(--green);
    font-weight: 500;
}

h2 {
    font-size: 16pt;
    color: var(--green);
    font-weight: 400;
}

section {
    padding-bottom: 36px;
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


.disabled {
    background-color: var(--gray-bright);
    cursor: default;
}

button:hover {
    background-color: var(--gray-bright);
}
</style>
