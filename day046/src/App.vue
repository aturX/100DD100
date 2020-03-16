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
  }, 
  created () {
    document.title = '今日待办'
  }
}
</script>

<style>
*{
  margin:0;
  padding:0;
}


#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  /* background:rgb(243, 247, 199); */
  width:100%;
  height: 100%;
  position: absolute;
}
</style>
