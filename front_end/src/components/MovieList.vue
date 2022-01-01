<template>
  <div class="container">
    <swiper class="swiper-wrapper" :options="swiperOption">
      <swiper-slide v-for="movie in movies" :key="movie.id">
        <router-link :to="{ name: 'MovieDetail', params: { movie_pk : movie.id }}">
          <img 
            :src="moviePoster + movie.poster_path" alt="" 
            style="width: 210px; height: 300px;"
          >
        </router-link>
        <p>{{ movie.title }}</p>
      </swiper-slide>
    </swiper>
  </div>
</template>

<script>
import Vue from "vue";
import { Swiper, SwiperSlide } from "vue-awesome-swiper"
import "swiper/css/swiper.css";

export default Vue.extend({
  name: 'MovieList',
  components: {
    Swiper,
    SwiperSlide,
  },
  props : {
    movies: {
      type: Array,
    },
  },
  data() {
    return {
      swiperOption: {
        slidesPerView: 5,
        spaceBetween: 0,
        breakpoints: {
          1400: {
            slidesPerView: 6,
            spaceBetween: 0,
          },
          1200: {
            slidesPerView: 5,
            spaceBetween: 10
          },
          1000: {
            slidesPerView: 4,
            spaceBetween: 10,
          },
          750: {
            slidesPerView: 3,
            spaceBetween: 10,
          },
          500: {
            slidesPerView: 2,
            spaceBetween: 10,
          }
        }
      }
    };
  },
  computed: {
    moviePoster() {
      return 'https://www.themoviedb.org/t/p/w300_and_h450_bestv2'
    }
  },
});
</script>

<style scoped>
</style>