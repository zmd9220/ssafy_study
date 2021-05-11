<template>
  <li class="video-list-item" @click="onVideoClick">
    <img :src="video.snippet.thumbnails.default.url" alt="youtube-thumbnail-image">
    <!-- <span>{{ video.snippet.title | unescape }}</span> -->
    <!-- <span>{{ unescape(video.snippet.title)  }}</span> -->
    <span>{{ videoTitle }}</span>
  </li>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'VideoListItem',
  props: {
    video: {
      type: Object,
    }
  },
  // filters: {
  //   unescape: function (text) {
  //     return _.unescape(text)
  //   }
  // },
  computed: {
    videoTitle: function () {
      return _.unescape(this.video.snippet.title)
    }
  },
  methods: {
    onVideoClick: function() {
      return this.$emit('select-video', this.video)
    },
  },
}
</script>

<style>
.video-list-item {
  display: flex;        /* 가로 배치 및 flex의 CSS 적용 */
  margin-bottom: 1rem;  /* item의 상하 여백 */
  cursor: pointer;      /* 마우스를 포인터로 변경 */
}
.video-list-item:hover {
  background: #eee;
}
.video-list-item img {
  height: fit-content;   /* 텍스트가 길어져도 이미지는 늘어나지 않게 설정 */
  margin-right: 0.5rem;  /* 이미지와 텍스트 사이의 여백 */
}
</style>