<script setup>
import { onMounted, ref, watch } from 'vue'
import { facialExpressionData } from '/src/data/facialExpressions'

const expressionData = ref("")
const expressionEmoji = ref("")
const expressionName = ref("")

onMounted(() => {
  getRandomExpression()
});

function getRandomExpression() {
  expressionData.value = facialExpressionData[Math.floor(Math.random() * facialExpressionData.length)];
}

watch(() => expressionData.value, (value) => {
  expressionEmoji.value = value["emoji"];
  expressionName.value = value["name"]
})


</script>

<template>
  <div class="scene-starter">
    <p class="emoji">{{ expressionEmoji }}</p>
    <!-- <p class="expression-name">{{ expressionName }}</p> -->
    <button type="button" class="btn btn-primary" @click="getRandomExpression()">Reroll!</button>
  </div>
</template>

<style>
.emoji {
  font-size: 8rem;
}

.expression-name {
  font-size: 1.25rem;
}
</style>


