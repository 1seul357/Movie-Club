<template>
  <div class="example-3d">
    <swiper class="swiper" :options="swiperOption">
      <swiper-slide v-for="movie in movies" :key="movie.id">
        <router-link :to="{ name: 'MovieDetail', params: { movie_pk : movie.id }}">
        <img :src="moviePoster + movie.poster_path" alt="">
        </router-link>
      </swiper-slide>
    </swiper>
  </div>
</template>

<script>
import Vue from "vue";
import { Swiper, SwiperSlide } from 'vue-awesome-swiper'
import 'swiper/css/swiper.css'

export default Vue.extend({
  name: 'MainMovieList',
  components: {
    Swiper,
    SwiperSlide
  },
  props : {
    movies: {
      type: Array,
    },
  },
  computed: {
    moviePoster() {
      return 'https://www.themoviedb.org/t/p/w300_and_h450_bestv2'
    }
  },
  data() {
    return {
      swiperOption: {
        effect: 'coverflow',
        slidesPerView: '3',
        loop: true,
        spaceBetween: 6,
        slidesOffsetBefore: 0,
        slidesOffsetAfter: 0,
        freeMode: true,
        centerInsufficientSlides: true,
        breakpoints: {
          1400: {
            slidesPerView: 4,
            spaceBetween: 10
          }
        },
      }
    }
  },
});
</script>