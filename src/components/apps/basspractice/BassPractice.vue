<script setup>
import { onMounted, ref, watch } from 'vue'
import { warmups } from '/src/data/basspractice'

const warmup = ref("")

onMounted(() => {
    getRandomWarmup()
});

function getRandomWarmup() {
    warmup.value = warmups[Math.floor(Math.random() * warmups.length)];
}

</script>

<template>
    <div class="bass-practice">
        <h1>Warm Up</h1>
        <div class="warmup mb-4"><span v-html="warmup"></span></div>
    </div>
</template>
