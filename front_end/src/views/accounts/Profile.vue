<template>
  <div class="container">
    <p>{{ username }}</p>
    <div class="d-flex justify-content-center">
      <a href="#" @click="getLikeMovies">My List</a>
      <a href="#" @click="getFavorite">My Favorite</a>
      <a href="#" @click="getReviews">My Review</a>
    </div>
    <div v-if="isShow1">
      <div v-if="like_movies">
        <h5 class="mt-2 mb-3" style="text-align: center;">총 {{ like_movies.length }}개의 영화를 찜했습니다.</h5>
        <MyMovieList :movies="like_movies"/>
      </div>
    </div>
    <div v-if="isShow2">
      <div v-if="genre_movies">
        <h5 class="mt-2 mb-3" style="text-align: center;">가장 좋아하는 장르는 {{ genre_movies[0].genre }}입니다.</h5>
        <MyMovieList :movies="genre_movies"/>
      </div>  
      <div v-else>
        <h5 class="mt-2 mb-3" style="text-align: center;">좋아하는 영화 장르가 없습니다.</h5>
      </div>
    </div>
    <MyReviewList v-if="isShow3" :reviews="write_reviews"/>
  </div>
</template>

<script>
import axios from 'axios'
import jwt_decode from 'jwt-decode'
import MyReviewList from '@/components/MyReviewList.vue'
import MyMovieList from '@/components/MyMovieList.vue'

const BACKEND = process.env.VUE_APP_SERVER_URL

export default {
  name: 'Profile',
  data: function() {
    return {
      like_movies: null,
      genre_movies: null,
      write_reviews: null,
      isShow1: false,
      isShow2: false,
      isShow3: false,
      username: null,
    }
  },
  components: {
    MyReviewList,
    MyMovieList,
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    getProfile: function () {
      axios({
        method: 'get',
        url: `${BACKEND}accounts/profile/`,
        headers: this.setToken()
      })
      .then(res => {
        console.log(res)
        this.like_movies = res.data[0]
        this.write_reviews = res.data[1]
        this.genre_movies = res.data[2]
      })
      .catch(err => {
        console.log(err)
        console.log(BACKEND)
      })
    },
    getLikeMovies: function () {
      this.isShow1 = true,
      this.isShow2 = false,
      this.isShow3 = false
    },
    getFavorite: function () {
      this.isShow1 = false,
      this.isShow2 = true,
      this.isShow3 = false
    },
    getReviews: function () {
      this.isShow1 = false,
      this.isShow2 = false,
      this.isShow3 = true
    }
  },
  created: function () {
    if (localStorage.getItem('jwt')) {
      this.getProfile()
      const token = localStorage.getItem('jwt')
      const decoded = jwt_decode(token)
      // console.log(decoded)
      this.username = decoded.username
      this.isShow1 = true
    } else {
      this.$router.push({name: 'Login'})
    }
  }
}
</script>

<style scoped>
  a {
    color: palevioletred;
    text-decoration: none;
    font-size: 1.5rem;
    margin-left: 25px;
    font-family: 'Black Han Sans', sans-serif;
  }
  p {
    font-family: 'Black Han Sans', sans-serif;
    font-size: 4rem;
    text-align: center;
  }
</style>