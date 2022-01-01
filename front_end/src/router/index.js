import Vue from 'vue'
import VueRouter from 'vue-router'
import Signup from '@/views/accounts/Signup'
import Login from '@/views/accounts/Login'
import Index from '@/views/movies/Index'
import MovieDetail from '@/views/movies/MovieDetail'
import ReviewDetail from '@/views/movies/ReviewDetail'
import Profile from '@/views/accounts/Profile'


Vue.use(VueRouter)

const routes = [
  {
    path: '/accounts/signup',
    name: 'Signup',
    component: Signup,
  },
  {
    path: '/accounts/login/',
    name: 'Login',
    component: Login,
  },
  {
    path: '/accounts/profile/',
    name: 'Profile',
    component: Profile,
  },
  {
    path: '/',
    name: 'Index',
    component: Index,
  },
  {
    path: '/movies/:movie_pk',
    name: 'MovieDetail',
    component: MovieDetail,
  },
  {
    path: '/movies/review_detail/:review_pk',
    name: 'ReviewDetail',
    component: ReviewDetail,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
