<script>

export default {
    props: {
        name: String,
        descr: String,
        amount: Number
    },
    emits: ["ChangeAmount", "Delete"],
    methods: {
        use(event) {
            if(this.amount <= 0)
                return
            this.$emit('ChangeAmount', -1)
        },
        add(event) {
            this.$emit('ChangeAmount', 1)
        },
        remove() {
            this.$emit('Delete') 
        }
    }
}
</script>

<template>
    <div class="row d-flex align-items-center">
        <div class="col-7 d-flex">
            <div class="fs-5 fw-semibold text-break">
               {{ name }} 
            </div>
            <span class="m-1 badge bg-secondary align-self-stretch">x{{ amount }}</span>
        </div>
        <div class="col-5 d-flex justify-content-end">
            <div class="btn-group" role="group" aria-label="Basic example">
                <button @click="use" type="button" class="btn btn-primary btn-sm" style="width: 40px">-</button>
                <button @click="add" type="button" class="btn btn-primary btn-sm" style="width: 40px">+</button>
                <button @click="remove" type="button" class="btn btn-danger btn-sm" style="width: 40px">
                    <i class="bi bi-trash3"></i>
                </button>
            </div>
        </div>
    </div>
    <div class="row mt-1 mb-1 d-flex align-items-center">
        <small class="col ms-3">
            {{ descr }}
        </small>
    </div>
</template>

<style scoped></style>