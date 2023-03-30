<script>
import Title from './components/Title.vue'
import TitleWithEdit from './components/TitleWithEdit.vue'
import SpellCharge from './components/SpellCharge.vue'
import Consumable from './components/Consumable.vue'
import Artifacts from './components/Artifacts.vue'
import BackpackItem from './components/BackpackItem.vue'

export default {
    components: {
        Title,
        TitleWithEdit,
        SpellCharge,
        Consumable,
        Artifacts,
        BackpackItem
    },
    data() {
        return {
            spellSlots:
            {
                title: 'Spell Slots',
                levels: [
                    [true, true, false],
                    [true, true, false],
                    [true, true, false],
                    [true, true, false]
                ]
            },
            spPowers:
            {
                title: 'Special Powers',
                powers: [
                    {
                        name: "Monc Power",
                        charges: [true, false, true, false]
                    },
                    {
                        name: "Other Power",
                        charges: [true, false, true, false]
                    }
                ]
            },
            consumables: [
                {
                    name: "Food",
                    descr: "Eat eat, yammy!",
                    amount: 10
                },
                {
                    name: "Potion",
                    descr: "Heals",
                    amount: 10
                }
            ],
            artifacts: [
                {
                    name: "Sword",
                    descr: "Cuts in half",
                    charges: [true, false, true, false]
                },
                {
                    name: "Stick",
                    descr: "Bonk!",
                    charges: [true, false, true, false]
                }
            ],
            bPItems: [
                {
                    name: "Rope",
                    descr: "30 ft long, like my dick",
                    amount: 10
                },
                {
                    name: "Condoms",
                    descr: "For my ropes",
                    amount: 10
                }
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
            console.log(res);
            return res;
        },

        onUseSpellCharge(level_id, charge_id, checked) {
            this.spellSlots.levels[level_id][charge_id] = checked;
        },

        onUseSPCharge(power_id, charge_id, checked) {
            this.spPowers.powers[power_id].charges[charge_id] = checked;
        },

        changeConsumableAmount(consumable_id, addition) {
            this.consumables[consumable_id].amount += addition;
        },

        onUseArtifactCharge(artifact_id, charge_id, checked) {
            this.artifacts[artifact_id].charges[charge_id] = checked;
        },

        changeBackpackItemAmount(item_id, addition) {
            this.bPItems[item_id].amount += addition;
        },

        deleteBackpackItem(item_id) {
            this.bPItems.splice(item_id, 1);
        },

        duplicateBackpackItem(item_id) {
            var new_item =                 {
                    name: this.bPItems[item_id].name,
                    descr: this.bPItems[item_id].descr,
                    amount: this.bPItems[item_id].amount
                }
            
            this.bPItems.push(new_item);
        }
    }
}

</script>


<template>
    <div class="container mt-2 mb-4">
        <div class="row">
            <div class="pt-4 col-sm-12 col-md-6">
                <TitleWithEdit :title="spellSlots.title" />
                <ul class="pt-2 list-group">
                    <li class="list-group-item" v-for="(charges, index) in spellSlots.levels" :key="index">
                        <SpellCharge :title="intToRoman(index + 1) + ' Level'" :charges="charges"
                            @CheckBoxClick="(id, checked) => onUseSpellCharge(index, id, checked)" />
                    </li>
                </ul>
            </div>

            <div class="pt-4 col-sm-12 col-md-6">
                <TitleWithEdit :title="spPowers.title" />
                <ul class="pt-2 list-group">
                    <li class="list-group-item" v-for="(power, index) in spPowers.powers">
                        <SpellCharge :title="power.name" :charges="power.charges" :key="index"
                            @CheckBoxClick="(id, checked) => onUseSPCharge(index, id, checked)" />
                    </li>
                </ul>
            </div>

            <div class="pt-4 col-sm-12 col-md-6">
                <Title :title="'Consumables'" />
                <ul class="pt-2 list-group">
                    <li v-for="(item, index) in consumables" class="list-group-item">
                        <Consumable :name="item.name" :descr="item.descr" :amount="item.amount"
                            @ChangeAmount="(addition) => changeConsumableAmount(index, addition)" />
                    </li>
                    <li class="list-group-item">
                        <button type="button" class="btn btn-success" style="width: 100%;">
                            Add
                        </button>

                    </li>
                </ul>
            </div>

            <div class="pt-4 col-sm-12 col-md-6">
                <Title :title="'Artifacts'" />
                <div class="pt-2 list-group">
                    <div v-for="(artif, index) in artifacts" class="list-group-item">
                        <Artifacts :name="artif.name" :descr="artif.descr" :charges="artif.charges"
                            @CheckBoxClick="(id, checked) => onUseArtifactCharge(index, id, checked)" />
                    </div>
                    <li class="list-group-item">
                        <button type="button" class="btn btn-success" style="width: 100%;">
                            Add
                        </button>

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
                        <button type="button" class="btn btn-success" style="width: 100%;">
                            Add
                        </button>
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
