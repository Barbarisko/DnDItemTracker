<script>
import Title from '@/components/Title.vue'
import utils from '@/utils'
import character_api from '@/apis/character_api'
import user_api from '@/apis/user_api'

import { useUserStore } from '../stores/user-session'

export default {
    components: {
        Title,
    },
    data() {
        return {
            userSession: useUserStore(),
            characters: [
                {
                    id: 1,
                    name: "jeifjiefj",
                    level: 2
                }
            ],
            new_name: "",
            new_level: 1,
            new_class: ""
        }
    },
    methods:
    {
        async addNew() {
            var item = {
                name: this.new_name,
                level: this.new_level,
                class_name: this.new_class,
            }
            var res = await character_api.create(this.new_name, this.new_level, this.new_class, this.userSession.id);
            if (res.status) {
                item.id = res.new_id;
                this.characters.push(item);
            }
        },

        select(index) {
            debugger
            this.userSession.setCharacter({
                id: this.characters[index].id,
                name: this.characters[index].name
            });
        }
    },
    mounted() {
        character_api.get_all_characters(this.userSession.id).then(data => this.characters = data)
    }
}

</script>


<template>
    <Title class="mt-2" :title="'Your Characters'" />
    <div class="container fs-2 fw-semibold">

        <ul class="pt-2 list-group">
            <li class="list-group-item" v-for="(ch, index) in characters">
                <!-- <div @click="select(index)">
                    {{ ch.name + " " + ch.level + " level " }}
                </div> -->
                <router-link to="/character" :tag="button" @click.native="select(index)">
                    {{ ch.name + " " + ch.level + " level " }}
                </router-link>
            </li>
            <li class="list-group-item">
                <div class="row">
                    <div class="col">
                        <label for="NameInput" class="form-label">Name</label>
                        <input v-model="new_name" type="text" class="form-control" id="NameInput" required="" />
                    </div>
                    <div class="col">
                        <label class="form-label" for="LevelInput">Level</label>
                        <input v-model="new_level" min="1" type="number" id="LevelInput" class="form-control" />
                    </div>
                    <div class="col">
                        <label for="ClassInput" class="form-label">Class</label>
                        <input v-model="new_class" type="text" class="form-control" id="ClassInput" required="" />
                    </div>
                </div>
                <div class="row mt-2">
                    <div class="col">
                        <button type="button" class="btn btn-success" style="width: 100%;" @click="addNew">
                            New
                        </button>
                    </div>
                </div>
            </li>
        </ul>
    </div>
</template>
