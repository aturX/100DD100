<template>
   <div id="todolist">
      <el-container>

     <el-row :gutter="12">
          <el-col :xs="24" :sm="24" :md="24" :lg="24" :xl="2"></el-col>
          <el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="10">
            <!-- 左边 -->
            <el-container class="grid-content bg-purple-light">
              <el-main>
                  <AddTodo username="房锦妍" />
                  <TodoTable :user= 0 />
              </el-main>
            </el-container>
           </el-col>
          <el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="10">
                  <!-- 右边 -->
              <el-container class="grid-content bg-purple">
                <el-main> 
                    <AddTodo username="李思毅" />
                    <TodoTable :user= 1 />
                </el-main>
              </el-container>
          </el-col>
          <el-col :xs="24" :sm="24" :md="24" :lg="24" :xl="2"></el-col>
           
      </el-row>
      </el-container>
   </div>

</template>

<script>
import TodoTable from './TodoTable.vue'
import AddTodo from './AddTodo.vue'


export default { 
     name: 'todolist',
     components: {TodoTable, AddTodo},

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.add-input {
    width: 50%;
}
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}

.el-main {
    background-color: #E9EEF3;
    color: #333;
    text-align: center;
    line-height: 40px;
    box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1)
  }

.el-container {
    margin: 10px;
    color: Transparent;

  }
.el-button{
    margin: 10px;
}



/* 响应式 */
.el-col {
    border-radius: 4px;
  }
  .bg-purple-dark {
    background: #99a9bf;
  }
  .bg-purple {
    background: #d3dce6;
  }
  .bg-purple-light {
    background: #e5e9f2;
  }
  .grid-content {
    border-radius: 4px;
    min-height: 36px;
  }  


</style>

