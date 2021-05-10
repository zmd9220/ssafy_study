<template>
  <div id="child">
    <h1>Child</h1>
    <input type="text" @input="onInput" v-model="childData">
    <p>appData: {{ appData }}</p>
  </div>
</template>

<script>
export default {
  name: 'Child',
  data: function () {
    return {
      childData: '',
    }
  },
  // App.vue(상위 컴포넌트)에서 전달 받은 데이터
  props: {
    appData: {
      type: String,
      required: true, // 데이터가 항상 필요 - 데이터가 안 들어오면 에러나 경고 나오게 관리 가능
    }
  },
  methods: {
    // 이벤트 함수 - 위에서 input이 일어났을 때 child-input 이라는 이벤트를 발생 시킴
    onInput: function () {
      this.$emit('child-input', this.childData)
    }
  }
}
</script>

<style>
#child {
  margin: 1rem;
  border: 1px solid blue;
}
</style>