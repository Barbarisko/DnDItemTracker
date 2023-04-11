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
            currentPath: window.location.hash,
            user: {
                id: -1,
                logged_in: false,
                name: "",
                selected_character:
                {
                    id: -1,
                    name: ""
                }
            }
        }
    },
    computed: {
        currentView() {
            if (!this.user.logged_in) {
                var prev_login = this.getUserIdCookie()
                if (prev_login.length) {
                    const cookieValue = prev_login[0].split("=")[1];
                    this.user.id = Number(cookieValue);
                    this.user.logged_in = true;
                    //get username
                }
            }
            if (!this.user.logged_in) {
                if (this.currentPath == '#/about') {
                    return About;
                }
                return Login;
            }
            if(this.user.selected_character.id < 0 && this.currentPath.slice(1) == '/character')
            {
                return Home;
            }
            return routes[this.currentPath.slice(1) || '/'] || Login;
        },
        user_character_title() {
            if (!this.user.logged_in)
                return "";

            if (this.user.selected_character == "")
                return this.user.name;

            return this.user.name + " and hero: " + this.user.selected_character.name;
        }
    },
    mounted() {
        window.addEventListener('hashchange', () => {
            this.currentPath = window.location.hash
        })
    },
    methods: {
        logOut() {
            this.user = {
                id: -1,
                logged_in: false,
                name: "",
                selected_character:
                {
                    id: -1,
                    name: ""
                }
            }
            this.delete_cookie("user_id");
        },
        getUserIdCookie() {
            return document.cookie.split(';').filter((item) => item.trim().startsWith('user_id='));
        },
        delete_cookie(name, path, domain) {
            document.cookie = name + "=" +
                ((path) ? ";path=" + path : "") +
                ((domain) ? ";domain=" + domain : "") +
                ";expires=Thu, 01 Jan 1970 00:00:01 GMT";
        },
        logIn(user_data) {
            var prev_login = this.getUserIdCookie();

            if (prev_login.length) {
                prev_login.forEach(element => {
                    this.delete_cookie("user_id");
                });
            }
            document.cookie = `user_id=${user_data.id}; ;max-age=max-age-in-seconds=${60 * 60 * 1};SameSite=Lax;`;

            this.user.id = user_data.id;
            this.user.logged_in = user_data.logged_in;
            this.user.name = user_data.name;

            window.location.hash = "#/home";
        },
        setCharacter(character) {
            this.user.selected_character.id = character.id;
            this.user.selected_character.name = character.name;
            window.location.hash = "#/character";
        }
    }
}
</script>

<template>
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
        <div class="container-fluid">
            <a class="navbar-brand" href="#/home">Home</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent"
                aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                    <li class="nav-item">
                        <a class="nav-link" href="#/about">About</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link disabled" href="#/dm-info">DM Info</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="https://send.monobank.ua/jar/2WeUR25CS3">Donate</a>
                    </li>
                </ul>
                <div class="d-flex">
                    <span class="navbar-text flex-grow-1">
                        {{ user_character_title }}
                    </span>

                    <a href="#/login" v-if="!user.logged_in" class="btn btn-outline-success ms-3" tabindex="-1"
                        role="button" @click="logOut" style="width: 90px;">Log In</a>
                    <a href="#/login" v-if="user.logged_in" class="btn btn-outline-danger ms-3" tabindex="-1" role="button"
                        @click="logOut" style="width: 90px;">Log Out</a>

                </div>
            </div>
        </div>
    </nav>

    <component :is="currentView" :user_id="user.id" :character_id="user.selected_character.id"
        v-on:setCharacter="setCharacter" v-on:setUser="logIn" />
</template>