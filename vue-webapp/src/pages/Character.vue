<script>
import Title from '@/components/bits/Title.vue'
import TitleWithEdit from '@/components/bits/TitleWithEdit.vue'
import SpellCharge from '@/components/bits/SpellCharge.vue'
import Consumable from '@/components/bits/Consumable.vue'
import Artifacts from '@/components/bits/Artifacts.vue'
import BackpackItem from '@/components/bits/BackpackItem.vue'
import NewItemForm from '@/components/bits/NewItemForm.vue'
import EditChargesForm from '@/components/bits/EditChargesForm.vue'
import EditSpPowersForm from '@/components/bits/EditSpPowersForm.vue'

import SpellSlots from '@/components/SpellSlots.vue'
import SpecialPowers from '@/components/SpecialPowers.vue'

import utils from '@/utils'

import artifact_api from '@/apis/artifact_api'
import backpack_api from '@/apis/backpack_api'
import character_api from '@/apis/character_api'
import consumable_api from '@/apis/consumable_api'
import sp_api from '@/apis/sp_api'
import spell_api from '@/apis/spell_api'
import user_api from '@/apis/user_api'

import { useUserStore } from '../stores/user-session'

export default {
    components: {
        Title,
        TitleWithEdit,
        SpellCharge,
        Consumable,
        Artifacts,
        BackpackItem,
        NewItemForm,
        EditChargesForm,
        EditSpPowersForm,
        SpellSlots,
        SpecialPowers
    },
    data() {
        return {
            userSession: useUserStore(),
            consumables: [
                // {
                //     name: "Food",
                //     descr: "Eat eat, yammy!",
                //     amount: 10
                // },
                // {
                //     name: "Potion",
                //     descr: "Heals",
                //     amount: 10
                // }
            ],
            artifacts: [
                // {
                //     name: "Sword",
                //     descr: "Cuts in half",
                //     charges: [true, false, true, false]
                // },
                // {
                //     name: "Stick",
                //     descr: "Bonk!",
                //     charges: [true, false, true, false]
                // }
            ],
            bPItems: [
                // {
                //     name: "Rope",
                //     descr: "30 ft long, like my dick",
                //     amount: 10
                // },
                // {
                //     name: "Condoms",
                //     descr: "For my ropes",
                //     amount: 10
                // }
            ]
        }
    },
    methods:
    {
        intToRoman(num) {
            if (isNaN(num))
                return NaN;
            if (num == 1)
                return "I";
            if (num == 2)
                return "II";
            if (num == 3)
                return "III";
            var digits = String(+num).split(""),
                key = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM",
                    "", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC",
                    "", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"],
                roman = "",
                i = 3;
            while (i--)
                roman = (key[+digits.pop() + (i * 10)] || "") + roman;
            var res = Array(+digits.join("") + 1).join("M") + roman;
            return res;
        },

        //Consumables
        async changeConsumableAmount(consumable_id, addition) {
            var cons = this.consumables[consumable_id];
            var res = await consumable_api.set(cons.id, cons.name, cons.amount + addition, cons.descr);
            if (res)
                this.consumables[consumable_id].amount += addition;
        },

        async addConsumable(obj) {
            var item = {
                name: obj.name,
                descr: obj.descr,
                amount: obj.amount,
                character_id: this.character_id
            }
            var res = await consumable_api.create(obj.name, obj.amount, obj.descr, this.character_id);
            if (res.status) {
                item.id = res.new_id;
                this.consumables.push(item);
            }
        },

        async deleteConsumable(consumable_id) {
            const cons = this.consumables.splice(consumable_id, 1);

            var res = await consumable_api.delete(cons[0].id);
            if (!res) {
                this.consumables.push(cons[0]);
            }
        },

        //Artifacts
        async onUseArtifactCharge(artifact_id, charge_id, checked) {
            this.artifacts[artifact_id].charges[charge_id] = checked;

            var art = this.artifacts[artifact_id];
            var res = await artifact_api.set(
                art.id,
                art.name,
                art.charges.length,
                utils.calculate_used_charges(art.charges),
                art.descr
            );

            this.artifacts[artifact_id].charges[charge_id] = res ? checked : !checked;
        },

        async restoreAllArtifactCharges(artifact_id) {
            var art = this.artifacts[artifact_id];
            var res = await artifact_api.set(
                art.id,
                art.name,
                art.charges.length,
                0,
                art.descr
            );

            if (res) {
                for (var i = 0; i < art.charges.length; i++) {
                    art.charges[i] = false;
                }
            }
        },

        async addArtifactItem(obj) {
            var item = {
                name: obj.name,
                descr: obj.descr,
                charges: Array(obj.charges).fill(false),
                character_id: this.character_id
            }
            var res = await artifact_api.create(obj.name, obj.charges, obj.descr, 0, this.character_id);
            if (res.status)
                this.artifacts.push(item);
        },

        async deleteArtifact(artifact_id) {
            const item = this.artifacts.splice(artifact_id, 1);

            var res = await artifact_api.delete(item[0].id);
            if (!res) {
                this.artifacts.push(item[0]);
            }
        },

        //Backpacks
        async changeBackpackItemAmount(item_id, addition) {
            var item = this.bPItems[item_id];
            var res = await backpack_api.set(item.id, item.name, item.amount + addition, item.descr);
            if (res)
                this.bPItems[item_id].amount += addition;
        },

        async deleteBackpackItem(item_id) {
            const item = this.bPItems.splice(item_id, 1);

            var res = await backpack_api.delete(item[0].id);
            if (!res) {
                this.bPItems.push(item[0]);
            }
        },

        async duplicateBackpackItem(item_id) {
            var new_item = {
                name: this.bPItems[item_id].name,
                descr: this.bPItems[item_id].descr,
                amount: this.bPItems[item_id].amount
            }

            var res = await backpack_api.create(new_item.name, new_item.amount, new_item.descr, this.character_id);
            if (res.status) {
                new_item.id = res.new_id;
                this.bPItems.push(new_item)
            }
        },

        async addBackpackItem(obj) {
            var item = {
                name: obj.name,
                descr: obj.descr,
                amount: obj.amount,
                character_id: this.character_id
            }

            var res = await backpack_api.create(obj.name, obj.amount, obj.descr, this.character_id);
            if (res.status) {
                item.id = res.new_id;
                this.bPItems.push(item)
            }
        }
    },
    mounted() {
        const user_id = this.userSession.selectedCharacter.id;
        consumable_api.get_all_consumables(user_id).then(data => this.consumables = data)
        artifact_api.get_all_artifacts(user_id).then(data => this.artifacts = data)
        backpack_api.get_all_items(user_id).then(data => this.bPItems = data)
    }
}

</script>


<template>
    <div class="container mt-2 mb-4">
        <div class="row">
            <div class="pt-4 col-sm-12 col-md-6">
                <SpellSlots :character="this.userSession.selectedCharacter"></SpellSlots>
            </div>

            <div class="pt-4 col-sm-12 col-md-6">
                <SpecialPowers :character="this.userSession.selectedCharacter"></SpecialPowers>
            </div>

            <div class="pt-4 col-sm-12 col-md-6">
                <Title :title="'Consumables'" />
                <ul class="pt-2 list-group">
                    <li v-for="(item, index) in consumables" class="list-group-item">
                        <Consumable :name="item.name" :descr="item.descr" :amount="item.amount"
                            @ChangeAmount="(addition) => changeConsumableAmount(index, addition)"
                            @Delete="() => deleteConsumable(index)" />
                    </li>
                    <li class="list-group-item">
                        <button type="button" class="btn btn-success" style="width: 100%;" data-bs-toggle="modal"
                            data-bs-target="#AddNewConsumable">
                            Add
                        </button>
                        <NewItemForm @NewItem="addConsumable" :form_id="'AddNewConsumable'" />
                    </li>
                </ul>
            </div>

            <div class="pt-4 col-sm-12 col-md-6">
                <Title :title="'Artifacts'" />

                <div class="pt-2 list-group">
                    <div v-for="(artif, index) in artifacts" class="list-group-item">
                        <Artifacts :name="artif.name" :descr="artif.descr" :charges="artif.charges"
                            @CheckBoxClick="(id, checked) => onUseArtifactCharge(index, id, checked)"
                            @restoreAll="() => restoreAllArtifactCharges(index)" @remove="() => deleteArtifact(index)" />
                    </div>
                    <li class="list-group-item">
                        <button type="button" class="btn btn-success" style="width: 100%;" data-bs-toggle="modal"
                            data-bs-target="#AddNewArtifact">
                            Add
                        </button>
                        <NewItemForm :form_id="'AddNewArtifact'" :has_charges="true" @NewItem="addArtifactItem" />
                    </li>

                </div>
            </div>

            <div class="pt-4 col-sm-12 col-md-6">
                <Title :title="'Light'" />
                <ul class="pt-2 list-group">
                    <li class="list-group-item">
                        TODO
                    </li>
                </ul>
            </div>

            <div class="pt-4 col-sm-12 col-md-6">
                <Title :title="'Money'" />
                <ul class="pt-2 list-group">
                    <li class="list-group-item">
                        TODO
                    </li>
                </ul>
            </div>

            <div class="pt-4 col-12">
                <Title :title="'Backpack'" />
                <ul class="pt-2 list-group">
                    <li class="list-group-item">
                        <button type="button" class="btn btn-success" style="width: 100%;" data-bs-toggle="modal"
                            data-bs-target="#AddNewBPItem">
                            Add
                        </button>
                        <NewItemForm @NewItem="addBackpackItem" :form_id="'AddNewBPItem'" />
                    </li>
                    <li v-for="(item, index) in bPItems" class="list-group-item">
                        <BackpackItem :name="item.name" :descr="item.descr" :amount="item.amount"
                            @ChangeAmount="(addition) => changeBackpackItemAmount(index, addition)"
                            @DuplicateItem="() => duplicateBackpackItem(index)"
                            @DeleteItem="() => deleteBackpackItem(index)" />
                    </li>
                </ul>
            </div>
        </div>
    </div>
</template>
