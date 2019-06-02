<template>
    <aside>

        <div class="side-pane">
            <label class="side-pane-title">Pagina specifiek</label>
            
            <div class="side-pane-content">
                <!-- TODO: fetch content -->
            </div>
        </div>
        <div class="side-pane">
            <label class="side-pane-title">Mijn Projecten</label>
            <div class="side-pane-content">
                <!-- TODO: fetch content, hide when logged out -->
            </div>
        </div>
        <div class="side-pane">
            <label class="side-pane-title">Recente Projecten</label>
            <div class="side-pane-content">
                <!-- TODO: fetch content, hide when logged out -->
            </div>
        </div>
        <div class="side-pane">
           <label class="side-pane-title">Explore</label>
            <div class="side-pane-content">
                
            </div>
        </div>
    </aside>
</template>

<script>
export default {
    name: 'Sidebar'
}
</script>

<style scoped>

aside {
    position: absolute;
    top: 0;
    left: 0;
    height: 100%;
    width: var(--side-full-width);
    background-color: var(--black-smooth);
    padding: var(--header-height) 0 var(--footer-height) 0;
    box-sizing: border-box;
}

.side-pane {
    display: block;
    border-bottom: 2px solid var(--gray-darker);
    padding: 5px;
    box-sizing: border-box;
}

.side-pane-title {
    display: block;
    color: var(--white-soft);
    font-size: 12pt;
    font-weight: 500;
    padding: 5px;
    box-sizing: border-box;
    cursor: pointer;
}

.side-pane-title:hover {
    color: var(--green);
}

</style>
