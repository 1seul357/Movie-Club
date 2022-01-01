<template>
  <div class="d-flex flex-wrap">
    <div v-for="movie in movies" :key="movie.id">
      <router-link :to="{ name: 'MovieDetail', params: { movie_pk : movie.id }}">
        <img 
          :src="moviePoster + movie.poster_path" alt="" 
          style="width: 210px; height: 300px;"
          class="ms-1 mb-2"
        >
      </router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MyMovieList',
  props: {
    movies: {
      type: Array,
    }
  },
  computed: {
    moviePoster() {
      return 'https://www.themoviedb.org/t/p/w300_and_h450_bestv2'
    }
  },
}
</script>

<style scoped>
  img:hover{ 
    transform:scale(1.1);
    box-shadow: 0 0 20px grey;
  }
</style>