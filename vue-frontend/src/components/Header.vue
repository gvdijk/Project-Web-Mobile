<template>
    <header>
        <div class="header-content">
            <div class="logo-wrapper">
                <router-link to="/"><img src="../assets/Logo_Full_White.svg" alt="logo"></router-link>
            </div>
            <div class="search-wrapper">
                <i class="fa fa-search"></i>
                <input type="search" name="headerSearch" v-model="searchQuery" placeholder="Doorzoek de website">
            </div>
            <div class="search-filler"></div>
            <div class="account-wrapper">
                <span class="account-label search-label" @click="toggleSearch"><i class="fa fa-search"></i><span>Zoeken</span></span>
                <span v-if="!authenticated" class="account-label" @click="$emit('requestModal', 'login', {})" title="Inloggen"><i class="fa fa-sign-in"></i><span>Inloggen</span></span>
                <router-link v-if="authenticated" class="account-label" to="/profile" title="Profiel"><i class="fa fa-user"></i><span>Profiel</span></router-link>
                <span v-if="authenticated" class="account-label" @click="logout" title="Uitloggen"><i class="fa fa-sign-out"></i><span>Uitloggen</span></span>
                <router-link v-if="!authenticated" class="account-label" to="/register" title="Registreren"><i class="fa fa-paper-plane"></i><span>Registreren</span></router-link>
            </div>
        </div>
        <div class="mobile-search-wrapper" v-bind:class="{ 'mobile-search-expanded': searchExpanded }">
            <div class="mobile-search">
                <i class="fa fa-search"></i>
                <input type="search" name="headerSearch" v-model="searchQuery" placeholder="Doorzoek de website">
            </div>
        </div>
    </header>
</template>

<script>
export default {
    name: 'Header',
    methods: {
        login() { },
        toggleMenu() { this.menuCollapse = !this.menuCollapse; },
        logout() {
            this.$store.dispatch('logoutUser');
            this.$router.push({path: '/'});
        },
        toggleSearch() { this.searchExpanded = !this.searchExpanded; }
    },
    data() {
        return {
            menuCollapse: true,
            searchQuery: "",
            searchExpanded: false
        }
    },
    computed: {
        authenticated(){
            return this.$store.getters.authenticated;
        },
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
    grid-template-columns: 160px auto 140px;
    grid-column-gap: 10px;
    top: 0;
    left: 50%;
    transform: translateX(-50%);
    text-align: right;
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

.account-label {
    display: inline-block;
    padding: 5px;
    font-size: 15px;
    cursor: pointer;
    color: var(--white-pure);
    transition-duration: .1s;
    box-sizing: border-box;
    text-decoration: none;
}

.search-label {
    display: none;
}

.search-filler {
    display: none;
}

.account-label:not(:first-child) {
    margin-left: 10px;
}

i {
    width: 20px;
    height: 20px;
    font-size: 14pt;
    color: var(--white-soft);
    display: block;
    text-align: center;
    width: 100%;
}

.account-label span {
    display: block;
    font-size: 8pt;
    font-weight: 500;
    text-align: center;
}

.account-label:hover i,
.account-label:hover span {
    color: var(--green);
}

button:hover {
    background-color: var(--green);
}

.mobile-search-wrapper {
    display: none;
    position: absolute;
    right: 0;
    top: var(--header-height);
    background-color: var(--black-soft);
    width: 70vw;
    height: 0px;
    padding: 0 10px;
    box-sizing: border-box;
    border-bottom-left-radius: 5px;
    overflow: hidden;
    transition-duration: 0.2s;
}

.mobile-search {
    position: relative;
    align-self: center;
}

.mobile-search i {
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

.mobile-search input {
    position: relative;
    width: 100%;
    height: 28px;
    padding: 4px 8px 4px 28px;
    box-sizing: border-box;
    border: 1px solid transparent;
    border-radius: 3px;
}

.mobile-search-expanded {
    height: 37px;
}


@media screen and (max-width: 800px)  {
    .search-wrapper {
        position: absolute;
        display: none;
    }

    .search-label {
        display: inline-block;
    }

    .search-filler {
        display: block;
    }

    .header-content {
        grid-template-columns: 160px auto 190px;
    }

    .mobile-search-wrapper {
        display: block;
    }

}

</style>
