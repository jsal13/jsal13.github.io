<script setup>
import { onMounted, ref } from 'vue'

const props = defineProps({ sides: Number });
const val = ref(1)

function Roll() {
  // The maximum is exclusive and the minimum is inclusive
  val.value = Math.floor((Math.random() * props.sides) + 1);
}

onMounted(() => { Roll() })

defineExpose({
  Roll, val
})

</script>

<template>
  <div class="single-die">
    <!-- BOOTSTRAP 5: Badges scale to match the size of the immediate parent element by using relative font sizing and em units. Hence the outer span. -->
    <span class="display-6">
      <span :class="'badge rounded-pill die-badge d' + props.sides.toString()">
        {{ val }}
      </span>
    </span>
  </div>
</template>

