<template>
    <div class="screen">
        <nuxt-loading-indicator />
        <topVue />
        <slot />
    </div>
</template>
<script setup>
import topVue from '~~/components/top.vue';
</script>
<style lang="scss">
.screen {
    display: flex;
    flex-direction: column;
    min-height: 100vh;
    min-width: 100vw;
    overflow-x: hidden;
}
</style>