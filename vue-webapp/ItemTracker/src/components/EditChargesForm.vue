<script>
import utils from '@/utils'

export default {
    props: {
        title: String,
        form_id: String,
        ref_levels: Object
    },
    emits: ["NewItem"],
    data() {
        return {
            // levels: []
        }
    },
    methods: {

    },
    computed: {
        levels() {
            debugger
            var res = []
            this.ref_levels.forEach(el => {
                res.push({
                    id: el.id,
                    name: utils.intToRoman(el.level) + " Level",
                    charges: el.charges.length,
                    used_charges: utils.calculate_used_charges(el.charges)
                })
            })
            return res
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
                                <div class="col-4 fs-4 ps-0">
                                    {{ level.name }}
                                </div>
                                <div class="col-4">
                                    <input :value="item_amount" min="1" type="number" id="typeNumber" class="form-control" />
                                </div>
                                <div class="col-4 pe-0 d-flex justify-content-end align-items-center">
                                    <div class="btn-group" role="group" aria-label="Basic example">
                                        <button type="button" class="btn btn-primary btn-sm" @click="useOneOf">
                                            Use
                                        </button>
                                        <button type="button" class="btn btn-danger btn-sm" @click="">
                                            Delete
                                        </button>
                                    </div>
                                </div>
                            </div>
                        </li>
                        <li class="list-group-item">
                            <button type="button" class="btn btn-success" style="width: 100%;">
                            Add
                        </button>
                        </li>
                    </ul>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                    <button type="button" class="btn btn-primary">Save changes</button>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped></style>