<script setup>
import { onMounted, ref } from 'vue'

const props = defineProps({ sides: Number });

import SingleDie from "/src/components/apps/dice/SingleDie.vue"

const dieA = ref(null)
const dieB = ref(null)

function RollAll() {
  dieA.value.Roll()
  dieB.value.Roll()
}

defineExpose({
  RollAll
})

</script>

<template>
  <div class="dice-card">
    <ul :class="'list-group d-inline-flex list-group-horizontal d' + sides.toString()">
      <li :class="'list-group-item d' + props.sides.toString() + '-bg'">
        <span class="display-6">
          <span class="badge rounded-pill">d{{ props.sides.toString() }}</span>
        </span>
      </li>
      <li class="list-group-item d-inline-flex">
        <SingleDie ref="dieA" class="me-2" :sides="sides" />
        <SingleDie ref="dieB" :sides="sides" />
      </li>
    </ul>
  </div>
</template>
