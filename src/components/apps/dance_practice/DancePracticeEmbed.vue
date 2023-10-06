<script setup>
const props = defineProps({ url: String })
</script>

<template>
    <div class="embed-responsive embed-responsive-16by9">
        <iframe class="embed-responsive-item" :src="'https://www.youtube.com/embed/' + props.url" allowfullscreen></iframe>
    </div>
</template>