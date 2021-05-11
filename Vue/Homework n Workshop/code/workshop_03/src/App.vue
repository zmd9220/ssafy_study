<template>
  <div id="app">
    <h1>My First Youtube Project</h1>
    <SearchBar @search="onSearch" />
    <!-- <p> {{query}} </p> -->
  </div>
</template>

<script>
import axios from 'axios'
import SearchBar from '@/components/SearchBar.vue'

export default {
  name: 'App',
  components: {
    SearchBar,
  },
  data: function () {
    return {
      query: '',
      videoList: [],
    }
  },
  methods: {
    // Youtube API 로 데이터 요청
    onSearch: function (query) {
      // this.query = query
      const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
      // console.log(API_KEY)
      const API_URL = 'https://www.googleapis.com/youtube/v3/search'
      const params = {
        key: API_KEY,
        part: 'snippet',
        type: 'video',
        q: query,
      }
      axios({
      method: 'GET',
      url: API_URL,
      params,
      }).then(response => {
        // console.log(response)
        this.videoList = response.data.items
      }).catch(error => {
        console.log(error)
      })
    },

  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
