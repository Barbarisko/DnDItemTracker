<script>
export default {
    props: {
        title: String,
        charges: Array
    },
    emits: ["CheckBoxClick", "RestoreAll"],
    methods: {
        onCheckBoxClick(event) {
            this.$emit('CheckBoxClick', Number(event.target.id), event.target.checked);
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
        },
        restoreAll(event) {
            this.$emit('restoreAll');
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
                    <button type="button" class="btn btn-primary btn-sm" @click="useOneOf">
                        Use
                    </button>
                    <!-- <button type="button" class="btn btn-primary btn-sm" @click="restoreOneOf">
                        Restore
                    </button> -->
                    <button type="button" class="btn btn-success btn-sm" @click="restoreAll">
                        Restore All
                    </button>
                </div>
            </div>
        </div>

        <div class="row p-2 pt-0 form-check-inline">
            <input v-for="(charge, index) in charges" @change="onCheckBoxClick"
                class="ms-2 mt-2 form-check-input big-checkbox" type="checkbox" :id="index" value="" :checked="charge">
        </div>
    </div>
</template>

<style scoped></style>