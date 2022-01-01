<template>
  <div v-if="movie" class="container">
    <div class="row">
      <section class="col-4">
        <img :src="moviePoster + movie.poster_path" alt="">
      </section>
      <section class="col-8">
        <h2><strong>{{ movie.title }}</strong></h2>
        <p><strong>Release_date </strong> | {{ movie.release_date }}</p>
        <p><strong>Vote_average </strong> | {{ movie.vote_average }}</p>
        <p><strong>Genre </strong> | {{ movie.genre }}</p>
        <p><strong>Popularity </strong> | {{ movie.popularity }}</p>
        <p class="mt-3">{{ movie.overview }}</p>
      </section>
    </div>
    <div class="heart">
      <div v-if="movie.like_users.includes(userpk)">
        <font-awesome-icon @click="like_movie(movie)" class="heart-icon fa-2x" style="color: red;" icon="heart"/>
      </div>
      <div v-else>
        <font-awesome-icon @click="like_movie(movie)" class="heart-icon fa-2x" icon="heart"/>
      </div>
      <p>{{ movie.like_users.length }} likes</p>
    </div>
    <ReviewList :movie="movie"/>
  </div>
  
</template>

<script>
import axios from 'axios'
import ReviewList from '@/components/ReviewList.vue'
import jwt_decode from 'jwt-decode';

const BACKEND = process.env.VUE_APP_SERVER_URL

export default {
  name: 'MovieDetail',
  components: {
    ReviewList,
  },
  data: function() {
    return {
      movie: null,
      userpk: null,
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
    getMovie: function (movie_pk) {
      axios({
        method: 'get',
        url: `${BACKEND}movies/${movie_pk}/`,
        headers: this.setToken()
      })
      .then(res => {
        console.log(res)
        this.movie = res.data
      })
      .catch(err => {
        console.log(err)
      })
    },
    like_movie: function (movie) {
      axios({
        method: 'post',
        url: `${BACKEND}movies/${movie.id}/likes/`,
        headers: this.setToken()
      })
      .then(res => {
        console.log(res)
        this.getMovie(this.movie.id)
      })
      .catch(err => {
        console.log(err)
      })
    },
  },
  computed: {
    moviePoster() {
      return 'https://www.themoviedb.org/t/p/w300_and_h450_bestv2'
    }
  },
  created: function () {
    if (localStorage.getItem('jwt')) {
      const token = localStorage.getItem('jwt')
      const decoded = jwt_decode(token)
      // console.log(decoded)
      this.userpk = decoded.user_id
      this.getMovie(this.$route.params.movie_pk)
    } else {
      this.$router.push({name: 'Login'})
    }
  }
}
</script>

<style scoped>
  .container {
    min-height: 100vh;
  }
  img {
    box-shadow: 5px 5px 10px grey;
    margin-left: 3rem;
  }
  h2 {
    margin-bottom: 1.5rem;
  }
  p {
    margin: 6px;
  }
  .heart {
    display: flex;
    justify-content: flex-end;
    padding: 5px;
  }
  .heart-icon:hover {
    transform:scale(1.2);
  }
</style>