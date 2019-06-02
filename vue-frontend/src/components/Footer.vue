<template>
    <footer>
        <div class="footer-content">
            <div class="footer-column">
                <a>Home</a>
                <a>Over ons</a>
                <a>Sitemap</a>
            </div>
            <div class="footer-column">
            </div>
            <div class="footer-column">
                <a>Mobiele website</a>
                <a>Help</a>
                <a>Contact</a>
            </div>
        </div>
    </footer>
</template>

<script>
export default {
    name: 'Footer'
}
</script>

<style scoped>

footer {
    position: absolute;
    bottom: 0;
    left: 0;
    height: var(--footer-height);
    width: 100%;
    background-color: var(--green);
    box-sizing: border-box;
    overflow: hidden;
    z-index: 100;
}

.footer-content {
    display: grid;
    position: relative;
    height: var(--footer-height);
    width: 500px;
    max-width: 94%;
    grid-template-columns: 1fr 1fr 1fr;
    grid-template-rows: 1fr;
  align-items: center;
    grid-column-gap: 20px;
    top: 0;
    left: 50%;
    transform: translateX(-50%);
}

.footer-column {
    align-self: center;
}

.footer-column a {
    display: block;
    color: var(--white-pure);
    font-size: 12pt;
    margin: 4px 2px;
    text-decoration: none;
    cursor: pointer;
}
</style>
