<script>

export default {
    props: {
        name: String,
        descr: String,
        amount: Number
    },
    emits: ["ChangeAmount", "DeleteItem", "DuplicateItem", "EditItem"],
    methods: {
        use(event) {
            if(this.amount <= 0)
                return
            this.$emit('ChangeAmount', -1)
        },
        add(event) {
            this.$emit('ChangeAmount', 1)
        }
    }
}
</script>

<template>
    <div class="row d-flex align-items-center">
        <div class="col-8 d-flex">
            <div class="fs-5 fw-semibold">
                {{ name }}
            </div>
            <span class="m-1 badge bg-secondary align-self-stretch">x{{ amount }}</span>
        </div>
        <div class="col-4 d-flex justify-content-end">
            <div class="btn-group" role="group" aria-label="Basic example">
                <button @click="use" type="button" class="btn btn-primary btn-sm" style="width: 40px">-</button>
                <button @click="add" type="button" class="btn btn-primary btn-sm" style="width: 40px">+</button>
            </div>
        </div>
    </div>
    <div class="row m-2 d-flex align-items-center">
        <small class="col">
            {{ descr }}
        </small>
    </div>

    <div class="row m-1 justify-content-end">
        <div class="col-lg-4 col-9 btn-group" role="group" aria-label="Basic mixed styles example">
            <button @click="$emit('DeleteItem')" type="button" class="btn btn-danger">Delete</button>
            <button type="button" class="btn btn-primary">Edit</button>
            <button @click="() => $emit('DuplicateItem')" type="button" class="btn btn-success">Duplicate</button>
        </div>
    </div>
</template>

<style scoped></style>