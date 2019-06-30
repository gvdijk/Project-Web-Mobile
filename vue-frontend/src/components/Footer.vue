<template>
    <footer>
        <div class="footer-filler">
            <div class="footer-content">
                <div class="logo-wrapper">
                    <img src="../assets/Logo_Full_White.svg" alt="logo">
                </div>
                <span class="footer-message">Project Planner &#9400;2019</span>
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
    width: 100vw;
    overflow: hidden;
    z-index: 100;
    user-select: none;
    -moz-user-select: -moz-none;
}

.footer-filler {
    position: relative;
    height: var(--footer-height);
    width: 100%;
    background-color: var(--black-soft);
    border-top: 20px solid var(--green);
    box-sizing: border-box;
}

.footer-content {
    display: grid;
    position: relative;
    height: 100%;
    width: 600px;
    max-width: 80%;
    grid-template-columns: 1fr;
    grid-template-rows: 2fr 1fr;
    align-items: center;
    grid-column-gap: 50px;
    top: 0;
    left: 50%;
    transform: translateX(-50%);
    padding: 30px 0;
    box-sizing: border-box;
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
    transition-duration: 0.1s;
}

.footer-column a:hover {
    color: var(--green);
}

.logo-wrapper {
    position: relative;
    display: inline-block;
    height: 70px;
    width: 100%;
    padding: 5px;
    box-sizing: border-box;
}

.logo-wrapper img {
    position: relative;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    max-width: 280px;
    max-height: 100%;
    cursor: pointer;
}

.footer-message {
    color: var(--white-soft);
    font-size: 13pt;
    font-weight: 300;
    display: block;
    width: 100%;
    text-align: center;
}
</style>
