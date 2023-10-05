<script setup>
import { onMounted, ref } from 'vue'
import { warmups, mains } from '/src/data/vocalpractice'
import CountDownTimer from '/src/components/common/CountDownTimer.vue'

const warmup1 = ref(null)
const warmup2 = ref(null)
const main1 = ref(null)
const main2 = ref(null)
const timerWarmupSecs = ref(300)
const timerMainSecs = ref(600)

onMounted(() => {
  Reroll()
})

function Reroll() {
  GetRandomWarmups()
  GetRandomMains()
}

function GetRandomWarmups() {
  warmup1.value = warmups[Math.floor(Math.random() * warmups.length)]
  warmup2.value = warmups[Math.floor(Math.random() * warmups.length)]

  // TODO: Uh...fix this.  Permutations, etc.  No replacement.
  if (warmup1.value === warmup2.value) {
    GetRandomWarmups()
  }
}

function GetRandomMains() {
  main1.value = mains[Math.floor(Math.random() * mains.length)]
  main2.value = mains[Math.floor(Math.random() * mains.length)]

  // TODO: Uh...fix this.  Permutations, etc.  No replacement.
  if (main1.value === main2.value) {
    GetRandomMains()
  }
}
</script>

<template>
  <div class="vocal-practice">
    <h1>Vocal Practice Generator</h1>
    <hr />
    <button type="button" class="btn btn-primary mb-4" @click="Reroll()">
      New Practice Routine!
    </button>

    <div class="accordion mb-4" id="vocal-practice-accordion">
      <div class="accordion-item">
        <div class="accordion-header">
          <button class="accordion-button" id="warmup-label" type="button" data-bs-toggle="collapse"
            data-bs-target="#warmup-collapse" aria-expanded="true" aria-controls="warmup-collapse">
            <h2>Warm Up</h2>
          </button>
        </div>
        <div id="warmup-collapse" class="accordion-collapse collapse show" aria-labelledby="warmup-label"
          data-bs-parent="#vocal-practice-accordion">
          <div class="accordion-body">
            <CountDownTimer :seconds="timerWarmupSecs" class="mb-4" />
            <div class="warmup mb-4"><span v-html="warmup1"></span></div>
            <hr />
            <div class="warmup mb-4"><span v-html="warmup2"></span></div>
            <hr />
          </div>
        </div>
      </div>
      <div class="accordion-item">
        <div class="accordion-header">
          <button class="accordion-button" id="main-practice-label" type="button" data-bs-toggle="collapse"
            data-bs-target="#main-practice-collapse" aria-expanded="true" aria-controls="main-practice-collapse">
            <h2>Main Practice</h2>
          </button>
        </div>
        <div id="main-practice-collapse" class="accordion-collapse collapse show" aria-labelledby="main-practice-label"
          data-bs-parent="#vocal-practice-accordion">
          <div class="accordion-body">
            <CountDownTimer :seconds="timerMainSecs" class="mb-4" />
            <div class="main mb-4"><span v-html="main1"></span></div>
            <hr />
            <div class="main mb-4"><span v-html="main2"></span></div>
            <hr />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
