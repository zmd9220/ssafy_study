import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    // todoList를 vuex에서 관리 (전체 공유 데이터)
    todoList: [],
  },
  mutations: {
    // todoList에 데이터를 넣는 방법
    ADD_TODO: function (state, todoItem) {
      state.todoList.push(todoItem)
    },
    // 별로 좋지 않은 삭제 코드
    // DELETE_TODO: function (state, todoItem) {
    //   state.todoList = state.todoList.filter(todo => {
    //     return todo !== todoItem
    //   })
    // },
    DELETE_TODO: function (state, createdAt) {
      state.todoList = state.todoList.filter(todo => {
        return todo.createdAt !== createdAt
      })
    },
    UPDATE_TODO: function (state, todoItem) {
      // todoItem.completed = !todoItem.completed
      state.todoList = state.todoList.map(todo => {
        if (todo.createdAt === todoItem.createdAt) {
          return todoItem
        }
        return todo
      } )
    },

  },
  actions: {
    // 컴포넌트에서 dispatch로 호출할 함수
    // 액션 함수는 항상 첫 번째 인자로 context가 들어감 addTodo 기능을 위한 모든 행동을 추가함
    addTodo: function (context, content) {
      if (!content) return
      const todo = {
        content: content,
        createdAt: Date.now(),
        completed: false,
      }
      
      // mutation 함수 호출 (commit)
      context.commit('ADD_TODO', todo)
    },
    toggleTodo: function (context, todoItem) {
      context.commit('UPDATED_TODO', {...todoItem, complete: !this.todo.completed})
    }
  }
})
