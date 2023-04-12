<script>
import artifact_api from '../apis/artifact_api';


export default {
    props: {
        name: String,
        descr: String,
        charges: Array
    },
    emits: ["CheckBoxClick", "restoreAll", "remove"],
    methods: {
        onCheckBoxClick(event) {
            this.$emit('CheckBoxClick', event.target.id, event.target.checked);
        },
        restoreAll(event) {
            this.$emit('restoreAll');
        },
        useOneOf(event) {
            var index = this.charges.findIndex(el => !el);
            if (index == -1) {
                return;
            }
            this.$emit('CheckBoxClick', index, true);
        },
        restoreAll(event) {
            this.$emit('restoreAll');
        },
        remove(event) {
            this.$emit('remove');
        }
    }
}
</script>

<template>
    <div class="row">
        <div class="col-6">
            <h5 class="p-1"> {{ name }} </h5>
        </div>
        <div class="col-6 d-flex justify-content-end align-items-center">
            <div class="btn-group" role="group" aria-label="Basic example">
                <button type="button" class="btn btn-primary btn-sm" @click="useOneOf">
                    Use
                </button>
                <!-- <button type="button" class="btn btn-primary btn-sm" @click="restoreOneOf">
                            Restore
                        </button> -->
                <button type="button" class="btn btn-success btn-sm" @click="restoreAll">
                    Restore All
                </button>
                <button @click="remove" type="button" class="btn btn-danger btn-sm" style="width: 40px">
                    <i class="bi bi-trash3"></i>
                </button>
            </div>
        </div>
    </div>
    <div class="row m-1 d-flex align-items-center">
        <small class="col">
            {{ descr }}
        </small>
    </div>
    <div class="row ps-2 pb-2 form-check-inline">
        <input v-for="(charge, index) in charges" :key="index" @click="onCheckBoxClick"
            class="ms-2 mt-2 form-check-input big-checkbox" type="checkbox" :id="index" value="" :checked="charge">
    </div>
</template>

<style scoped></style>