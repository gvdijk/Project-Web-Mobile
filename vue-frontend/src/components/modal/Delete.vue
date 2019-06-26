<template>
    <div class="modal-content">
        <div class="modal-header">Verwijderen</div>
        <div class="modal-text">
            Weet je zeker dat je 
            <span v-if="body.type == 'post'">dit bericht</span>
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
 *      type: [project || post || comment],
 *      id: [projectID || postID || commentID]
 *  }
 */
export default {
    name: 'Delete',
    methods: {
        deleteAction() {
             console.log(`Deleted ${this.body.type} with id ${this.body.id}`);
            if (this.body.type == 'project') {
                this.$store.dispatch('deleteProject', this.body.id)
                .then(this.$emit('closeModal'))
                .catch(error => console.log(error));
            } else if (this.body.type == 'post') {
                this.$store.dispatch('deletePost', this.body.id)
                .then(this.$emit('closeModal'))
                .catch(error => console.log(error));
            } else {
                this.$store.dispatch('deleteComment', this.body.id)
                .then(this.$emit('closeModal'))
                .catch(error => console.log(error));
            }
        }
    },
    props: ['body']
}
</script>

<style scoped>

</style>
