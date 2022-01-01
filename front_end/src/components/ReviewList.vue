<template>
<div class="container">
  <div>
    <b-button class="button-effect" id="show-btn" @click="showModal">리뷰 쓰기</b-button>
    <b-modal ref="my-modal" hide-footer title="Create Review" hide-header-close>
      <div class="d-block">
        <div class="container">
        <b-form @submit="createReview(movie)">
          <b-form-group
            id="input-group-1"
            label="title"
            label-for="input-1"
          >
            <b-form-input
              id="input-1"
              v-model="title"
              type="text"
              placeholder="input title"
              required
            ></b-form-input>
          </b-form-group>
          <b-form-group id="input-group-2" label="content" label-for="input-2">
            <b-form-textarea
              id="input-2"
              v-model="content"
              type="text"
              rows="8"
              placeholder="input content"
              required
            ></b-form-textarea>
          </b-form-group>
          <b-form-group id="input-group-3" label="rank" label-for="input-3">
            <b-form-input
              id="input-3"
              v-model="rank"
              type="number"
              required
            ></b-form-input>
          </b-form-group>
          <div class="mt-3">
            <b-button type="submit" variant="btn btn-primary">Create</b-button>
            <b-button variant="btn btn-secondary" class="ms-1" @click="hideModal">Close</b-button>
          </div>
        </b-form>
        </div>
      </div>
    </b-modal>
  </div>
  <p v-for="review in reviews" :key="review.id">
    <ReviewListItem :review="review"/>
  </p>
</div>
</template>

<script>
import axios from 'axios';
import ReviewListItem from '@/components/ReviewListItem.vue'

const BACKEND = process.env.VUE_APP_SERVER_URL

export default {
  name: 'ReviewList',
  props : {
    movie: {
      type: Object,
    },
  },
  components: {
    ReviewListItem,
  },
  data: function() {
    return {
      reviews: null,
      title: null,
      content: null,
      rank: null,
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
    getReviews: function() {
      axios({
        method: 'get',
        url: `${BACKEND}movies/review_list/${this.movie.id}/`,
        headers: this.setToken()
      })
      .then(res => {
        console.log(res)
        this.reviews = res.data
      })
      .catch(err => {
        console.log(err)
      })
    },
    createReview: function(movie) {
      const reviewItem = {
        content: this.content,
        rank: this.rank,
        title: this.title,
      }
      if (reviewItem.content) {
        axios({
          method: 'post',
          url: `${BACKEND}movies/review_create/${movie.id}/`,
          data: reviewItem,
          headers: this.setToken()
        })
        .then(res => {
          console.log(res)
          this.content = null,
          this.rank = null,
          this.title = null
        })
        .catch(err => {
          console.log(err)
        })
      }
    },
  },
  created: function () {
    if (localStorage.getItem('jwt')) {
      this.getReviews()
    } else {
      this.$router.push({name: 'Login'})
    }
  }
}
</script>

<style scoped>
  #show-btn {
    background: linear-gradient(-45deg, #df4338, #4a4ce9, #990fb4, #4712c2);
    color: white;
    margin-left: 3rem;
  }
  #show-btn:hover{ 
    transform:scale(1.1);
    box-shadow: 0 0 20px grey;
  }
  #show-btn {
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