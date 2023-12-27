<script>
import Artifacts from '@/components/Artifacts.vue'
import artifact_api from '@/apis/artifact_api'

export default {
    components: {
        Artifacts
    },
    props: {
        form_id: String,
        has_charges: {
            type: Boolean,
            default: false
        }
    },
    emits: ["NewItem"],
    data() {
        return {
            item_name: "",
            item_descr: "",
            item_amount: 1,

            invalid_name: false
        }
    },
    methods: {
        validate(event) {
            if (this.item_name == "") {
                this.invalid_name = true
                return
            }
            else
                this.invalid_name = false

            this.$emit('NewItem', {
                name: this.item_name,
                descr: this.item_descr,
                amount: this.has_charges ? undefined : Number(this.item_amount),
                charges: this.has_charges ? Number(this.item_amount) : undefined
            });

            const myModal = document.getElementById(this.form_id)
            var modal = bootstrap.Modal.getInstance(myModal)
            modal.hide();
            this.reset()
        },

        reset() {
            this.item_name = "";
            this.item_descr = "";
            this.item_amount = 1;
        }
    }
}
</script>

<template>
    <!-- Modal -->
    <div class="modal fade" :id=form_id tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="exampleModalLabel">Add new item</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <form class="needs-validation was-validated" novalidate="">
                        <div class="mb-3">
                            <label for="NameInput" class="form-label">Name</label>
                            <input :value="item_name" @input="event => item_name = event.target.value" type="text"
                                class="form-control" id="NameInput" aria-describedby="emailHelp" required="" />
                            <div v-if="invalid_name" class="invalid-feedback">I need nonempty name</div>
                        </div>
                        <div class="mb-3">
                            <label for="descriptionTextAria" class="form-label">Description</label>
                            <textarea :value="item_descr" @input="event => item_descr = event.target.value"
                                class="form-control" placeholder="Some text to remember what it does"
                                id="descriptionTextAria" style="height: 100px"></textarea>
                        </div>
                        <div class="mb-3">
                            <template v-if="has_charges">
                                <label class="form-label" for="typeNumber">Charges</label>
                                <input :value="item_amount" @input="event => item_amount = event.target.value" min="1"
                                    type="number" id="typeNumber" class="form-control" />
                            </template>

                            <template v-else>
                                <label class="form-label" for="typeNumber">Amount</label>
                                <input :value="item_amount" @input="event => item_amount = event.target.value" min="0"
                                    type="number" id="typeNumber" class="form-control" />
                            </template>
                        </div>
                    </form>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                    <button @click="validate" type="button" class="btn btn-primary">Add</button>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped></style>