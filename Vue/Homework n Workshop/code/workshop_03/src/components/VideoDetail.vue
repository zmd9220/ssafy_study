<template>
  <div v-if="selectedVideo" id="video-detail">
    <!-- <img :src="selectedVideo.snippet.thumbnails.high.url" alt="youtube-thumbnail-image">
    <p>{{ videoTitle }}</p> -->
    <div class="video-container">
      <iframe 
        id="ytplayer" 
        type="text/html"
        :src="videoURI"
        frameborder="0">
      </iframe>
    </div>
    <hr>
    <h2>{{ videoTitle }}</h2>
    <p>{{ videoDescription }}</p>
  </div>
  
</template>

<script>
import _ from 'lodash'

export default {
  name: 'VideoDetail',
  props: {
    selectedVideo: {
      type: Object,
    }
  },
  computed: {
    videoTitle: function () {
      return _.unescape(this.selectedVideo.snippet.title)
    },
    videoDescription: function () {
      return _.unescape(this.selectedVideo.snippet.description)
    },
    videoURI: function () {
      const videoId = this.selectedVideo.id.videoId
      return `https://www.youtube.com/embed/${videoId}`
    }
  },
}
</script>

<style>
#video-detail {
  width: 70%;           /* Detail, List를 전체 가로 비율 대비 7:3으로 설정 */
  padding-right: 1rem;  /* Detail과 List 사이의 margin */
}
.video-container {
  position: relative;   /* iframe을 container를 기준으로 위치를 지정 */
  padding-top: 56.25%;  /* 유튜브 비디오 비율을 맞추기 위한 높이 설정 */
}
.video-container > iframe {
  position: absolute;   /* container를 기준으로 위치를 지정*/
  top: 0;               /* container의 가장 위쪽으로 위치를 지정 */
  left: 0;
  width: 100%;
  height: 100%;
}
</style>