<template>
    <div class="page-selector" v-if="totalEntries > entriesPerPage + 1">
        <button :disabled="currentPage === 1" @click="switchPage(1)" class='left-border-button' v-bind:class="{'inactive': currentPage == 1}">&lt;&lt;</button>
        <button :disabled="currentPage === 1" @click="switchPage(currentPage - 1)" class='selector-button' v-bind:class="{'inactive': currentPage == 1}">&lt;</button>
        <span v-for="button in buttons" v-bind:key="button.id">
            <button :disabled="button.disabled" @click="switchPage(button.id)" class='selector-button' v-bind:class="{'active': button.disabled}">{{button.id}}</button>
        </span>
        <button :disabled="currentPage === totalPages" @click="switchPage(currentPage + 1)" class='selector-button' v-bind:class="{'inactive': currentPage === totalPages}">&gt;</button>
        <button :disabled="currentPage === totalPages" @click="switchPage(totalPages)" class='right-border-button' v-bind:class="{'inactive': currentPage === totalPages}">&gt;&gt;</button>
    </div>
</template>

<script>
export default {
    name: 'PageSelector',
    props: {
        visiblePages: {
            type: Number,
            required: false,
            default: 3
        },
        totalEntries: {
            type: Number,
            required: true
        },
        entriesPerPage: {
            type: Number,
            required: true
        }
    },
    data() {
        return {
            currentPage: 1,
        }
    },
    methods: {
        switchPage(index){
            if (index <= this.totalPages && index >= 1){
                this.currentPage = index;
                this.pageChanged();
            }
        },
        pageChanged(){
            let startIndex = (this.currentPage - 1) * this.entriesPerPage;
            let endIndex = ((startIndex + this.entriesPerPage) > this.totalEntries) ? this.totalEntries-1 : startIndex + this.entriesPerPage;
            this.$emit('pageChanged', startIndex, endIndex);
        }
    },
    computed: {
        totalPages(){
            return Math.ceil(this.totalEntries/this.entriesPerPage);
        },
        startButton(){
            if(this.currentPage == 1){
                return 1;
            }else if(this.currentPage == this.totalPages){
                if(this.totalPages >= this.visiblePages){
                    return this.totalPages - this.visiblePages + 1;
                }else{
                    return 1;
                }
            }else{
                return this.currentPage -1;
            }
        },
        buttons(){
            let buttons = [];
            for(let i = this.startButton; i <= Math.min(this.startButton + this.visiblePages -1, this.totalPages); i++){
                buttons.push({
                    id: i,
                    disabled: i === this.currentPage
                })
            }
            return buttons;
        },
    },
    watch: {
        totalEntries: function() {
            this.pageChanged();
        },
    }
}
</script>

<style scoped>
.page-selector{
    margin-top: 20px;
}

button{
    width: 40px;
    height: 40px;
    background-color: var(--white-base);
    color: var(--green);
    border-style: solid;
    border-color: var(--gray-bright);
    cursor: pointer;
}

.inactive{
    cursor: default;
    color: var(--gray-dark);
}

.active{
    color: var(--white-base);
    background-color: var(--green);
}

.right-border-button{
    border-width: 1px 1px 1px 0px;
    border-top-right-radius: 8px;
    border-bottom-right-radius: 8px;
}

.left-border-button{
    border-width: 1px 1px 1px 1px;
    border-top-left-radius: 8px;
    border-bottom-left-radius: 8px;
}

.selector-button{
    border-width: 1px 1px 1px 0px;
}
</style>
