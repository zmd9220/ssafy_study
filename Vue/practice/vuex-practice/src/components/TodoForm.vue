<template>
  <div>
    <input type="text" v-model="content" @keyup.enter="onEnter">
  </div>
</template>

<script>
import { mapActions } from 'vuex'
export default {
  name: 'TodoForm',
  data: function () {
    return {
      content: '',
    }
  },
  methods: {
    ...mapActions(['addTodo']),
    onEnter: function () {
      this.addTodo(this.content.trim())
      // this.$store.dispatch('addTodo', this.content)
      this.content = ''
    }
  }
}
</script>

<style>

</style>