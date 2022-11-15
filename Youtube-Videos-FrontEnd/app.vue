<template>
  <div>
    <nuxt-layout>
      <NuxtPage />
    </nuxt-layout>
  </div>
</template>
<script setup>


useHead({
  title: 'Ahtisham COD Mobile',
  meta: [
    { charset: 'utf-8' },
    { name: 'viewport', content: 'width=device-width, initial-scale=1' },
    {
      name: 'description',
      content: 'Hey There i am CODM & Warzone Mobile Player & Utuber Business email: ahtishamcod123@gmail.com '
    }
  ],
  link: [
    {
      rel: 'stylesheet',
      type: 'text/css',
      href: 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.0/css/all.min.css'
    },
  ],
  script: [


  ]
})
</script>

<style lang="scss">
.splide__arrow svg {
  fill: var(--bg);
  transform: translateY(-21px);
}

.splide__arrow--prev svg {
  transform: scaleX(-1) translateY(-21px);
}
</style>