<script setup>
import { ref } from 'vue'

import GridSquare from '/src/components/apps/grid/GridSquare.vue'

const numSquares = ref(200)
</script>

<template>
  <div class="grid-span">
    <div class="container d-inline-flex flex-wrap">
      <GridSquare v-for="n in numSquares" :key="'square-' + n" />
    </div>
  </div>
</template>
