<template>
  <div>
    <div class="form">
      <b-form-input
        id="input-1"
        v-model="content"
        type="text"
        placeholder="input comment"
        required
        @keyup.enter="createComment(review)"
      ></b-form-input>
      <b-button @click="createComment(review)" id="show-btn">작성</b-button>
    </div>
    <div v-if="comments" class="comments">
      <h2>Comments</h2>
      <p>총 {{ comments.length }}개의 댓글이 있습니다.</p>
      <hr>
      <div v-for="comment in comments" :key="comment.pk">
        <div class="box">
          {{ comment.user.username }} : 
          {{ comment.content }}
          <a v-if="userid==comment.user.id" href="#" @click="deleteComment(comment)">삭제</a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import jwt_decode from 'jwt-decode'

const BACKEND = process.env.VUE_APP_SERVER_URL

export default {
  name: 'CommentList',
  data: function () {
    return {
      content: null,
      comments: null,
    }
  },
  props : {
    review: {
      type: Object,
    },
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    getComments: function () {
      axios({
        method: 'get',
        url: `${BACKEND}movies/review/comment_list/${this.review.id}/`,
        headers: this.setToken(),
      })
      .then(res => {
        console.log(res)
        this.comments = res.data
      })
      .catch(err => {
        console.log(err)
      })
    },
    createComment: function (review) {
      const createItem = {
        content: this.content,
      }
      axios({
        method: 'post',
        url: `${BACKEND}movies/review/comment_create/${review.id}/`,
        headers: this.setToken(),
        data: createItem,
      })
      .then(res => {
        console.log(res)
        this.content = res.data
        this.content = null,
        this.getComments()
      })
      .catch(err => {
        console.log(err)
      })
    },
    deleteComment: function (comment) {
      axios({
        method: 'delete',
        url: `${BACKEND}movies/review/comment_delete/${comment.id}/`,
        headers: this.setToken()
      })
        .then(res => {
          console.log(res)
          this.getComments()
        })
        .catch(err => {
          console.log(err)
        })
    },
  },
  created: function () {
    if (localStorage.getItem('jwt')) {
      this.getComments()
      const token = localStorage.getItem('jwt')
      const decoded = jwt_decode(token)
      // console.log(decoded)
      this.userid = decoded.user_id
    } else {
      this.$router.push({name: 'Login'})
    }
  }
}
</script>

<style scoped>
  button {
    text-decoration: none;
    color: darkred;
  }
  input {
    width: 80%;
    margin-right: 1rem;
  }
  .form {
    display: -webkit-flex;
    display: -moz-flex;
    display: -ms-flexbox;
    display: -o-flex;
    display: flex;
    justify-content: center;
    padding: 10px;
    top: 8rem;
    position: relative;
  }
  #show-btn {
    background: linear-gradient(-45deg, #ee0e76, #4a4ce9, #990fb4, #58b0eb);
    color: white;
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
  h2 {
    font-family: 'Do Hyeon', sans-serif;
    margin-bottom: 1rem;
    color: antiquewhite;
  }
  .box {
    display: flex;
    justify-content: space-between;
    margin-bottom: 7px;
  }
  .comments {
    position: relative;
    top: 10rem;
  }
  a {
  color: darkred;
  text-decoration: none;
  }
</style>