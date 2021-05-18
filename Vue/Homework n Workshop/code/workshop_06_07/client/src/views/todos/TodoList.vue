<template>
  <div>
    <ul>
      <li v-for="todo in todos" :key="todo.id">
        <span @click="updateTodoStatus(todo)" :class="{ completed: todo.completed }">{{ todo.title }}</span>
        <button @click="deleteTodo(todo)" class="todo-btn">X</button>
      </li>
    </ul>
<!--     필요 없음?
    <button @click="getTodos">Get Todos</button> -->
  </div>
</template>

<script>
import axios from 'axios'
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'TodoList',
  props: {
    isLogin: {
      type: Boolean,
      required: true,
    }
  },
  data: function () {
    return {
      todos: [],
    }
  },
  methods: {
    // asyne 비동기 함수로 만듬 - 현업에서 많이 사용
    getTodos: async function () {
      const response = await axios ({
        method: 'get',
        url: SERVER_URL + '/todos/',
        // headers: {
        //   Authorization: `JWT ${localStorage.getItem('jwt')}`
        // }
      })
      this.todos = response.data
      // 일반 함수
      // axios({
      //   method: 'get',
      //   url: SERVER_URL + '/todos/',
      // })
      //   .then((res) => {
      //     // console.log(res)
      //     this.todos = res.data
      //   })
      //   .catch((err) => {
      //     console.log(err)
      //   })
    },
    deleteTodo: function (todo) {
      axios({
        method: 'delete',
        url: `${SERVER_URL}/todos/${todo.id}/`,
        // headers: {
        //   Authorization: `JWT ${localStorage.getItem('jwt')}`
        // }
      })
        .then(() => {
          // console.log(res)
          // 데이터 삭제 후 전체 새로고침 같이 갱신
          this.getTodos()
        })
        .catch((err) => {
          console.log(err)
        })
    },
    updateTodoStatus: function (todo) {
      const todoItem = {
        ...todo, // 기존 todo의 모든 속성을 그대로 가져오되,
        completed: !todo.completed // completed 속성만 반대로 바꿈
      }

      axios({
        method: 'put',
        url: `${SERVER_URL}/todos/${todo.id}/`,
        // headers: {
        //   Authorization: `JWT ${localStorage.getItem('jwt')}`
        // },
        data: todoItem,
      })
        .then(() => {
          // console.log(res)
          // 동적으로 직접 업데이트 (취소선)
          // todo.completed = !todo.completed
          // 그냥 바뀐 값으로 갱신해서 가져오기 (이게 조금더 적절한 듯)
          this.getTodos()
        })
      },
    },
  created: function () {
    if (this.isLogin) {
      this.getTodos()
    } else {
      this.$router.push({ name: 'Login' })
    }
  }
}
</script>

<style scoped>
  .todo-btn {
    margin-left: 10px;
  }

  .completed {
    text-decoration: line-through;
    color: rgb(112, 112, 112);
  }
</style>
