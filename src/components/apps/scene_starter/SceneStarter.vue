<script setup>
import { onMounted, ref } from 'vue'
import { dialogue, emotions } from '/src/data/sceneStarterData'

const dialogueVal = ref('')
const emotionVal = ref('')

onMounted(() => {
  reroll()
})

function reroll() {
  getRandomDialogue()
  getRandomEmotion()
}

function getRandomDialogue() {
  dialogueVal.value = dialogue[Math.floor(Math.random() * dialogue.length)]
}

function getRandomEmotion() {
  emotionVal.value = emotions[Math.floor(Math.random() * emotions.length)]
}
</script>

<template>
  <div class="scene-starter">
    <h1 class="mb-4">Random Dialogue with Emotion</h1>
    <h2 class="emotion">{{ emotionVal }}</h2>
    <p class="dialogue">{{ dialogueVal }}</p>
    <button type="button" class="btn btn-primary" @click="reroll()">Reroll!</button>
  </div>
</template>

<style>
.dialogue {
  font-size: 1.25rem;
}
</style>
