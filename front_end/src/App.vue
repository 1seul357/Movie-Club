<template>
  <div id="app">
    <div id="navbar">
      <h4 class="main">MOVIE CLUB</h4>
      <div id="nav">
        <span v-if="isLogin">
          <router-link :to="{ name: 'Index' }">Movie</router-link>&nbsp; 
          <router-link :to="{ name: 'Profile' }">Profile</router-link>&nbsp; 
          <router-link @click.native="logout" to="#">Logout</router-link>
        </span>
        <span v-else>
          <router-link :to="{ name: 'Signup' }">Signup</router-link>&nbsp; 
          <router-link :to="{ name: 'Login' }">Login</router-link>
        </span>
      </div>
    </div>
    <router-view @login="isLogin = true"/>
  </div>
</template>

<script>
export default {
  name: 'App',
  data: function () {
    return {
      isLogin: false,
    }
  },
  methods: {
    logout: function () {
      this.isLogin = false
      localStorage.removeItem('jwt')    // 토큰 값 삭제
      this.$router.push({name: 'Login'})
    },
  },
  created: function () {
    const token = localStorage.getItem('jwt')
    if (token) {
      this.isLogin = true
    }
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Black+Han+Sans&family=Do+Hyeon&family=Nanum+Gothic:wght@400;700;800&display=swap');

#app {
  font-family: 'Nanum Gothic', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  background-color: black;
  color: white;
  min-height: 100vh;
}
#navbar {
  display: flex;
  justify-content: space-between;
  padding: 20px;
  font-family: 'Black Han Sans', sans-serif;
  position: relative;
  z-index: 99;
}
#nav a {
  font-weight: bold;
  color: white;
  text-decoration: none;
}
#nav a.router-link-exact-active {
  color: #e73c7e;
}
.main {
  background: linear-gradient(-45deg, #ee7752, #e73c7e, #9d23d5, #23d5ab);
}
.main {
  background: linear-gradient(-45deg, #ee7752, #e73c7e, #9d23d5, #23d5ab);
  color: transparent;
  -webkit-background-clip: text;
  -moz-background-clip: text;
}
</style>
