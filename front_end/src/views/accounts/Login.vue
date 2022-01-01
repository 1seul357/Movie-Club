<template>
  <section>
    <div class="container">
      <h2>Login</h2>
      <div class="form">
        <b-form-input 
          type="text" 
          id="username"
          placeholder="Username"
          rows="3"
          v-model="credentials.username"
        >
        </b-form-input>
        <b-form-input 
          type="password" 
          id="password"
          placeholder="Password"
          v-model="credentials.password"
          @keyup.enter="login"
        >
        </b-form-input>
        <b-button @click="login">Login</b-button>
        <div class="signup">
          Didn't you have ID? &nbsp;&nbsp; 
          <router-link :to="{ name: 'Signup' }">Sign up</router-link>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import axios from 'axios'

const BACKEND = process.env.VUE_APP_SERVER_URL

export default {
  name: 'Login',
  data: function () {
    return {
      credentials: {
        username: null,
        password: null,
      },
    }
  },
  methods: {
    login: function () {
      axios({
        method: 'post',
        url: `${BACKEND}accounts/api-token-auth/`,
        data: this.credentials,
      })
        .then(res => {
          console.log(res)
          localStorage.setItem('jwt', res.data.token)
          this.$emit('login')
          this.$router.push({ name: 'Index'})
        })
        .catch(err => {
          alert("사용자 정보를 확인해주세요!")
          console.log(err)
          console.log(process.env)
        })
    }
  }
}
</script>

<style scoped>
  section {
    background-image: url('assets/movie_theater.jpg');
    display: flex;
    align-items: center;
    background-size: 100% 100%;
    position: fixed;
    padding: 40px 40px;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    z-index: 0;
  }
  .container {
    width: 350px;
    height: 400px;
    background-color: white;
    color: black;
  }
  .form {
    padding: 40px;
    width: 100%;
  }
  button {
    width: 100%;
    margin-top: 2rem;
    background-color: rgb(119, 14, 14);
  }
  button:hover {
    background-color: rgb(119, 14, 14);
    transform:scale(1.1);
  }
  input {
    margin-bottom: 1rem;
  }
  a {
    text-decoration: none;
    color: rgb(14, 144, 196);
  }
  .signup {
    margin-top: 4rem;
    display: flex;
    justify-content: flex-end; 
  }
  h2 {
    text-align: center;
    margin-top: 1rem;
    font-family: 'Black Han Sans', sans-serif;
  }
</style>