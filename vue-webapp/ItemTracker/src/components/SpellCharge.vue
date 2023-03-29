<script>
export default {
    props: {
        title: String,
        charges: Array
    }
}
</script>

<template>
    <div class="row ps-3">
        <div class="row pe-0">
            <div class="col-6 fs-4 ps-0">
                {{ title }}
            </div>
            <div class="col-6 pe-0 d-flex justify-content-end align-items-center">
                <div class="btn-group" role="group" aria-label="Basic example">
                    <button type="button" class="btn btn-primary btn-sm">Restore</button>
                    <button type="button" class="btn btn-success btn-sm">Use</button>
                </div>
            </div>
        </div>

        <div class="row p-2 pt-0 form-check-inline">
            <input v-for="charge in charges" 
            class="ms-2 mt-2 form-check-input big-checkbox" type="checkbox"
                id="inlineCheckbox1" value=""
                :checked="charge">
        </div>
    </div>
</template>

<style scoped></style>