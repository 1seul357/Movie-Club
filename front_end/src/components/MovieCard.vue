<template>
  <div class="d-flex row justify-content-center">
    <b-card v-for="movie in movies" :key="movie.id"
      :title="movie.title"
      :img-src="moviePoster + movie.poster_path"
      img-alt="Image"
      img-top
      tag="article"
      style="width: 17rem; border: 1px solid black;"
      class="mb-4"
    >
    <b-card-text>
      <p>개봉일 | {{ movie.release_date }}</p>
    </b-card-text>
    </b-card>
  </div>
</template>

<script>
export default {
  name: 'MovieCard',
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
}
</script>

<style scoped>
</style>