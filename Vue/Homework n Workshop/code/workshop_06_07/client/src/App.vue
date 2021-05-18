<template>
  <div id="app">
    <div id="nav">
      <span v-if="isLogin">
        <router-link :to="{ name: 'TodoList' }">Todo List</router-link> | 
        <router-link :to="{ name: 'CreateTodo' }">Create Todo</router-link> |
        <router-link to="#" @click.native="onLogout">Logout</router-link>
      </span>
      <span v-else>
        <router-link :to="{ name: 'Signup' }">Signup</router-link> |
        <router-link :to="{ name: 'Login' }">Login</router-link> 
      </span>
    </div>
    <router-view @login="onLogin" :isLogin="isLogin" />
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'App',
  data: function () {
    return {
      isLogin: false,
    }
  },
  methods: {
    onLogin: function () {
      this.isLogin = true
      axios.defaults.headers.common['Authorization'] = `JWT ${localStorage.getItem('jwt')}`
    },
    onLogout: function () {
      localStorage.removeItem('jwt')
      this.isLogin = false
      this.$router.push({ name: 'Login' })
      axios.defaults.headers.common['Authorization'] = ''
    }
  },
  created: function () {
    const jwt = localStorage.getItem('jwt')
    if (jwt) {
      this.isLogin = true
      axios.defaults.headers.common['Authorization'] = `JWT ${jwt}`
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
