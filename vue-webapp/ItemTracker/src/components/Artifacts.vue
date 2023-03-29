<script>

export default {
    props: {
        name: String,
        descr: String,
        charges: Array
    }
}
</script>

<template>
    <div class="row">
        <div class="col-8">
            <h5 class="p-1"> {{ name }} </h5>
        </div>
        <div class="col-4 d-flex justify-content-end">
            <button type="button" class="btn btn-outline-danger btn-sm align-self-center">
                Reset All
            </button>
        </div>
    </div>
    <div class="row m-1 d-flex align-items-center">
        <small class="col">
            {{ descr }}
        </small>
    </div>
    <div class="row ps-2 pb-2 form-check-inline">
        <input v-for="charge in charges"
         class="ms-2 mt-2 form-check-input big-checkbox" 
         type="checkbox" id="inlineCheckbox1" value=""
         :checked="charge">
    </div>
</template>

<style scoped></style>