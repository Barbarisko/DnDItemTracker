<script  lang="ts">
import user_api from '@/apis/user_api'
import utils from '@/utils'
import * as SESSION from '../logic/login'

export default {
    data() {
        return {
            registerMode: false,
            username: "",
            password: "",
            repeatPassword: "",
            showHint: false,
            hintMessage: "",
        }
    },
    methods: {
        onChangeMode(event: any) {
            if (event.target.id == "modeLogin") {
                this.registerMode = false;
            }
            else {
                this.registerMode = true;
            }
        },
        async onGo() {
            this.showHint = false;
            this.hintMessage = "Undefined Error occured";
            if (this.username == "" || this.password == "")
                //give some error
                return;
            this.username.replace(/^\s\s*/, '').replace(/\s\s*$/, '');

            var pwd_hash = await utils.sha256(this.password)

            var res = await (this.registerMode ? user_api.create(this.username, pwd_hash) : user_api.login(this.username, pwd_hash));

            if (res.status) {
                SESSION.logIn({
                    id: res.new_id,
                    loggedIn: true,
                    name: this.username,
                    selectedCharacter: { id: -1, name: "", className: "", level: -1 }
                });
                this.$router.push('Home')
            }
            else {
                //give some error
                this.showHint = true;
                this.hintMessage = res.message.length > 0 ? res.message : this.hintMessage;
                return;
            }
        }
    },
    computed: {
        canLogin() {
            return this.username != "" && this.password != "" && (
                this.registerMode ? this.password == this.repeatPassword : true
            )
        }
    }
}
</script>

<template>
    <div class="row align-items-center mt-5">
        <div class="container">
            <div class="row justify-content-center">
                <div class="col-sm-12 col-md-8 col-lg-6">
                    <div class="btn-group ps-4 pe-4" style="width: 100%;" role="group"
                        aria-label="Basic radio toggle button group">
                        <input type="radio" class="btn-check" name="btnradio" id="modeLogin" autocomplete="off"
                            @change="onChangeMode" checked>
                        <label class="btn btn-outline-primary fs-4" for="modeLogin">
                            Login
                        </label>

                        <input type="radio" class="btn-check" name="btnradio" id="modeRegister" autocomplete="off"
                            @change="onChangeMode">
                        <label class="btn btn-outline-primary fs-4" for="modeRegister">
                            Register
                        </label>
                    </div>
                </div>
            </div>
            <div class="row justify-content-center mt-4">
                <div class="col-sm-10 col-md-8 col-lg-6">

                    <div class="input-group ps-4 pe-4">
                        <span class="input-group-text">@</span>
                        <div class="form-floating">
                            <input type="text" class="form-control" id="floatingInputGroup1" placeholder="Username"
                                v-model="username">
                            <label for="floatingInputGroup1">Username</label>
                        </div>
                    </div>

                    <div class="input-group ps-4 pe-4 mt-2">
                        <span class="input-group-text" style="width: 42px;">*</span>
                        <div class="form-floating">
                            <input type="password" class="form-control" id="floatingInputGroup1" placeholder="Password"
                                v-model="password">
                            <label for="floatingInputGroup1">Password</label>
                        </div>
                    </div>

                    <div v-if="registerMode" class="input-group ps-4 pe-4 mt-2">
                        <span class="input-group-text" style="width: 42px;">*</span>
                        <div class="form-floating">
                            <input type="password" v-model="repeatPassword" class="form-control" id="floatingInputGroup1"
                                placeholder="Password">
                            <label for="floatingInputGroup1">Repeat Password</label>
                        </div>
                    </div>

                    <div v-if="showHint" class="ps-4 pe-4 mt-3 text-center text-danger">
                        {{ hintMessage }}
                    </div>

                </div>
            </div>
            <div class="row justify-content-center mt-3">
                <div class="col-4 mt-4 position-relative">
                    <button type="button" class="btn btn-primary position-absolute start-50 translate-middle fs-4"
                        :disabled="!canLogin" style="width: 200px;" @click="onGo">
                        Go!
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>

<style></style>