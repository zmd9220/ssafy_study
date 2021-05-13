<template>
<div>  
  <select v-model="status">
    <option value="all">전체</option>
    <option value="inProgress">진행 중</option>
    <option value="completed">완료</option>
  </select>
  <ul>
    <!-- key는 고유값이어야 함 index로 할 경우 추후에 오류가 발생할 여지 다분 -->
    <!-- 완료 목록 미완 목록 분리했다가 키 중복돼서 에러났습니다.. -->
    <TodoListItem 
      v-for="todo in todoListByStatus"
      :key="todo.id"
      :todo="todo"
    />
  </ul>
</div>
</template>

<script>
import { mapState, mapGetters } from 'vuex' 
import TodoListItem from '@/components/TodoListItem'

export default {
  name: 'TodoList',
  components: {
    TodoListItem,
  },
  computed: {
    // todoList: function () {
      //   return this.$store.state.todoList
    // }
    ...mapState(['todoList']),
    ...mapGetters(['todoListByStatus']),
    status: {
      get: function () {
        return this.$store.state.status
      },
      set: function (value) {
        this.$store.commit('UPDATE_STATUS', value)
      },
      
    },
  }
}
</script>

<style>

</style>