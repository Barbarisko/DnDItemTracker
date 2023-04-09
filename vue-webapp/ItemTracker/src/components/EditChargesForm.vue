<script>
import utils from '@/utils'
import spell_api from '@/apis/spell_api'

export default {
    props: {
        title: String,
        form_id: String,
        ref_levels: Object,
        character_id: Number
    },
    emits: ["UpdateSpells"],
    data() {
        return {
            levels: []
        }
    },
    methods: {
        onDelete(index) {
            this.levels.splice(index, 1);
        },
        onAdd(event) {
            var new_el = {
                id: -1,
                level: -1,
                charges: 1,
                used_charges: 0
            }
            if (this.levels.length <= 0) {
                new_el.level = 1;
            }
            else {
                new_el.level = this.levels.at(-1).level + 1;
            }
            this.levels.push(new_el);
        },
        async onSave(event) {
            this.levels.forEach(el => {
                if (el.used_charges > el.charges) {
                    el.used_charges = el.charges;
                }
            })

            var future_list = []
            // delete removed levels
            const delete_list = this.ref_levels.filter((ref_element) => !this.levels.some((element) => element.id === ref_element.id));
            delete_list.forEach(el => future_list.push(spell_api.delete(el.id)))

            // update existing 
            const update_list = this.levels.filter((element) => element.id != -1);
            update_list.forEach(el => future_list.push(spell_api.set(el.id, el.level, el.charges, el.used_charges)))

            // add new
            const add_list = this.levels.filter((element) => element.id == -1);
            add_list.forEach(el => future_list.push(spell_api.create(el.level, el.charges, el.used_charges, this.character_id)))

            for (var i = 0; i < future_list.length; i++) {
                await future_list[i];
            }

            const myModal = document.getElementById(this.form_id)
            var modal = bootstrap.Modal.getInstance(myModal)
            modal.hide();
            this.$emit('UpdateSpells');
        },
        name(level) {
            return utils.intToRoman(level) + " Level"
        }
    },
    watch: {
        ref_levels(newLevels, oldLevels) {
            this.levels = []
            newLevels.forEach(el => {
                this.levels.push({
                    id: el.id,
                    level: el.level,
                    charges: el.charges.length,
                    used_charges: utils.calculate_used_charges(el.charges)
                })
            });
        }
    }
}
</script>

<template>
    <div class="modal fade" :id="form_id" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog modal-dialog-scrollable">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5"> Edit {{ title }}</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <ul class="pt-2 list-group">
                        <li class="list-group-item" v-for="(level, index) in this.levels" :key="index">
                            <div class="row ps-2 pe-2">
                                <div class="col-6 fs-4 ps-0">
                                    {{ name(level.level) }}
                                </div>
                                <div class="col-3">
                                    <input v-model="level.charges" min="1" type="number" id="typeNumber"
                                        class="form-control" />
                                </div>
                                <div class="col-3 pe-0 d-flex justify-content-end align-items-center">
                                    <div class="btn-group" role="group" aria-label="Basic example">
                                        <button type="button" class="btn btn-danger btn-sm" @click="onDelete(index)"
                                            style="wodth: 100px;">
                                            Delete
                                        </button>
                                    </div>
                                </div>
                            </div>
                        </li>
                        <li class="list-group-item">
                            <button type="button" class="btn btn-success" style="width: 100%;" @click="onAdd">
                                Add
                            </button>
                        </li>
                    </ul>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                    <button type="button" class="btn btn-primary" @click="onSave">Save changes</button>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped></style>