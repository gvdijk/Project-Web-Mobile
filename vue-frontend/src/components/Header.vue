<template>
    <header>
        <div class="header-content">
            <div class="logo-wrapper">
                <router-link to="/"><img src="../assets/Logo_Full_White.svg" alt="logo"></router-link>
            </div>
            <div class="hamburger" v-bind:class="{'active-burger':menuCollapse}" @click="toggleMenu">
                <div class="top"></div>
                <div class="mid"></div>
                <div class="bot"></div>
            </div>
            <div class="search-wrapper">
                <i class="fa fa-search"></i>
                <input type="search" name="headerSearch" id="headerSearch" placeholder="Doorzoek de website">
            </div>
            <div class="account-wrapper">
                <router-link to="#"><a>Inloggen</a></router-link>
                <router-link to="/register"><a>Registreren</a></router-link>
            </div>
        </div>
    </header>
</template>

<script>
export default {
    name: 'Header',
    methods: {
        login() { },
        toggleMenu() { this.menuCollapse = !this.menuCollapse; }
    },
    data() {
        return {
            menuCollapse: true
        }
    }
}
</script>

<style scoped>
header {
    position: absolute;
    top: 0;
    left: 0;
    height: var(--header-height);
    width: 100vw;
    background-color: var(--black-soft);
    box-sizing: border-box;
    overflow: hidden;
    z-index: 100;
    user-select: none;
    -moz-user-select: -moz-none;
}

.header-content {
    display: grid;
    position: relative;
    height: var(--header-height);
    width: var(--max-width);
    max-width: 94%;
    grid-template-columns: 160px auto 180px;
    grid-column-gap: 10px;
    top: 0;
    left: 50%;
    transform: translateX(-50%);
}

.hamburger {
    display: none;
}

.logo-wrapper {
    position: relative;
    display: inline-block;
    height: var(--header-height);
    width: 100%;
    padding: 5px;
    box-sizing: border-box;
}

.logo-wrapper img {
    position: relative;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    max-width: 160px;
    max-height: 100%;
    cursor: pointer;
}

.search-wrapper {
    position: relative;
    margin: 5px;
    align-self: center;
}

.search-wrapper input {
    position: relative;
    width: 100%;
    height: 28px;
    padding: 4px 8px 4px 28px;
    box-sizing: border-box;
    border: 1px solid transparent;
    border-radius: 3px;
}

.search-wrapper input:focus {
    border: 1px solid var(--green);
}

.search-wrapper i {
    position: absolute;
    top: 50%;
    left: 0;
    transform: translateY(-50%);
    color: var(--gray-darker);
    z-index: 888;
    width: 16px;
    height: 16px;
    padding: 0 8px;
    box-sizing: border-box;
}

.account-wrapper {
    display: inline-block;
    align-self: center;
    white-space: nowrap;
}

.account-wrapper a {
    display: inline-block;
    padding: 5px;
    font-size: 15px;
    cursor: pointer;
    color: var(--white-pure);
    transition-duration: .1s;
    box-sizing: border-box;
}

.account-wrapper a:not(:first-child) {
    margin-left: 10px;
}

.account-wrapper a:hover {
    color: var(--green);
}

button:hover {
    background-color: var(--green);
}


@media screen and (max-width: 800px)  {
    .search-wrapper {}

    .header-content {
        display: block;
        height: var(--header-height);
        width: var(--max-width);
        max-width: 94%;
        top: 0;
        left: 50%;
        transform: translateX(-50%);
        align-content: center;
    }

    .hamburger {
        display: block;
        position: absolute;
        top: 50%;
        transform: translateY(-50%);
        right: 0;
        cursor: pointer;
    }

    .hamburger div {
        width: 25px;
        height: 3px;
        background-color: var(--white-soft);
        margin: 6px 0;
        opacity: 100;
        transition-duration: 0.2s;
    }

    .active-burger div {
        margin: -3px 0;
    }

    .active-burger .top {
        transform: rotate(-45deg);
    }

    .active-burger .mid {
        opacity: 0;
    }

    .active-burger .bot {
        transform: rotate(45deg);
    }
}

</style>
