<script>
import Title from '@/components/Title.vue'
import TitleWithEdit from '@/components/TitleWithEdit.vue'
import SpellCharge from '@/components/SpellCharge.vue'
import Consumable from '@/components/Consumable.vue'
import Artifacts from '@/components/Artifacts.vue'
import BackpackItem from '@/components/BackpackItem.vue'
import NewItemForm from '@/components/NewItemForm.vue'
import EditChargesForm from '@/components/EditChargesForm.vue'

import utils from '@/utils'

import artifact_api from '@/apis/artifact_api'
import backpack_api from '@/apis/backpack_api'
import character_api from '@/apis/character_api'
import consumable_api from '@/apis/consumable_api'
import sp_api from '@/apis/sp_api'
import spell_api from '@/apis/spell_api'
import user_api from '@/apis/user_api'
import EditSpPowersForm from '@/components/EditSpPowersForm.vue'

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
    EditSpPowersForm
},
    props: {
        user_id: Number,
        character_id: Number,
    },
    data() {

        return {

            spellSlots:
            {
                title: 'Spell Slots',
                levels: [
                    // {
                    //     level: 1,
                    //     charges: [true, true, false]
                    // }
                ]
            },
            spPowers:
            {
                title: 'Special Powers',
                powers: [
                    // {
                    //     name: "Monc Power",
                    //     charges: [true, false, true, false]
                    // },
                    // {
                    //     name: "Other Power",
                    //     charges: [true, false, true, false]
                    // }
                ]
            },
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

        //Spells
        async onUseSpellCharge(level_id, charge_id, checked) {
            this.spellSlots.levels[level_id].charges[charge_id] = checked;
            var level = this.spellSlots.levels[level_id];
            var res = await spell_api.set(
                level.id,
                level.level,
                level.charges.length,
                utils.calculate_used_charges(level.charges));

            this.spellSlots.levels[level_id].charges[charge_id] = res ? checked : !checked;
        },

        async restoreAllSpellCharges(level_id) {
            var level = this.spellSlots.levels[level_id];
            var res = await spell_api.set(
                level.id,
                level.level,
                level.charges.length,
                0);

            if (res) {
                for (var i = 0; i < level.charges.length; i++) {
                    level.charges[i] = false;
                }
            }
        },

        async ReloadSpells() {
            this.spellSlots.levels = []
            spell_api.get_all_spell_levels(this.character_id)
                .then(data => this.spellSlots.levels = data)
        },

        async ReloadSpecialPowers() {
            this.spPowers.powers = []
            sp_api.get_all_special_powers(this.character_id)
                .then(data => this.spPowers.powers = data)
        },

        //Special Powers
        async onUseSPCharge(power_id, charge_id, checked) {
            this.spPowers.powers[power_id].charges[charge_id] = checked;

            var power = this.spPowers.powers[power_id];
            var res = await sp_api.set(
                power.id,
                power.name,
                power.charges.length,
                utils.calculate_used_charges(power.charges));

            this.spPowers.powers[power_id].charges[charge_id] = res ? checked : !checked;
        },

        async restoreAllSPs(power_id) {

            var power = this.spPowers.powers[power_id];
            var res = await sp_api.set(
                power.id,
                power.name,
                power.charges.length,
                0);

            if (res) {
                for (var i = 0; i < power.charges.length; i++) {
                    power.charges[i] = false;
                }
            }
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
            if (res.status)
            {
                item.id = res.new_id;
                this.consumables.push(item);
            }
        },

        async deleteConsumable(consumable_id) {
            const cons = this.consumables.splice(consumable_id, 1);

            var res = await consumable_api.delete(cons[0].id);
            if (!res)
            {
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
            if (!res)
            {
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
            if (!res)
            {
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
            if (res.status)
            {
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
            debugger
            var res = await backpack_api.create(obj.name, obj.amount, obj.descr, this.character_id);
            if (res.status)
            {
                item.id = res.new_id;
                this.bPItems.push(item)
            }
        }
    },
    mounted() {
        spell_api.get_all_spell_levels(this.character_id).then(data => this.spellSlots.levels = data)
        sp_api.get_all_special_powers(this.character_id).then(data => this.spPowers.powers = data)
        consumable_api.get_all_consumables(this.character_id).then(data => this.consumables = data)
        artifact_api.get_all_artifacts(this.character_id).then(data => this.artifacts = data)
        backpack_api.get_all_items(this.character_id).then(data => this.bPItems = data)
    }
}

</script>


<template>
    <div class="container mt-2 mb-4">
        <div class="row">
            <div class="pt-4 col-sm-12 col-md-6">
                <TitleWithEdit :title="spellSlots.title" :id_for_modal_selector="'#SpellSlotsModal'" />
                <EditChargesForm :title="spellSlots.title" :form_id="'SpellSlotsModal'" :ref_levels="spellSlots.levels"
                    :character_id="character_id" @UpdateSpells="ReloadSpells" />

                <ul class="pt-2 list-group">
                    <li class="list-group-item" v-for="(level, index) in spellSlots.levels" :key="index">
                        <SpellCharge :title="intToRoman(level.level) + ' Level'" :charges="level.charges"
                            @CheckBoxClick="(id, checked) => onUseSpellCharge(index, id, checked)"
                            @restoreAll="() => restoreAllSpellCharges(index)" />
                    </li>
                </ul>
            </div>

            <div class="pt-4 col-sm-12 col-md-6">
                <TitleWithEdit :title="spPowers.title" :id_for_modal_selector="'#SpecialPowersModal'" />
                <EditSpPowersForm :title="spPowers.title" :form_id="'SpecialPowersModal'" :ref_powers="spPowers.powers"
                    :character_id="character_id" @UpdatePowers="ReloadSpecialPowers" />

                <ul class="pt-2 list-group">
                    <li class="list-group-item" v-for="(power, index) in spPowers.powers">
                        <SpellCharge :title="power.name" :charges="power.charges" :key="index"
                            @CheckBoxClick="(id, checked) => onUseSPCharge(index, id, checked)"
                            @restoreAll="() => restoreAllSPs(index)" />
                    </li>
                </ul>
            </div>

            <div class="pt-4 col-sm-12 col-md-6">
                <Title :title="'Consumables'" />
                <ul class="pt-2 list-group">
                    <li v-for="(item, index) in consumables" class="list-group-item">
                        <Consumable :name="item.name" :descr="item.descr" :amount="item.amount"
                            @ChangeAmount="(addition) => changeConsumableAmount(index, addition)" 
                            @Delete="() => deleteArtifact(index)"/>
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
                            @restoreAll="() => restoreAllArtifactCharges(index)" 
                            @remove="() => deleteArtifact(index)"/>
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
