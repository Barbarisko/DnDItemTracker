<script>
import user_api from '@/apis/user_api'
import utils from '@/utils'

export default {
    emits: ["setUser"],
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

            var pwd_hash = await utils.sha256(this.password)

            var res = await (this.registerMode ? user_api.create(this.username, pwd_hash) : user_api.login(this.username, pwd_hash));
            
            if (res.status) {
                this.$emit('setUser', 
                {
                    id: res.new_id,
                    logged_in: true,
                    name: this.username
                })
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
                <div class="col-sm-12 col-md-8 col-lg-6">
                    <div class="btn-group ps-4 pe-4" style="width: 100%;" role="group" aria-label="Basic radio toggle button group">
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
                            <input type="text" class="form-control" id="floatingInputGroup1" placeholder="Password"
                                v-model="password">
                            <label for="floatingInputGroup1">Password</label>
                        </div>
                    </div>

                    <div v-if="registerMode" class="input-group ps-4 pe-4 mt-2">
                        <span class="input-group-text" style="width: 42px;">*</span>
                        <div class="form-floating">
                            <input type="text" class="form-control" id="floatingInputGroup1" placeholder="Password">
                            <label for="floatingInputGroup1">Repeate Password</label>
                        </div>
                    </div>

                </div>
            </div>
            <div class="row justify-content-center mt-4">
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