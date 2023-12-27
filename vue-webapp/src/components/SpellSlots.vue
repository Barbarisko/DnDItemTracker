

<script lang="ts">
import { defineComponent } from 'vue'
import type { PropType } from 'vue'

import spell_api from '@/apis/spell_api';
import type { Character } from '@/models/character';
import type { SpellSlot } from '@/models/spellslot';

import TitleWithEdit from '@/components/bits/TitleWithEdit.vue'
import EditChargesForm from '@/components/bits/EditChargesForm.vue'
import SpellCharge from '@/components/bits/SpellCharge.vue'

import utils from '@/utils'

export default defineComponent({
    components: {
        TitleWithEdit,
        EditChargesForm,
        SpellCharge
    },
    props: {
        character: Object as PropType<Character>,
    },
    data() {
        return {
            title: 'Spell Slots',
            spellSlots: Array<SpellSlot>()
        }
    },
    methods: {
        async onUseSpellCharge(level_id: number, charge_id: number, checked: boolean) {
            this.spellSlots[level_id].charges[charge_id] = checked;
            var level = this.spellSlots[level_id];
            var res = await spell_api.set(
                level.id,
                level.level,
                level.charges.length,
                utils.calculate_used_charges(level.charges));

            this.spellSlots[level_id].charges[charge_id] = res ? checked : !checked;
        },

        async restoreAllSpellCharges(level_id: number) {
            var level = this.spellSlots[level_id];
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
            this.spellSlots = []
            if (this.character == undefined) return;
            spell_api.get_all_spell_levels(this.character.id)
                .then((data: Array<SpellSlot>) => {
                    debugger
                    this.spellSlots = data
                })
        },
        intToRoman(num: number) {
            return utils.intToRoman(num);
        }
    },
    mounted() {
        debugger
            this.ReloadSpells();
    }
})
</script>

<template>
    <TitleWithEdit :title="title" :id_for_modal_selector="'#SpellSlotsModal'" />
    <EditChargesForm :title="title" :form_id="'SpellSlotsModal'" :ref_levels="spellSlots" :character_id="character?.id"
        @UpdateSpells="ReloadSpells" />

    <ul class="pt-2 list-group">
        <li class="list-group-item" v-for="(level, index) in spellSlots" :key="index">
            <SpellCharge :title="intToRoman(level.level) + ' Level'" :charges="level.charges"
                @CheckBoxClick="(id: number, checked: boolean) => onUseSpellCharge(index, id, checked)"
                @restoreAll="() => restoreAllSpellCharges(index)" />
        </li>
    </ul>
</template>

<style scoped></style>