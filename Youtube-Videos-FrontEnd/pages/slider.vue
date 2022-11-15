<template>
  <div class="wrapper flex jus-center align-center">
    <!-- <h1 class="heading">Latest Videos</h1> -->
    <Splide :options="{ rewind: true, perPage: perPage, width: '1000%', arrows: false, autoplay: true, }"
      aria-label="My Favorite Images" class="slide">
      <SplideSlide class="splide-inner" v-for="slide in slides" :key="slide.title">
        <div class="inner-wrapper">
          <iframe :src="slide.video_url" frameborder="0" width="100%" height="100%"></iframe>
          <h4>{{ slide.title }}</h4>
          <p>{{ slide.description.substr(0, 50) }}</p>
        </div>

      </SplideSlide>
    </Splide>
  </div>
</template>
<script setup>
import '@splidejs/vue-splide/css';

// or other themes
import '@splidejs/vue-splide/css/skyblue';
import '@splidejs/vue-splide/css/sea-green';

// or only core styles
import '@splidejs/vue-splide/css/core';

let url = 'http://127.0.0.1:8000/api/v1/latest-videos/'
const { data, pending } = await useLazyAsyncData('count', () => $fetch(url))
let slides = data.value
let perPage = ref(1);
let iWidth = ref("100%")

function checkingWidth() {
  if (window.innerWidth < 600) {
    perPage.value = 1
    iWidth.value = "300px"
  } else if (window.innerWidth < 1500) {
    perPage.value = 2
    iWidth.value = "350px"
  } else if (window.innerWidth < 1590) {
    perPage.value = 3
    iWidth.value = "350px"
  }
}


onMounted(() => {
  // checkingWidth()
})


</script>
<style lang="scss" scoped>
.wrapper {
  margin-top: -1rem;

  .splide-inner {

    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    width: 100%;
    // margin-left: 1rem;
    // margin-right: 1rem;


    .inner-wrapper {
      display: flex;
      justify-content: flex-start;
      align-items: flex-start;
      flex-direction: column;
      width: 70vw;
      height: 400px;

      @media (max-width:576px) {
        width: 95vw;
        height: 250px;
      }

      // margin-left: 1rem;
      // width: 80%;
      // aspect-ratio: 16/9;

      // iframe {
      // }

      h4 {
        color: var(--dark);
      }

      p {
        text-align: left;
      }
    }

  }

}


.heading {
  color: var(--bg);
}
</style>


