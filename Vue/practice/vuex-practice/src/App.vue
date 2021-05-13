<template>
  <div id="app">
    <!-- <input type="text" @keyup.enter="onEnter" v-model="content"> -->
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
    }
  },
}
</script>

<style>

</style>
