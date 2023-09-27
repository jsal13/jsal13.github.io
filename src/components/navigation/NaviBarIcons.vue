<script setup>
import ItchIoIcon from '/src/components/icons/ItchIoIcon.vue'
import GithubIcon from '/src/components/icons/GithubIcon.vue'
</script>

<template>
    <div class="navibar-icons">
        <!-- Github. -->
        <a class="icon-link" href="https://github.com/jsal13/">
            <GithubIcon />
        </a>
        <a class="icon-link" href="https://melat0nin.itch.io/">
            <ItchIoIcon />
        </a>
    </div>
</template>

<style>
.navibar-icons * {
    color: lightgray !important;
}

.nav-icon {
    width: 1.75rem;
    height: 1.75rem;
    margin-left: 0.25rem;
    margin-right: 0.25rem;
}
</style>