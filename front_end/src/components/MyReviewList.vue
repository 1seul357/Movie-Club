<template>
<div>  
  <h5 class="mt-2" style="text-align: center;">총 {{ reviews.length }}개의 리뷰를 작성했습니다.</h5>
  <div class="cards d-flex flex-wrap justify-content-center">
    <div v-for="review in reviews" :key="review.id">
      <b-card
        :img-src="moviePoster + review.movie.backdrop_path"
        img-alt="Image"
        img-top
        tag="article"
        style="max-width: 16rem; height: 22rem;"
        class="card mb-4 ms-3 mt-2"
      >
        <b-card-text>
          <p style="font-size: 17px;"><strong>{{ review.movie.title }}</strong></p>
          <div class="mt-4">
            <p>제목 : {{ review.title }}</p>
            <p>작성일 : {{ dateTime(review.created_at) }} </p>
            <div class="star-ratings">
              <div 
                class="star-ratings-fill space-x-2 text-lg"
                :style="{ width: review.rank*10 + '%' }"
              >
                <span><font-awesome-icon class="fa-1x" icon="star"/></span>
                <span><font-awesome-icon class="fa-1x" icon="star"/></span>
                <span><font-awesome-icon class="fa-1x" icon="star"/></span>
                <span><font-awesome-icon class="fa-1x" icon="star"/></span>
                <span><font-awesome-icon class="fa-1x" icon="star"/></span>
              </div>
              <div class="star-ratings-base space-x-2 text-lg">
                <span><font-awesome-icon class="fa-1x" icon="star"/></span>
                <span><font-awesome-icon class="fa-1x" icon="star"/></span>
                <span><font-awesome-icon class="fa-1x" icon="star"/></span>
                <span><font-awesome-icon class="fa-1x" icon="star"/></span>
                <span><font-awesome-icon class="fa-1x" icon="star"/></span>
              </div>
            </div>
            <b-button @click="reviewDetail(review)" class="mt-3">Detail</b-button>
          </div>
        </b-card-text>
      </b-card>
    </div>
  </div>
</div>
</template>

<script>
import moment from 'moment';

export default {
  name: 'MyReviewList',
  props: {
    reviews: {
      type: Array,
    }
  },
  computed: {
    moviePoster() {
      return 'https://www.themoviedb.org/t/p/original'
    }
  },
  methods: {
    dateTime(value) {
      return moment(value).format('YYYY-MM-DD');
    },
    reviewDetail: function(review) {
      this.$router.push({ name: 'ReviewDetail', params: { review_pk : review.id }})
    }
  }
}
</script>

<style scoped>
  .card {
    background-color: white;
    color: black;
  }
  .star-ratings {
    color: #aaa9a9; 
    position: relative;
    unicode-bidi: bidi-override;
    width: max-content;
    -webkit-text-fill-color: transparent; /* Will override color (regardless of order) */
    -webkit-text-stroke-width: 1.3px;
    -webkit-text-stroke-color: #2b2a29;
  }
  .star-ratings-fill {
    color: #f5e108;
    padding: 0;
    position: absolute;
    z-index: 1;
    display: flex;
    top: 0;
    left: 0;
    overflow: hidden;
    -webkit-text-fill-color: gold;
  }
  .star-ratings-base {
    z-index: 0;
    padding: 0;
  }
  p {
    margin-bottom: 3px;
  }
  button {
    background-color: rgb(212, 30, 91);
    border-color: rgb(212, 30, 91);
  }
  button:hover {
    background-color: black;
    border-color: black;
  }
</style>