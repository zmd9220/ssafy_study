<template>
  <div id="app">
    <!-- <input type="text" @keyup.enter="onEnter" v-model="content"> -->
    <!-- <select v-model="status" @change="onChangeStatusClick">
      <option value="all">전체</option>
      <option value="inProgress">진행 중</option>
      <option value="completed">완료</option>
    </select> -->
    <TodoForm />
    <TodoList />
  </div>
</template>

<script>
import TodoForm from '@/components/TodoForm'
import TodoList from '@/components/TodoList'


export default {
  name: 'App',
  components: {
    TodoForm,
    TodoList,
  },
  data: function () {
    return {
      content: '',
    }
  },
  methods: {
    onEnter: function () {
      this.$store.dispatch('addTodo', this.content)
    },
    // onChangeStatusClick: function () {
    //   this.$store.commit('UPDATE_STATUS', this.status)
    // },
  },
  computed: {

  }
}
</script>

<style>

</style>
