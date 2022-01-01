<template>
  <div>
    <div class="form">
      <b-form-input 
      type="text" 
      id="input_data"
      placeholder="검색어를 입력해주세요."
      v-model="data.input_data"
      @keyup.enter="search"
      ></b-form-input>
      <b-button class="button-effect" @click="search">검색</b-button>
    </div>
    <div v-if="movies">
      <h2>검색결과</h2>
      <h5>총 {{ movies.length }}개의 영화를 찾았습니다.</h5>
    </div>
    <MovieList :movies="movies"/>
  </div>
</template>

<script>
import axios from 'axios'
import MovieList from '@/components/MovieList.vue'

const BACKEND = process.env.VUE_APP_SERVER_URL

export default {
  name: 'SearchForm',
  data: function () {
    return {
      data: {
        input_data: null,
      },
      movies: null,
    }
  },
  components: {
    MovieList,
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    search: function () {
      axios({
        method: 'post',
        url: `${BACKEND}movies/search/`,
        headers: this.setToken(),
        data: this.data
      })
        .then(res => {
          console.log(res)
          this.movies = res.data
          this.input_data = null
        })
        .catch(err => {
          console.log(err)
        })
    }
  },
  created: function () {
    const token = localStorage.getItem('jwt')
    if (token) {
      this.isLogin = true
    }
  }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Black+Han+Sans&family=Do+Hyeon&family=Nanum+Gothic:wght@400;700;800&display=swap');
  h2 {
    font-family: 'Do Hyeon', sans-serif;
  }
  h5 {
    font-family: 'Nanum Gothic', sans-serif;
  }
  .form {
    display: -webkit-flex;
    display: -moz-flex;
    display: -ms-flexbox;
    display: -o-flex;
    display: flex;
    justify-content: center;
    padding: 10px;
    margin-top: 1rem;
  }
  input {
    width: 80%;
    margin-right: 1rem;
  }
  button {
    background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
    color: white;
  }
  button:hover{ 
    transform:scale(1.1);
    box-shadow: 0 0 20px grey;
  }
  .button-effect {
    background-size: 400% 400%;
    animation: gradient1 5s ease infinite;
  }
  @keyframes gradient1 {
    0% {
        background-position: 0% 50%;
    }
    50% {
        background-position: 100% 50%;
    }
    100% {
        background-position: 0% 50%;
    }
  }
</style>