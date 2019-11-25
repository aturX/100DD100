<template>
  <div id="app">
    <!-- <img src="./assets/logo.png"> -->
    <Header title="今日待办事项列表" />
    
       


    <TodoList />
  </div>
</template>

<script>
import TodoList from './components/TodoList.vue'
import Header from './components/Header.vue'


export default {
  name: 'app',
  components: {
    TodoList,
    Header
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 5px;
}
</style>
