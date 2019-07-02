<template>
    <div class="welcome">
        <div class="wide-banner">
            <div class="banner-content">
                <div class="banner-text">
                    <span class="banner-title">Welkom bij <span class="logo-text">Project <span class="cursive-green">Planner</span></span></span>
                    <span class="banner-subtitle">De samenwerkingstool om de communicatie binnen je project naar het volgende level te tillen</span>
                    <div class="banner-actions">
                        <router-link to="/explore" class="banner-button">Ontdek Projecten</router-link>
                        <router-link to="/register" class="banner-button">Direct Aanmelden</router-link>
                    </div>
                </div>
            </div>
        </div>
        <div class="site-info">
            <div class="site-info-title">Voordelen</div>
            <div class="info-grid">                
                <div class="info-column">
                    <div class="info-column-title">Deel Ideeën</div>
                    <div class="info-column-content">Vindt de projecten die bij jou passen, en deel jouw beste ideeën met anderen. Project planner is het ideale platform om anderen op de hoogte te stellen van jouw beste werk.</div>
                </div>
                <div class="info-column">
                    <div class="info-column-title">Start conversaties</div>
                    <div class="info-column-content">Bereik nieuwe leden, start nieuwe gesprekken en bereik nieuwe hoogtes in jouw project. Het regelen van projecten is nog nooit zo makkelijk geweest.</div>
                </div>
                <div class="info-column">
                    <div class="info-column-title">Beheer leden</div>
                    <div class="info-column-content">Kies met wie jij je volgende grote klus gaat klaren, en stel het beste team samen voor jouw project. Project planner biedt de mogelijkheid om jouw projecten te beheren op de manier die jij wilt.</div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Welcome'
}
</script>

<style scoped>
.welcome {
    padding-top: 400px;
}

.wide-banner {
    position: absolute;
    height: 400px;
    width: 100vw;
    left: 50%;
    top: 0;
    transform: translateX(-50%);
    background-color: var(--black-smooth);
}

.banner-content {
    position: relative;
    width: 100vw;
    height: 400px;
    padding: 20px;
    box-sizing: border-box;
}

.banner-text {
    position: relative;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    text-align: center;
}

.cursive-green {
    font-weight: 700;
    font-style: italic;
    color: var(--green);
}

.logo-text {
    white-space: nowrap;
}

.banner-title {
    display: block;
    font-size: 32pt;
    color: var(--white-soft);
    margin-bottom: 5px;
    margin-top: 10px;
}

.banner-subtitle {
    font-size: 20pt;
    color: var(--gray-bright);
    font-weight: 300;
}

.banner-actions {
    display: block;
    text-align: center;
    margin-top: 16px;
}

.banner-button {
    display: inline-block;
    padding: 4px 16px 6px;
    background-color: var(--dark-green);
    color: var(--white-soft);
    font-size: 13pt;
    margin: 5px 10px;
    border-radius: 5px;
    cursor: pointer;
    user-select: none;
    -moz-user-select: -moz-none;
    text-decoration: none;
}

.banner-button:hover {
    background-color: var(--green);
}

.site-info {
    margin: 10px 0;
}

.site-info-title {
    text-align: center;
    font-size: 24pt;
    color: var(--black-mid);
    font-weight: 300;
}

.info-grid {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    width: 100%;
    grid-column-gap: 20px;
    margin: 20px 0;
}

.info-column {
    align-self: flex-start;
    margin: 10px 0;
}

.info-column-title {
    display: block;
    color: var(--green);
    font-size: 18pt;
    margin-bottom: 5px;
    font-weight: 600;
    text-align: center;
}

.info-column-content {
    color: var(--black-mid);
    text-align: center;
}


@media screen and (max-width: 600px) {
    .info-grid {
        grid-template-columns: 1fr;
    }


    .banner-title {
        font-size: 24pt;
    }

    .banner-subtitle {
        font-size: 16pt;
    }

    .banner-button:hover {
        background-color: var(--green);
    }
}

</style>
