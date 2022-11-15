<template>
    <div class="screen">
        <nuxt-loading-indicator />
        <navVue />
        <slot />
    </div>
</template>
<script setup>
import navVue from '~~/components/nav.vue';
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