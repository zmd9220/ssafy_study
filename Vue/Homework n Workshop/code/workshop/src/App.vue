<template>
  <div id="app">
    <h1>App</h1>
    <input type="text" v-model="appData">
    <p>parentData: {{ parentData }}</p>
    <p>childData: {{ childData }}</p>
    <!-- 3. 사용하기 -->
    <Parent :appData="appData" @child-input="onChildInput" @parent-input="onParentInput" />
  </div>
</template>

<script>
// 1. 불러오기
import Parent from '@/components/Parent.vue'

export default {
  name: 'App',
  // 양방향 바인딩, 데이터를 받을 함수 데이터 지정 (꼭 함수 형태여야함)
  data: function () {
    return {
      appData: '',
      childData: '',
      parentData: '',
    }
  },
  components: {
    // 2. 등록하기
    Parent,
  },
  methods: {
    onParentInput: function (parentData) {
      this.parentData = parentData
    },
    onChildInput: function (childData) {
      // console.log('child input @ App.vue')
      this.childData = childData
    },
  }
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

  /* 추가 */
  width: 500px;
  margin: 0 auto;
  border: 1px solid black  
}
</style>
