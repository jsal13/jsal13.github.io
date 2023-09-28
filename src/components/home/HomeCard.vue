<script setup>
const props = defineProps({ itemData: Object })
</script>

<template>
  <ul class="list-group mb-4">
    <li class="list-group-item bg-primary text-white list-title" aria-current="true">
      <h1 class="display-6">{{ props.itemData.title }}</h1>
    </li>
    <li class="list-group-item" v-for="(item, index) in props.itemData.data" :key="'item-' + index">
      <span v-html="item"></span>
    </li>
  </ul>
</template>
