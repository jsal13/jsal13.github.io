<script setup>
// Make this timer better.  Maybe give it a pause function.

import { ref, onMounted, watch } from 'vue'
import { countdown } from '/src/scripts/countdown'

const props = defineProps({ seconds: Number })

const endTime = ref(0)
const delta = ref(0)

const minsRemaining = ref(0)
const secsRemaining = ref(0)
const interval = ref(0)
const playing = ref(false)
const timerComplete = ref(false)
const iconVal = ref('bi-play')
const bgColor = ref('bg-dark')

onMounted(() => {
  minsRemaining.value = parseInt(Math.floor(props.seconds / 60))
  secsRemaining.value = props.seconds % 60
})

watch(
  () => delta.value,
  (val) => {
    minsRemaining.value = val.minutes
    secsRemaining.value = val.seconds
  }
)

watch(() => secsRemaining.value, (val) => {
  if (minsRemaining.value <= 0 & val <= 0) {
    timerComplete.value = true
    minsRemaining.value = 0
    secsRemaining.value = 0
    PauseTimer()
  }
  else {
    timerComplete.value = false
  }
})

watch(
  () => playing.value,
  (val) => {
    if (val) {
      iconVal.value = 'bi-pause'
      bgColor.value = 'bg-success'
    } else {

      if (timerComplete.value) {
        bgColor.value = 'bg-danger'
      }
      else {
        iconVal.value = 'bi-play-fill'
        bgColor.value = 'bg-dark'
      }
    }
  }
)

function StartTimer(secondsRemaining) {
  endTime.value = new Date(new Date().getTime() + secondsRemaining * 1000)
  delta.value = countdown(new Date(), endTime.value)
  playing.value = true
  interval.value = setInterval(UpdateTimer, 1000)
}

function UpdateTimer() {
  delta.value = countdown(new Date(), endTime.value)
}

function ResetTimer() {
  clearInterval(interval.value)
  StartTimer(props.seconds)
}

function ToggleTimer() {
  if (playing.value) {
    PauseTimer()
  } else {
    StartTimer(minsRemaining.value * 60 + secsRemaining.value)
  }
}

function PauseTimer() {
  playing.value = false
  clearInterval(interval.value)
}
</script>

<template>
  <div :class="'timer d-inline-flex ' + bgColor">
    <div class="d-flex flex-column p-2">
      <div class="d-flex">
        <span class="time-left text-light">{{ minsRemaining.toString().padStart(2, '0') }}m
          {{ secsRemaining.toString().padStart(2, '0') }}s</span>
      </div>
      <div class="d-flex justify-content-around">
        <button class="btn btn-sm rounded-2 play-control-button" @click="ToggleTimer" v-if="!timerComplete">
          <i :class="iconVal + ' play-icon text-dark'"></i>
          <span class="visually-hidden">Toggle Timer Pause / Play</span></button><button
          class="btn btn-sm rounded-2 play-control-button" @click="ResetTimer">
          <i class="bi-arrow-counterclockwise play-icon text-dark"></i>
          <span class="visually-hidden">Reset Timer</span>
        </button>
      </div>
    </div>
  </div>
</template>

<style>
.time-left {
  font-size: 1.5rem;
  font-weight: bold;
  text-shadow: 1px 1px #0f0f0f;
}

.timer {
  border: 1px solid darkgray;
  border-radius: 1rem;
}

.play-control-button {
  background-color: lightgray !important;
}
</style>
