<script setup>
import { onMounted, ref } from 'vue'
import { dialogue, emotions } from '/src/data/sceneStarterData'

const dialogueVal = ref('')
const emotionVal = ref('')

onMounted(() => {
  NewSceneStarter()
})

function NewSceneStarter() {
  // Get new dialogue and emotion.
  dialogueVal.value = dialogue[Math.floor(Math.random() * dialogue.length)]
  emotionVal.value = emotions[Math.floor(Math.random() * emotions.length)]
}
</script>

<template>
  <div class="scene-starter">
    <h1 class="mb-4">Random Dialogue with Emotion</h1>
    <hr />
    <p class="emotion h4">{{ emotionVal }}</p>
    <p class="dialogue h6">"{{ dialogueVal }}"</p>
    <button type="button" class="btn btn-primary mt-4" @click="NewSceneStarter">Randomize!</button>
  </div>
</template>
