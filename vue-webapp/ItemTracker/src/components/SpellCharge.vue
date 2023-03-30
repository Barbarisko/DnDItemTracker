<script>
export default {
    props: {
        title: String,
        charges: Array
    },
    methods: {
        onCheckBoxClick(event) {
            this.$emit('CheckBoxClick', event.target.id, event.target.checked);
        },
        useOneOf(event) {
            var index = this.charges.findIndex(el => !el);
            if (index == -1) {
                return;
            }
            this.$emit('CheckBoxClick', index, true);
        },
        restoreOneOf(event) {
            var index = this.charges.findLastIndex(el => el);
            if (index == -1) {
                return;
            }
            this.$emit('CheckBoxClick', index, false);
        }
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
                    <button type="button" class="btn btn-primary btn-sm" @click="restoreOneOf">
                        Restore
                    </button>
                    <button type="button" class="btn btn-success btn-sm" @click="useOneOf">
                        Use
                    </button>
                </div>
            </div>
        </div>

        <div class="row p-2 pt-0 form-check-inline">
            <input v-for="(charge, index) in charges" :key="index" @click="onCheckBoxClick"
                class="ms-2 mt-2 form-check-input big-checkbox" type="checkbox" :id="index" value="" :checked="charge">
        </div>
    </div>
</template>

<style scoped></style>