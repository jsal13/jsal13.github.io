<script setup>
import { onMounted, ref } from 'vue'
import { mains } from '/src/data/dancepractice'
import DancePracticeEmbed from '/src/components/apps/dance_practice/DancePracticeEmbed.vue'
import CountDownTimer from '/src/components/common/CountDownTimer.vue'

const main1 = ref(null)
const main2 = ref(null)
const timerWarmupSecs = ref(300)
const timerMainSecs = ref(600)

onMounted(() => {
  Reroll()
})

function Reroll() {
  GetRandomMains()
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
  <div class="dance-practice">
    <h1>Dance Practice Generator</h1>
    <hr />
    <button type="button" class="btn btn-primary mb-4" @click="Reroll()">
      New Practice Routine!
    </button>

    <div class="accordion mb-4" id="dance-practice-accordion">
      <div class="accordion-item">
        <div class="accordion-header">
          <button class="accordion-button" id="main-practice-label" type="button" data-bs-toggle="collapse"
            data-bs-target="#main-practice-collapse" aria-expanded="true" aria-controls="main-practice-collapse">
            <h2>Main Practice</h2>
          </button>
        </div>
        <div id="main-practice-collapse" class="accordion-collapse collapse show" aria-labelledby="main-practice-label"
          data-bs-parent="#dance-practice-accordion">
          <div class="accordion-body">
            <CountDownTimer :seconds="timerMainSecs" class="mb-4" />
            <div class="main mb-4">
              <DancePracticeEmbed :url="main1" />
            </div>
            <hr />
            <div class="main mb-4">
              <DancePracticeEmbed :url="main2" />
            </div>
            <hr />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
