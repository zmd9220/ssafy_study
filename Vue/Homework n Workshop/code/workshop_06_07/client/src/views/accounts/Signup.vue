<template>
  <div>
    <h1>Signup</h1>
    <div>
      <label for="username">사용자 이름: </label>
      <input type="text" id="username" v-model="credentials.username">
    </div>
    <div>
      <label for="password">비밀번호: </label>
      <input type="password" id="password" v-model="credentials.password">
    </div>
    <div>
      <label for="passwordConfirmation">비밀번호 확인: </label>
      <input type="password" id="passwordConfirmation" v-model="credentials.passwordConfirmation">
    </div>
    <button @click="signup">회원가입</button>
  </div>
</template>

<script>
import axios from 'axios' 
// 환경 변수 VUE_APP_SERVER_URL 설정이 필요함
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'Signup',
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
        passwordConfirmation: '',
      }
    }
  },
  methods: {
    signup: function () {
      axios({
        method: 'POST',
        url: SERVER_URL + '/accounts/signup/',
        data: this.credentials,
      }).then(res => {
        console.log(res)
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
