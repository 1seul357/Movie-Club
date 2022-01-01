<template>
  <div class="container">
    <MainMovieList :movies="suggested_movies"/>
    <b-button variant="link" id="show-btn" @click="showModal"><font-awesome-icon class="fa-lg" icon="search"/>오늘의 영화
    </b-button>
    <b-modal ref="my-modal" hide-footer title="오늘의 영화" hide-header-close>
    <div class="d-block text-center">
      <MovieCard :movies="today_movie"/>
    </div>
      <b-button class="mt-3" variant="btn btn-secondary" block @click="hideModal">Close</b-button>
    </b-modal>
    <SearchForm/>
    <h2>최신 영화</h2>
    <MovieList :movies="latest_movies"/>
    <h2>이번 겨울에는</h2>
    <MovieList :movies="random_season_movies"/>
    <h2>인기 영화</h2>
    <MovieList :movies="like_movies"/>
  </div>
</template>

<script>
import axios from 'axios'
import MovieList from '@/components/MovieList.vue'
import MainMovieList from '@/components/MainMovieList.vue'
import SearchForm from '@/components/SearchForm.vue'
import MovieCard from '@/components/MovieCard.vue'

const BACKEND = process.env.VUE_APP_SERVER_URL


export default {
  name: 'Index',
  components: {
    MovieList,
    MainMovieList,
    SearchForm,
    MovieCard,
  },
  data: function () {
    return {
      latest_movies: null,
      random_season_movies: null,
      like_movies: null,
      suggested_movies: null,
      today_movie: null,
    }
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    showModal() {
      this.$refs['my-modal'].show()
    },
    hideModal() {
      this.$refs['my-modal'].hide()
    },
    getMovies: function () {
      axios({
        method: 'get',
        url: `${BACKEND}movies/`,
        headers: this.setToken()
      })
        .then(res => {
          console.log(res)
          this.latest_movies = res.data[0]
          this.random_season_movies = res.data[1]
          this.like_movies = res.data[2]
          this.suggested_movies = res.data[3]
          this.today_movie = res.data[4]
        })
        .catch(err => {
          console.log(err)
        })
    },
  },
  created: function () {
    if (localStorage.getItem('jwt')) {
      this.getMovies()
    } else {
      this.$router.push({name: 'Login'})
    }
  }
}
</script>

<style scoped>
  h2 {
    font-family: 'Do Hyeon', sans-serif;
    margin-top: 1.5rem;
  }
  #show-btn {
    text-decoration: none;
    color: white;
    margin-top: 3rem;
    font-size: 20px;
  }
  .modal {
    font-family: 'Do Hyeon', sans-serif;
  }
</style>