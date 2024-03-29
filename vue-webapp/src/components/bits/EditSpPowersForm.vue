<script lang="ts">
import utils from '@/utils'
import sp_api from '@/apis/sp_api'
import type { PropType } from 'vue';
import type { SpecialPower } from '@/models/specialpower';
import * as bootstrap from 'bootstrap'

interface TempSP {
    id: number,
    name: string,
    charges: number,
    usedCharges: number,
}

export default {
    props: {
        title: String,
        form_id: String,
        ref_powers: Object as PropType<Array<SpecialPower>>,
        character_id: Number
    },
    emits: ["UpdatePowers"],
    data() {
        return {
            powers: Array<TempSP>()
        }
    },
    methods: {
        onDelete(index: number) {
            this.powers.splice(index, 1);
        },
        onAdd(event: any) {
            let new_el = {
                id: -1,
                name: "",
                charges: 1,
                usedCharges: 0
            } as TempSP;
            this.powers.push(new_el);
        },
        async onSave(event: any) {
            if (!this.ref_powers) return;
            this.powers.forEach(el => {
                if (el.usedCharges > el.charges) {
                    el.usedCharges = el.charges;
                }
            })

            var future_list = Array<any>();
            // delete removed levels
            const delete_list = this.ref_powers.filter((ref_element) => !this.powers.some((element) => element.id === ref_element.id));
            delete_list.forEach(el => future_list.push(sp_api.delete(el.id)))

            // update existing 
            const update_list = this.powers.filter((element) => element.id != -1);
            update_list.forEach(el => future_list.push(sp_api.set(el.id, el.name, el.charges, el.usedCharges)))

            // add new
            const add_list = this.powers.filter((element) => element.id == -1);
            add_list.forEach(el => future_list.push(sp_api.create(el.name, el.charges, el.usedCharges, this.character_id)))

            for (var i = 0; i < future_list.length; i++) {
                await future_list[i];
            }

            if (!this.form_id) return;
            const myModal = document.getElementById(this.form_id)
            if (myModal == null) return;
            var modal = bootstrap.Modal.getInstance(myModal)
            modal?.hide();
            this.$emit('UpdatePowers');
        }
    },
    watch: {
        ref_powers(newPowers: Array<SpecialPower>, oldPowers) {
            this.powers = []
            newPowers.forEach(el => {
                this.powers.push({
                    id: el.id,
                    name: el.name,
                    charges: el.charges.length,
                    usedCharges: utils.calculate_used_charges(el.charges)
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
                        <li class="list-group-item" v-for="(power, index) in powers" :key="index">
                            <form class="row ps-2 pe-2 needs-validation" novalidate>
                                <div class="col-6 fs-4 ps-0">

                                    <input v-model="power.name" type="text" class="form-control" id="name_validator"
                                        required>
                                    <div v-if="power.name == ''" class="invalid-feedback">
                                        Please provide a valid name.
                                    </div>
                                </div>
                                <div class="col-3">
                                    <input v-model="power.charges" min="1" type="number" id="typeNumber"
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
                            </form>
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