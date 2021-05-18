<template>
  <div>
    <input type="text" v-model.trim="title" @keyup.enter="createTodo">
    <button @click="createTodo">+</button>
  </div>
</template>

<script>
import axios from'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'CreateTodo',
  data: function () {
    return {
      title: '',
    }
  },
  methods: {
    createTodo: function () {
      const todoItem = {
        title: this.title,
      }

      if (todoItem.title) {
        axios({
          method: 'post',
          // 둘 다 상관 없음 같은 결과
          url: SERVER_URL + '/todos/',
          // url: `${SERVER_URL}/todos/`,
          data: todoItem
        }).then((res) => {
          console.log(res)
          this.$router.push({ name: 'TodoList' })
        }).catch((err) => {
          console.log(err)
        })
      }
    },
  }
}
</script>
