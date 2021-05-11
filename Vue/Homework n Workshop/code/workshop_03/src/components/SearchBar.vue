<template>
  <div>
    <input type="text" v-model="query" @keyup.enter="onEnter">
  </div>
</template>

<script>
export default {
  name: 'SearchBar',
  data: function () {
    return {
      query: '',
    }
  },
  methods: {
    onEnter: function () {
      return this.$emit('search', this.query)
    },
  },
}
</script>

<style>

</style>