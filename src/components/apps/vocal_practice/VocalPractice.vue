<script setup>
import { onMounted, ref } from 'vue'
import { warmups } from '/src/data/vocalpractice'
import CountDownTimer from '/src/components/common/CountDownTimer.vue'

const warmup1 = ref('')
const warmup2 = ref('')

onMounted(() => {
  getRandomWarmups()
})

function getRandomWarmups() {
  warmup1.value = warmups[Math.floor(Math.random() * warmups.length)]
  warmup2.value = warmups[Math.floor(Math.random() * warmups.length)]

  // TODO: Uh...fix this.  Permutations, etc.  No replacement.
  if (warmup1.value === warmup2.value) {
    getRandomWarmups()
  }
}
</script>

<template>
  <div class="bass-practice">
    <h1>Bass Practice Generator</h1>
    <button type="button" class="btn btn-primary mb-4" @click="getRandomWarmups()">
      New Practice Routine!
    </button>
    <hr class="mb-4" />
    <h2>Warm Up</h2>
    <CountDownTimer :seconds="300" class="mb-4" />
    <div class="warmup mb-4"><span v-html="warmup1"></span></div>
    <div class="warmup mb-4"><span v-html="warmup2"></span></div>
  </div>
</template>
