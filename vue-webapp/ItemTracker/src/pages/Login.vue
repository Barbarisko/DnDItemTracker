<script>
import user_api from '@/apis/user_api'

export default {

    data() {
        return {
            registerMode: false,
            username: "",
            password: ""
        }
    },
    methods: {
        onChangeMode(event) {
            if (event.target.id == "modeLogin") {
                this.registerMode = false;
            }
            else {
                this.registerMode = true;
            }
        },
        async onGo() {
            if (this.username == "" || this.password == "")
            //give some error
                return;

            async function sha256(message) {
                // encode as UTF-8
                const msgBuffer = new TextEncoder().encode(message);                    

                // hash the message
                const hashBuffer = await crypto.subtle.digest('SHA-256', msgBuffer);

                // convert ArrayBuffer to Array
                const hashArray = Array.from(new Uint8Array(hashBuffer));

                // convert bytes to hex string                  
                const hashHex = hashArray.map(b => b.toString(16).padStart(2, '0')).join('');
                return hashHex;
            }
            var pwd_hash = await sha256(this.password)

            var res = await (this.registerMode ? user_api.create(this.username, pwd_hash) : user_api.login(this.usernamem, pwd_hash));

            if (res.status) {
                this.$root.user.id = res.new_id;
                this.$root.user.logged_in = true;
                this.$root.user.name = this.username;
                window.location.hash = "#/home"
            }
            else {
                            //give some error

                return;
            }
        }
    }
}
</script>

<template>
    <div class="row align-items-center mt-5">
        <div class="container">
            <div class="row justify-content-center">
                <div class="col-sm-10 col-md-8 col-lg-6 btn-group" role="group"
                    aria-label="Basic radio toggle button group">
                    <input type="radio" class="btn-check" name="btnradio" id="modeLogin" autocomplete="off"
                        @change="onChangeMode" checked>
                    <label class="btn btn-outline-primary" for="modeLogin">
                        <h4>Login</h4>
                    </label>

                    <input type="radio" class="btn-check" name="btnradio" id="modeRegister" autocomplete="off"
                        @change="onChangeMode">
                    <label class="btn btn-outline-primary" for="modeRegister">
                        <h4>Register</h4>
                    </label>
                </div>
            </div>
            <div class="row justify-content-center">
                <div class="col-sm-10 col-md-8 col-lg-6 pt-4">

                    <div class="input-group mb-3">
                        <span class="input-group-text">@</span>
                        <div class="form-floating">
                            <input type="text" class="form-control" id="floatingInputGroup1" placeholder="Username"
                                v-model="username">
                            <label for="floatingInputGroup1">Username</label>
                        </div>
                    </div>

                    <div class="input-group mb-3">
                        <span class="input-group-text" style="width: 42px;">*</span>
                        <div class="form-floating">
                            <input type="text" class="form-control" id="floatingInputGroup1" placeholder="Password"
                                v-model="password">
                            <label for="floatingInputGroup1">Password</label>
                        </div>
                    </div>

                    <div v-if="registerMode" class="input-group mb-3">
                        <span class="input-group-text" style="width: 42px;">*</span>
                        <div class="form-floating">
                            <input type="text" class="form-control" id="floatingInputGroup1" placeholder="Password">
                            <label for="floatingInputGroup1">Repeate Password</label>
                        </div>
                    </div>

                </div>
            </div>
            <div class="row justify-content-center">
                <div class="col-4 mt-4 position-relative">
                    <button type="button" class="btn btn-primary position-absolute start-50 translate-middle fs-4"
                        style="width: 200px;" @click="onGo">
                        Go!
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>

<style></style>