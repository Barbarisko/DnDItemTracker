<script>
import Login from './pages/Login.vue'
import About from './pages/About.vue'
import Character from './pages/Character.vue'
import Home from './pages/Home.vue'

const routes = {
    '/': Login,
    '/home': Home,
    '/login': Login,
    '/character': Character,
    '/about': About
}

export default {
    data() {
        return {
            currentPath: window.location.hash
        }
    },
    computed: {
        currentView() {
            return routes[this.currentPath.slice(1) || '/'] || Login
        }
    },
    mounted() {
        window.addEventListener('hashchange', () => {
            this.currentPath = window.location.hash
        })
    }
}
</script>

<template>
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
        <div class="container-fluid">
            <a class="navbar-brand" href="#/home">Home</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav"
                aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse d-flex" id="navbarNav">
                <ul class="navbar-nav flex-grow-1">
                    <li class="nav-item">
                        <a class="nav-link" href="#/about">About</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link disabled" href="#/dm-info">DM Info</a>
                    </li>
                    <li class="nav-item ms-auto">
                        <a class="nav-link " href="#/login">Log In</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#/login">Log Out</a>
                    </li>
                </ul>

            </div>
        </div>
    </nav>

    <component :is="currentView" />
</template>