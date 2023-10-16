<script setup>
import { ref, watch } from 'vue'

// White, Green, Red, Yellow
const colorProgression = ['#ffffff', '#2a7f62', '#f55d3e', '#f7cb15']

const idx = ref(0)
const squareColor = ref(colorProgression[idx.value])

watch(
  () => idx.value,
  (val) => {
    squareColor.value = colorProgression[val]
  }
)

function ChangeColor() {
  idx.value = (idx.value + 1) % colorProgression.length
}
</script>

<template>
  <div class="grid-square">
    <div
      class="grid-square-single"
      :style="'background-color: ' + squareColor + ';'"
      @click="ChangeColor()"
    ></div>
  </div>
</template>

<style>
.grid-square-single {
  height: 50px;
  width: 50px;
  border: 1px solid black;
}
</style>
