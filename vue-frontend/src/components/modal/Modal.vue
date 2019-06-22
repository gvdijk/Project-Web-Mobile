<template>
    <div class="modal">
        <div class="modal-wrapper">
            <div class="modal-centerer">
                <div class="modal-body">
                    <div class="modal-close fa fa-times" @click="$emit('closeModal')"></div>
                    <Login 
                        v-if="modaltype == 'login'"
                        v-on:closeModal="$emit('closeModal')"
                    />
                    <Delete 
                        v-if="modaltype == 'delete'"
                        v-bind:body="modaldata"
                        v-on:closeModal="$emit('closeModal')"
                    />
                    <Create
                        v-if="modaltype == 'create'"
                        v-bind:body="modaldata"
                        v-on:closeModal="$emit('closeModal')"
                    />
                    <Edit 
                        v-if="modaltype == 'edit'"
                        v-bind:body="modaldata"
                        v-on:closeModal="$emit('closeModal')"
                    />
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import Login from './Login.vue';
import Delete from './Delete.vue';
import Create from './Create.vue';
import Edit from './Edit.vue';

export default {
    name: 'Modal',
    components: {
        Login,
        Delete,
        Create,
        Edit
    },
    props: ['modaltype', 'modaldata']
}
</script>

<style>

.modal {
    position: fixed;
    display: block;
    width: 100vw;
    height: 100vh;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-color: rgba(0,0,0,0.9);
    z-index: 10000;
}

.modal-wrapper {
    position: relative;
    width: 100vw;
    height: 100vh;
}

.modal-centerer {
    position: relative;
    display: inline-block;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    max-height: 90vh;
    max-width: 90vw;
}

.modal-body {
    box-sizing: border-box;
    width: 480px;
    min-height: 60px;
    max-width: 100%;
    max-height: 100%;
    padding: 10px;
    background-color: var(--black-soft);
    box-sizing: border-box;
}

.modal-content {
    position: relative;
}

.modal-header {
    display: block;
    font-size: 24pt;
    color: var(--green);
    margin: 12px 12px 0 12px;
    box-sizing: border-box;
}

.modal-text {
    display: block;
    font-size: 11pt;
    color: var(--white-soft);
    padding: 4px 16px;
    box-sizing: border-box;
}

.modal-close {
    position: absolute;
    top: 0;
    right: 0;
    margin: 5px 10px;
    padding: 5px;
    color: var(--gray-darker);
    user-select: none;
    -moz-user-select: -moz-none;
    cursor: pointer;
    font-size: 18pt;
    z-index: 10001;
    transition-duration: 0.2s;
}

.modal-close:hover {
    color: var(--white-soft);
}

.modal-actions {
    display: block;
    height: 40px;
}

.modal-button {
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
    -moz-user-select: -moz-none;
    transition-duration: 0.2s;
}

.modal-button:hover {
    background-color: var(--green);
}

.modal-button-red {
    background-color: var(--dark-red);
}
.modal-button-red:hover {
    background-color: var(--red);
}

.modal-button-cancel {
    background-color: var(--dark-blue);
}
.modal-button-cancel:hover {
    background-color: var(--blue);
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

label {
    display: block;
    font-weight: 300;
    color: var(--gray-bright);
    font-size: 11pt;
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

input:focus {
    border: 1px solid var(--green);
}

textarea:focus {
    border: 1px solid var(--green);
}


</style>
