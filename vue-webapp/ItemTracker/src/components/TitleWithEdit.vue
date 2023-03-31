<script>
export default {
  props: {
    title: String
  },
  emits: ["ItemEdited"]
}

</script>

<template>
    <div class="container">
        <div class="row border rounded bg-light-subtle">
            <div class="col-8 fs-2 fw-semibold">
                {{ title }}
            </div>
            <div class="col-4 d-flex justify-content-end align-items-center">
                <button type="button" class="btn btn-outline-primary btn-sm">Edit</button>
            </div>
        </div>
    </div>
</template>

<style scoped>
</style>