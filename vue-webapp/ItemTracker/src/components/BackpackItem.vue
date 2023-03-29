<script>

export default {
    props: {
        name: String,
        descr: String,
        amount: Number
    }
}
</script>

<template>
    <div class="row d-flex align-items-center">
        <div class="col-8 d-flex">
            <div class="fs-5 fw-semibold">
                {{ name }}
            </div>
            <span class="m-1 badge bg-secondary align-self-stretch">x{{ amount }}</span>
        </div>
        <div class="col-4 d-flex justify-content-end">
            <div class="btn-group" role="group" aria-label="Basic example">
                <button type="button" class="btn btn-primary btn-sm" style="width: 40px">+</button>
                <button type="button" class="btn btn-primary btn-sm" style="width: 40px">-</button>
            </div>
        </div>
    </div>
    <div class="row m-2 d-flex align-items-center">
        <small class="col">
            {{ descr }}
        </small>
    </div>

    <div class="row m-1 justify-content-end">
        <div class="col-lg-4 col-9 btn-group" role="group" aria-label="Basic mixed styles example">
            <button type="button" class="btn btn-danger">Delete</button>
            <button type="button" class="btn btn-primary">Edit</button>
            <button type="button" class="btn btn-success">Duplicate</button>
        </div>
    </div>
</template>

<style scoped></style>