<script setup>
const props = defineProps({ countryAbbr: String })
</script>

<template>
    <div class="flags-image">
        <img class="flag" :src="'assets/flags/' + props.countryAbbr + '.svg'" />
    </div>
</template>

<style>
.flag {
    width: 100%;
    border: 1px solid lightgray;
}
</style>