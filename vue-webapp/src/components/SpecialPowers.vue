

<script lang="ts">
import { defineComponent } from 'vue'
import type { PropType } from 'vue'

import sp_api from '@/apis/sp_api';
import type { Character } from '@/models/character';

import TitleWithEdit from '@/components/bits/TitleWithEdit.vue'
import EditSpPowersForm from '@/components/bits/EditSpPowersForm.vue'
import SpellCharge from '@/components/bits/SpellCharge.vue'

import utils from '@/utils'
import type { SpecialPower } from '@/models/specialpower';

export default defineComponent({
    components: {
        TitleWithEdit,
        EditSpPowersForm,
        SpellCharge
    },
    props: {
        character: Object as PropType<Character>,
    },
    data() {
        return {
            title: 'Spell Slots',
            powers: Array<SpecialPower>()
        }
    },
    methods: {
        async ReloadSpecialPowers() {
            this.powers = []
            if (this.character == undefined) return;
            sp_api.get_all_special_powers(this.character.id)
                .then((data:Array<SpecialPower>) => this.powers = data)
        },

        async onUseSPCharge(power_id:number, charge_id:number, checked:boolean) {
            this.powers[power_id].charges[charge_id] = checked;

            var power = this.powers[power_id];
            var res = await sp_api.set(
                power.id,
                power.name,
                power.charges.length,
                utils.calculate_used_charges(power.charges));

            this.powers[power_id].charges[charge_id] = res ? checked : !checked;
        },

        async restoreAllSPs(power_id: number) {

            var power = this.powers[power_id];
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
        }
    },
    mounted() {
        this.ReloadSpecialPowers();
    }
})
</script>

<template>
    <TitleWithEdit :title="title" :id_for_modal_selector="'#SpecialPowersModal'" />
    <EditSpPowersForm :title="title" :form_id="'SpecialPowersModal'" :ref_powers="powers"
        :character_id="character?.id" @UpdatePowers="ReloadSpecialPowers" />

    <ul class="pt-2 list-group">
        <li class="list-group-item" v-for="(power, index) in powers">
            <SpellCharge :title="power.name" :charges="power.charges" :key="index"
                @CheckBoxClick="(id: number, checked: boolean) => onUseSPCharge(index, id, checked)"
                @restoreAll="() => restoreAllSPs(index)" />
        </li>
    </ul>
</template>

<style scoped></style>