<script setup>
import { onMounted, ref } from 'vue'
import DiceCard from '/src/components/apps/dice/DiceCard.vue'

const d4 = ref(null)
const d6 = ref(null)
const d8 = ref(null)
const d10 = ref(null)
const d12 = ref(null)
const d20 = ref(null)

function RollAll() {
  // Rolls all die.
  d4.value.RollAll()
  d6.value.RollAll()
  d8.value.RollAll()
  d10.value.RollAll()
  d12.value.RollAll()
  d20.value.RollAll()
}

onMounted(() => {
  RollAll()
})
</script>

<template>
  <div class="dice-roller">
    <h1 class="mb-4">Dice</h1>
    <hr />
    <button type="button" class="btn btn-primary" @click="RollAll()">
      <span class="h3">ROLL!</span>
    </button>
    <hr />

    <div class="container d-flex-column">
      <DiceCard ref="d4" class="mb-2" :sides="4" />
      <DiceCard ref="d6" class="mb-2" :sides="6" />
      <DiceCard ref="d8" class="mb-2" :sides="8" />
      <DiceCard ref="d10" class="mb-2" :sides="10" />
      <DiceCard ref="d12" class="mb-2" :sides="12" />
      <DiceCard ref="d20" class="mb-2" :sides="20" />
    </div>
  </div>
</template>
