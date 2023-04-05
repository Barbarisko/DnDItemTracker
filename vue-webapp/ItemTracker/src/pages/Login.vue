<template>
    <div class="row align-items-center mt-5">
        <div class="container">

            <div class="row justify-content-center">
                <div class="col-sm-10 col-md-8 col-lg-6 btn-group" role="group" aria-label="Basic radio toggle button group">
                    <input type="radio" class="btn-check" name="btnradio" id="btnradio1" autocomplete="off" checked>
                    <label class="btn btn-outline-primary" for="btnradio1">
                        <h4>Login</h4>
                    </label>

                    <input type="radio" class="btn-check" name="btnradio" id="btnradio2" autocomplete="off">
                    <label class="btn btn-outline-primary" for="btnradio2">
                        <h4>Register</h4>
                    </label>
                </div>
            </div>
            <div class="row justify-content-center">
                <div class="col-sm-10 col-md-8 col-lg-6 pt-4">
                    <div class="input-group mb-3">
                        <span class="input-group-text" style="width: 42px;">@</span>
                        <div class="form-floating">
                            <input type="text" class="form-control" id="username" placeholder="Username">
                            <label for="floatingInputGroup1">Username</label>
                        </div>
                    </div>

                    <div class="input-group mb-3">
                        <span class="input-group-text " style="width: 42px;">
                            <h2> * </h2>
                        </span>
                        <div class="form-floating">
                            <input type="text" class="form-control" id="password" placeholder="Password">
                            <label for="floatingInputGroup1">Password</label>
                        </div>
                    </div> 

                    <div class="input-group mb-3">
                        <span class="input-group-text">*</span>
                        <div class="form-floating">
                            <input type="text" class="form-control" id="floatingInputGroup1" placeholder="Username">
                            <label for="floatingInputGroup1">Username</label>
                        </div>
                    </div>

                    <div class="input-group mb-3">
                        <span class="input-group-text">*</span>
                        <div class="form-floating">
                            <input type="text" class="form-control" id="floatingInputGroup1" placeholder="Username">
                            <label for="floatingInputGroup1">Username</label>
                        </div>
                    </div>

                </div>
            </div>
            <div class="row justify-content-center">
                <div class="col-4 mt-4 position-relative">
                    <button type="button" class="btn btn-primary position-absolute start-50 translate-middle"
                        style="width: 200px;">
                        <h5>Go!</h5>
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>

<style></style>