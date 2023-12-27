<script lang="ts">
import { useUserStore } from './stores/user-session'

import * as SESSION from './logic/login'

export default {
    data() {
        return {
            userSession: useUserStore()
        }
    },
    computed: {
        user_character_title() {
            if (!this.userSession.loggedIn)
                return "";

            if (this.userSession.selectedCharacter.name == "")
                return this.userSession.name;

            return this.userSession.name + " and hero: " + this.userSession.selectedCharacter.name;
        }
    },
    methods: {
        logOut() {
            SESSION.logOut();
        },

        // logIn(user_data) {
        //     SESSION.logIn({
        //         id: user_data.id,
        //         loggedIn: user_data.logged_in,
        //         name: user_data.name,
        //         selectedCharacter: { id: -1, name: "" }
        //     });
        // }
    },
    mounted() {
        try {
            SESSION.restoreUser();
        }
        catch (e) { }
    }
}
</script>

<template>
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
        <div class="container-fluid">
            <RouterLink class="navbar-brand" to="/home">Home</RouterLink>

            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent"
                aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                    <li class="nav-item">
                        <RouterLink class="nav-link" to="/about">About</RouterLink>

                    </li>
                    <li class="nav-item">
                        <RouterLink class="nav-link" to="/dm-info">DM Info</RouterLink>

                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="https://send.monobank.ua/jar/2WeUR25CS3">Donate</a>
                    </li>
                </ul>
                <div class="d-flex">
                    <span class="navbar-text flex-grow-1">
                        {{ user_character_title }}
                    </span>

                    <a href="/login" v-if="!userSession.loggedIn" class="btn btn-outline-success ms-3" tabindex="-1"
                        role="button" @click="logOut" style="width: 90px;">Log In</a>
                    <a href="/login" v-if="userSession.loggedIn" class="btn btn-outline-danger ms-3" tabindex="-1"
                        role="button" @click="logOut" style="width: 90px;">Log Out</a>

                </div>
            </div>
        </div>
    </nav>
    <RouterView />
</template>