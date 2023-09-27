<script setup>
import { onMounted, ref } from 'vue'
import { dialogue, emotions } from '/src/data/sceneStarterData'

const dialogueVal = ref("")
const emotionVal = ref("")

onMounted(() => {
  reroll()
});

function reroll() {
  getRandomDialogue()
  getRandomEmotion()
}

function getRandomDialogue() {
  dialogueVal.value = dialogue[Math.floor(Math.random() * dialogue.length)];
}

function getRandomEmotion() {
  emotionVal.value = emotions[Math.floor(Math.random() * emotions.length)];
}

</script>

<template>
  <div class="scene-starter">
    <p class="emotion">{{ emotionVal }}</p>
    <p class="dialogue">{{ dialogueVal }}</p>
    <button type="button" class="btn btn-primary" @click="reroll()">Reroll!</button>
  </div>
</template>

<style>
.emotion {
  font-size: 2rem;
  font-weight: bold;
}

.dialogue {
  font-size: 1.25rem;
}
</style>


