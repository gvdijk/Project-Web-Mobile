<template>
    <div class="modal-content">
        <div class="modal-header">Bewerken</div>
        <div class="modal-text">
            Geef een nieuwe omschrijving voor 
            <span v-if="body.type == 'post'">dit bericht</span>
            <span v-else>deze reactie</span>
            <span class="additional-info" v-if="body.type == 'post'">Titel kan niet worden aangepast</span>
            <textarea v-model="body.text"></textarea>
        </div>
        <div class="modal-actions">
            <div class="modal-button modal-button-cancel" @click="$emit('closeModal')">Annuleren</div>
            <div class="modal-button" @click="updateAction">Bevestig</div>
        </div>
    </div>
</template>

<script>
/*
 *  body should be of format { 
 *      type: [post || comment],
 *      id: [postID || commentID].
 *      text: 'original value'
 *  }
 */
export default {
    name: 'Edit',
    methods: {
        updateAction() {
            if (this.body.type == 'post') {
                this.$store.dispatch('updatePost', {
                    id: this.body.id,
                    text: this.body.text
                })
                .then(response => {
                    this.$emit('closeModal');
                    this.body.cb(response);
                })
                .catch(error => console.log(error));
            } else {
                this.$store.dispatch('updateComment', {
                    id: this.body.id,
                    text: this.body.text
                })
                .then(response => {
                    this.$emit('closeModal');
                    this.body.cb(response);
                })
                .catch(error => console.log(error));
            }
        }
    },
    props: ['body']
}
</script>

<style scoped>
    .additional-info {
        display: block;
        font-size: 10pt;
        color: var(--gray-base);
        padding: 2px 0 3px;
        font-style: italic;
    }
</style>
