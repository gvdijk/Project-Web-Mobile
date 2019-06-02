<template>
    <header>
        <div class="header-content">
            <div class="logo-wrapper">
                <img @click="home" src="https://via.placeholder.com/80x40.png?text=Logo%20Naam" alt="logo">
            </div>
            <div class="search-wrapper">
                <i class="fa fa-search"></i>
                <input type="search" name="headerSearch" id="headerSearch" placeholder="Doorzoek de website">
            </div>
            <div class="account-wrapper">
                <a @click="login">Inloggen</a>
                <a @click="register">Registreren</a>
            </div>
        </div>
    </header>
</template>

<script>
export default {
    name: 'Header',
    methods: {
        login() {

        },
        register() {
            this.$router.push({
                path: '/register'
            });
        },
        home() {
            this.$router.push({
                path: '/'
            });
        }
    },
}
</script>

<style scoped>
header {
    position: absolute;
    top: 0;
    left: 0;
    height: var(--header-height);
    width: 100%;
    background-color: var(--black-soft);
    box-sizing: border-box;
    overflow: hidden;
    z-index: 100;
}

.header-content {
    display: grid;
    position: relative;
    height: var(--header-height);
    width: var(--max-width);
    max-width: 94%;
    grid-template-columns: 80px auto 150px;
    grid-column-gap: 20px;
    top: 0;
    left: 50%;
    transform: translateX(-50%);
}

.logo-wrapper {
    position: relative;
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
    max-width: 100%;
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
    border: 2px solid transparent;
}

.search-wrapper input:focus {
    border: 2px solid var(--green);
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
    /*
    font-weight: bold;
    min-width: 60px;
    background-color: var(--dark-green);
    border-radius: 3px;
    */
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

</style>
