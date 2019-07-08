<template>
    <div class="modal-content">
        <div class="modal-header">Verwijderen</div>
        <div class="modal-text">
            Weet je zeker dat je 
            <span v-if="body.type == 'post'">dit bericht</span>
            <span v-if="body.type == 'project'">dit project</span>
            <span v-if="body.type == 'projectuser'">deze gebruiker</span>
            <span v-else>deze reactie</span> 
            wilt verwijderen?

        </div>
        <div class="modal-actions">
            <div class="modal-button modal-button-cancel" @click="$emit('closeModal')">Annuleren</div>
            <div class="modal-button modal-button-red" @click="deleteAction">Verwijder</div>
        </div>
    </div>
</template>

<script>
/*
 *  body should be of format { 
 *      type: [project || projectuser || post || comment],
 *      id: [projectID || postID || commentID]
 *      userID: []
 *  }
 */
export default {
    name: 'Delete',
    methods: {
        deleteAction() {
            //  console.log(`Deleted ${this.body.type} with id ${this.body.id}`);
            if (this.body.type == 'project') {
                this.$store.dispatch('deleteProject', this.body.id)
                .then(response => {
                    this.$emit('closeModal');
                    this.body.cb(response);
                })
                .catch(error => {
                    if (error.request) this.$emit('closeModal');
                });
            } else if (this.body.type == 'post') {
                this.$store.dispatch('deletePost', this.body.id)
                .then(response => { 
                    this.$emit('closeModal');
                    this.body.cb(this.body.id);
                })
                .catch(error => {
                    if (error.request) this.$emit('closeModal');
                });
            } else if (this.body.type == 'projectuser') {
                this.$store.dispatch('deleteProjectUser', {
                    projectID: this.body.id,
                    userID: this.body.userID
                })
                .then(response => { 
                    this.$emit('closeModal'); 
                    this.body.cb(this.body.id, this.body.userID);
                    })
                .catch(error => {
                    if (error.request) this.$emit('closeModal');
                });
            } else {
                this.$store.dispatch('deleteComment', this.body.id)
                .then(response => {
                    this.$emit('closeModal');
                    this.body.cb(this.body.id);
                })
                .catch(error => {
                    if (error.request) this.$emit('closeModal');
                });
            }
        }
    },
    props: ['body']
}
</script>

<style scoped>

</style>
