<template>
  <li @click="onTodoClick">
    <input type="checkbox" :checked="todo.completed">
    <span>{{ todo.content }}</span>
    <button @click="onDeleteButtonClick">삭제</button>
  </li>
</template>

<script>
export default {
  name: 'TodoListItem',
  props: {
    todo: {
      type: Object,
      required: true,
    },
  },
  methods: {
    onDeleteButtonClick: function () {
      this.$store.commit('DELETE_TODO', this.todo.createdAt)
    },
    onTodoClick: function () {
      // this.$store.commit('UPDATE_TODO', this.todo)
      // this.$store.commit('UPDATE_TODO', {...this.todo, completed: !this.todo.completed })
      this.$store.dispatch('toggleTodo', this.todo)
    }
  }
}
</script>

<style>

</style>