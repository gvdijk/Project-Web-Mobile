<template>
    <div class="page-selector">
        <button class='border-button'>&lt;&lt;</button>
        <button class='selector-button'>&lt;</button>
        <button class='selector-button'>1</button>
        <button class='selector-button'>&gt;</button>
        <button class='border-button'>&gt;&gt;</button>
    </div>
</template>

<script>
export default {
    name: 'PageSelector',
    data() {
        return {

        }
    },
    methods: {

    },
    props: ['']
}
</script>

<style scoped>
button{
    width: 30px;
    height: 30px;
}

.border-button{
    
}

.selector-button{

}
</style>
