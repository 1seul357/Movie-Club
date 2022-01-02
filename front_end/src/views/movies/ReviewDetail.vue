<template>
<div v-if="review">
  <section :style="{ backgroundImage: 'url(' + moviePoster() + review.movie.backdrop_path + ')'}"> 
    <div class="container" style="overflow:auto; height:90%;">
      <div style="padding: 30px;">
        <h4><strong>{{ review.title }}</strong></h4>
        <p>작성자 : {{ review.user.username }} <a v-if="this.userpk==review.user.id" href="#" @click="deleteReview(review)">삭제</a></p> 
        <p class="mb-3">작성일 : {{ dateTime(review.created_at) }}</p>
        <div style="white-space:pre;">{{ review.content }}</div>
        <CommentList :review="review"/>
      </div>
    </div>
  </section>
</div>
</template>

<script>
import axios from 'axios'
import moment from 'moment';
import jwt_decode from 'jwt-decode'
import CommentList from '@/components/CommentList.vue'

const BACKEND = process.env.VUE_APP_SERVER_URL

export default {
  name: 'ReviewDetail',
  data: function() {
    return {
      review: null,
      userpk: null,
    }
  },
  components: {
    CommentList,
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    moviePoster() {
        return 'https://www.themoviedb.org/t/p/original'
    },
    getReview: function(review_pk) {
      axios({
        method: 'get',
        url: `${BACKEND}movies/review_detail/${review_pk}/`,
        headers: this.setToken()
      })
      .then(res => {
        console.log(res)
        this.review = res.data
      })
      .catch(err => {
        console.log(err)
      })
    },
    deleteReview: function (review) {
      axios({
        method: 'delete',
        url: `${BACKEND}movies/review_delete/${review.id}/`,
        headers: this.setToken()
      })
        .then(res => {
          console.log(res)
          this.$router.push({ name: 'MovieDetail', params: { movie_pk : review.movie.id }})
        })
        .catch(err => {
          console.log(err)
        })
    },
    dateTime(value) {
      return moment(value).format('YYYY-MM-DD HH:MM:SS');
    }
  },
  created: function () {
    if (localStorage.getItem('jwt')) {
      const token = localStorage.getItem('jwt')
      const decoded = jwt_decode(token)
      // console.log(decoded)
      this.userpk = decoded.user_id
      this.getReview(this.$route.params.review_pk)
    } else {
      this.$router.push({name: 'Login'})
    }
  }
}
</script>

<style scoped>
  section {
    background-size: cover;
    position: fixed;
    height: 100vh;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    z-index: 0;
  }
  .container {
    margin-top: 3rem;
    background-color:rgba(0, 0, 0, 0.7);
    width: 60%;
  }
  p {
    margin-bottom: 6px;
  }
  a {
  color: darkred;
  text-decoration: none;
  }
</style>