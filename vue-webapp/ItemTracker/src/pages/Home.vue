<script>
import Title from '@/components/Title.vue'


import utils from '@/utils'

import character_api from '@/apis/character_api'
import user_api from '@/apis/user_api'

export default {
    components: {
        Title,
    },
    emits: ["setCharacter"],
    props:
    {
        user_id: String
    },
    data() {
        return {
            characters: [
                {
                    id: 1,
                    name: "jeifjiefj",
                    level: 2
                }
            ]
        }
    },
    methods:
    {
        addNew() {

        },
        select(index) {
            this.$emit('setCharacter',
                {
                    id: this.characters.id,
                    name: this.characters.name
                }
            )
        }
    },
    mounted() {
        // spell_api.get_all_spell_levels(this.character_id).then(data => this.spellSlots.levels = data)
    }
}

</script>


<template>
    <Title class="mt-2" :title="'Your Characters'" />
    <div class="container fs-2 fw-semibold">

        <ul class="pt-2 list-group">
            <li class="list-group-item" v-for="(ch, index) in characters" >
                <div @click="select(index)">
                    {{ ch.name + " " + ch.level + " level " }}
                </div>
            </li>
            <li class="list-group-item">
                <button type="button" class="btn btn-success" style="width: 100%;" @click="addNew">
                    New
                </button>
            </li>
        </ul>
    </div>
</template>
