<script setup>
import NaviBar from '/src/components/navigation/NaviBar.vue'
</script>

<template>
  <main>
    <NaviBar class="mb-4" />
    <div class="container">
      <div class="row">
        <div class="col-lg-2"></div>
        <div class="col-lg-8">
          <RouterView />
        </div>
        <div class="col-lg-2"></div>
      </div>
    </div>
  </main>
</template>
