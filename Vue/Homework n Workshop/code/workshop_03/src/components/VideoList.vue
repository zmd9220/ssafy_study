<template>
  <ul id="video-list">
    <!-- for문의 key는 항상 유니크한 값 -->
    <VideoListItem 
      v-for="video in videoList"
      :key="video.etag" 
      :video="video"
      @select-video="onSelectVideo"
    />
  </ul>
</template>

<script>
import VideoListItem from '@/components/VideoListItem.vue'

export default {
  name: 'VideoList',
  props: {
    videoList: {
      type: Array,
      required: true,
    }
  },
  components: {
    VideoListItem,
  },
  methods: {
  onSelectVideo: function(video) {
    return this.$emit('select-video', video)
    }
  }
}
</script>

<style>
#video-list {
  /* 기본 margin, padding, 그리고 list-style 속성 초기화 */
  padding: 0;
  margin: 0;
  list-style-type: none;
  width: 30%; /* Detail, List의 7:3 가로비율 설정*/
}
</style>