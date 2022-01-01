<template>
  <section> 
    <div class="container">
      <h2>Sign up</h2>
      <div class="form">
        <p v-if="message">{{ message }}</p>
        <b-form-input 
          type="text" 
          id="username"
          placeholder="Username"
          v-model="credentials.username"
        >
        </b-form-input >
        <b-form-input 
          type="password"
          id="password"
          placeholder="Password"
          v-model="credentials.password"
        >
        </b-form-input >
        <b-form-input  
          type="password" 
          id="passwordConfirmation"
          placeholder="Password Confirmation"
          v-model="credentials.passwordConfirmation"
          @keyup.enter="signup"
        >
        </b-form-input >
        <b-button @click="signup">Submit</b-button>
      </div>
    </div>
  </section>
</template>

<script>
import axios from 'axios'

const BACKEND = process.env.VUE_APP_SERVER_URL

export default {
  name: 'Signup',
  data: function () {
    return {
      credentials: {
        username: null,
        password: null,
        passwordConfirmation: null,
      },
      message: null,
    }
  },
  methods: {
    signup: function () {
      axios({
        method: 'post',
        url: `${BACKEND}accounts/signup/`,
        data: this.credentials
      })
        .then(() => {
          // console.log(res)
          this.$router.push({ name: 'Login'})
        })
        .catch(err => {
          if (err.response.data.error)
            alert(err.response.data.error)
          if (err.response.data.pass_error)
            alert(err.response.data.pass_error)
          else
            alert(err.response.data.username)
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
  h2 {
    text-align: center;
    margin-top: 1rem;
    font-family: 'Black Han Sans', sans-serif;
  }
</style>