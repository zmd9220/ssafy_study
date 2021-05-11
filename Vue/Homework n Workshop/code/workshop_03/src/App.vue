<template>
  <div id="app">
    <header>
      <SearchBar @search="onSearch" :video-length="videoList.length" />
    </header>
    <!-- <h1>My First Youtube Project</h1> -->
    <!-- <p> {{query}} </p> -->
    <section>
      <VideoDetail :selectedVideo="selectedVideo" />
      <VideoList :videoList="videoList" @select-video="onSelectVideo" />
    </section>
  </div>
</template>

<script>
import axios from 'axios'
import SearchBar from '@/components/SearchBar.vue'
import VideoList from '@/components/VideoList.vue'
import VideoDetail from '@/components/VideoDetail.vue'


export default {
  name: 'App',
  components: {
    SearchBar,
    VideoList,
    VideoDetail,
  },
  data: function () {
    return {
      // query: '',
      videoList: [],
      selectedVideo: null,
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
        if(!this.selectedVideo) {
          this.selectedVideo = this.videoList[0]
        }
      }).catch(error => {
        console.log(error)
      })
    },
    onSelectVideo: function (video){
      this.selectedVideo = video
    }
  },
}
</script>

<style>
header, section {
  width: 80%;
  margin: 0 auto;   /** 양 옆 margin을 균등하게 배분 (가운데 정렬) */
  padding: 1rem 0;  /** 위, 아래 padding */
}
section {
  display: flex; /** 가로 배치 */
}

</style>
