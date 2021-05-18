<template>
  <div>
    <h1>Login</h1>
    <div>
      <label for="username">사용자 이름: </label>
      <input type="text" id="username" v-model="credentials.username">
    </div>
    <div>
      <label for="password">비밀번호: </label>
      <input type="password" id="password" v-model="credentials.password" @keyup.enter="login">
    </div>
    <button @click="login">로그인</button>
  </div>
</template>


<script>
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'Login',
  props: {
    isLogin: {
      type: Boolean,
      required: true,
    }
  },
  data: function () {
    return {
      credentials: {
        username: '',
        password: '',
      }
    }
  },
  methods: {
    login: function () {
      axios({
        method: 'POST',
        url: SERVER_URL + '/accounts/api-token-auth/',
        data: this.credentials,
      }).then(response =>{
        // console.log(response)
        // 로컬에 토큰 저장
        localStorage.setItem('jwt', response.data.token)
        // App.vue에서 login이라는 이벤트를 전달
        this.$emit('login')
        // todo 리스트 페이지로 이동
        this.$router.push({ name : 'TodoList' })
      }).catch(err => {
        console.log(err)
      })
    }
  },
  created: function () {
    if (this.isLogin) {
      this.$router.push({ name: 'TodoList' })
    }
  },
}
</script>
