<script setup>
import { watch, ref } from 'vue';
const props = defineProps({ text: String, size: String })

const showSpoiler = ref(true);

watch(() => props.text, () => {
    if (!showSpoiler.value) {
        toggleSpoiler();
    }
})

function toggleSpoiler() {
    showSpoiler.value = !showSpoiler.value;
}
</script>

<template>
    <div class="spoiler-text">
        <p :class="{ spoiler: showSpoiler }" @click="toggleSpoiler()">{{ text }}</p>
    </div>
</template>

<style>
.spoiler-text>p {
    color: black;
    font-size: v-bind(size);
}

.spoiler {
    background-color: black;
}
</style>