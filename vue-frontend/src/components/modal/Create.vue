<template>
    <div class="modal-content">
        <div class="modal-header">Plaats een {{body.type == 'post' ? "bericht" : "reactie"}}</div>
        <div class="modal-text">
            {{body.message}}
            <label v-if="body.type == 'post'">Titel</label>
            <input v-if="body.type == 'post'" type="text" v-model="title" placeholder="Titel">
            <label>Omschrijving</label>
            <textarea v-model="description" placeholder="Omschrijving"></textarea>
        </div>
        <div class="modal-actions">
            <div class="modal-button modal-button-cancel" @click="$emit('closeModal')">Annuleren</div>
            <div class="modal-button" @click="createAction">Aanmaken</div>
        </div>
    </div>
</template>

<script>
/*
 *  body should be of format { 
 *      type: [post || comment || child], 
 *      id: [projectID || postID || commentID],
 *      parent: [commentID]
 *  }
 */
export default {
    name: 'Create',
    data() {
        return {
            title: "",
            description: ""
        }
    },
    methods: {
        createAction() {
            if (this.body.type == 'post') {
                this.$store.dispatch('createPost', {
                   projectID: this.body.id,
                   title: this.title,
                   content: this.description  
                })
                .then(response => {
                    this.$router.push(`/project/${this.body.id}/post/${response.data.postID}`);
                    this.$emit('closeModal');
                })
                .catch(error => console.log(error))
            } else {
                this.$store.dispatch('createComment', {
                   postID: this.body.id,
                   parent: this.body.parent || null,
                   content: this.description
                })
                .then(response => {
                    this.$emit('closeModal');
                    this.body.cb(response);
                })
                .catch(error => console.log(error))
            }
        }
    },
    props: ['body']
}
</script>

<style scoped>

</style>
