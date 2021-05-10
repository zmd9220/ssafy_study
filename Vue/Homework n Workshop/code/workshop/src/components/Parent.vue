<template>
  <div id="parent">
    <h1>Parent</h1>
    <input type="text" @input="onInput" v-model="parentData">
    <p>appData: {{ appData }}</p>
    <p>childData: {{ childData }}</p>
    <!-- 자식에서 child-input이라는 이벤트가 발생하면 onChildInput 리스너로 처리하겠다. -->
    <Child :appData="appData" @child-input="onChildInput" />
  </div>
</template>

<script>
import Child from '@/components/Child.vue'
export default {
  name: 'Parent',
  data: function () {
    return {
      childData: '',
      parentData: '',
    }
  },
  // App.vue(상위 컴포넌트)에서 전달 받은 데이터
  props: {
    appData: {
      type: String,
      required: true, // 데이터가 항상 필요 - 데이터가 안 들어오면 에러나 경고 나오게 관리 가능
    }
  },
  components: {
    Child,
  },
  methods: {
    onChildInput: function (childData) {
      // console.log(childData)
      this.childData = childData
      this.$emit('child-input', this.childData)
    },
    // 이벤트 함수 - 위에서 input이 일어났을 때 child-input 이라는 이벤트를 발생 시킴
    onInput: function () {
      this.$emit('parent-input', this.parentData)
    },
  }
}
</script>

<style>
#parent {
  margin: 1rem;
  border: 1px solid red;
}
</style>