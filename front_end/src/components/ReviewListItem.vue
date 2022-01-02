<template>
  <div class="container">
    <router-link :to="{ name: 'ReviewDetail', params: { review_pk : review.id }}">
      <div class="box">
        <p>
          ID : {{ review.user.username }} / 
          Date : {{ dateTime(review.created_at) }}
        </p>
        <div class="box1">
          <strong>{{ review.title }}</strong>
          <div class="star-ratings">
            <div 
              class="star-ratings-fill space-x-2 text-lg"
              :style="{ width: this.review.rank*10 + '%' }"
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
        </div>
      </div>
    </router-link>
  </div>
</template>

<script>
import moment from 'moment';

export default {
  name: 'ReviewListItem',
  props : {
    review: {
      type: Object,
    },
  },
  methods : {
    dateTime(value) {
      return moment(value).format('YYYY-MM-DD');
    }
  }
}
</script>

<style scoped>
  .box {
    border: 3px solid palevioletred;
    margin-left: 2rem;
    margin-top: 1rem;
    color: white;
    padding: 15px;
  }
  .container a {
    text-decoration: none;
  }
  .box1 {
    display: flex;
    justify-content: space-between;
  }
  .box:hover{ 
    transform:scale(1.1);
    box-shadow: 0 0 20px grey;
  }
  .star-ratings {
    color: #aaa9a9; 
    position: relative;
    unicode-bidi: bidi-override;
    width: max-content;
    -webkit-text-fill-color: transparent;
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
</style>