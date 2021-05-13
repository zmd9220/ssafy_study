<template>
  <ul>
    <!-- key는 고유값이어야 함 index로 할 경우 추후에 오류가 발생할 여지 다분 -->
    <!-- 완료 목록 미완 목록 분리했다가 키 중복돼서 에러났습니다.. -->
    <TodoListItem 
      v-for="todo in todoList"
      :key="todo.createdAt"
      :todo="todo"
    />
  </ul>
</template>

<script>
import { mapState } from 'vuex' 
import TodoListItem from '@/components/TodoListItem'

export default {
  name: 'TodoList',
  components: {
    TodoListItem,
  },
  computed: {
    ...mapState(['todoList']),
    // todoList: function () {
    //   return this.$store.state.todoList
    // }
  }
}
</script>

<style>

</style>