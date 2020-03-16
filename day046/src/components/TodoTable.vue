<template>
  <el-table
    :data="tableData"

    style="width: 100%">
    <!-- <el-table-column height="100" label="ID" prop="id"></el-table-column> -->
    <!-- <el-table-column height="100" label="用户" prop="user"></el-table-column> -->
    <el-table-column height="100" label="事项" prop="things"></el-table-column>
    <!-- <el-table-column height="100" label="描述" prop="doc"></el-table-column> -->
    <!-- <el-table-column height="100" label="状态" prop="status"></el-table-column> -->
    <el-table-column height="100" label="时间" prop="createTime"></el-table-column>
    <el-table-column
      align="right">
      <template slot-scope="scope">
        <el-button
          size="mini"
          @click="handleDone(scope.$index, scope.row)">完成</el-button>
        <el-button
          size="mini"
          type="danger"
          @click="handleDelete(scope.$index, scope.row)">删除</el-button>
      </template>
    </el-table-column>
  </el-table>
</template>

<script>
import axios from 'axios'
// import qs from 'qs'

  export default {
    data() {
      return {
        tableData: null,
 
      }
    },
    props:['user'],
    methods: {
      handleDone(index, row) {
     
        axios.post('http://web4web.top:8899/deleteItem',JSON.stringify(row), {
        headers: {
          'Content-Type': 'application/json;charset=UTF-8'
        },
      })
      .then(response => {
        this.tableData = JSON.parse(response.data.data)
        //  console.log(this.tableData)
      })
      .catch(function (error) {
        console.log(error)
      })

 
        
      },
      handleDelete(index, row) {
        axios.post('http://web4web.top:8899/deleteItem',JSON.stringify(row), {
        headers: {
          'Content-Type': 'application/json;charset=UTF-8'
        },
      })
      .then(response => {
        this.tableData = JSON.parse(response.data.data)
        
        //  console.log(this.tableData)
      })
      .catch(function (error) {
        console.log(error)
      })

      },
      getLsyTodos(){
      let data = new FormData();
      data.append('user','lsy');
    
      axios.post('http://web4web.top:8899/userQuery', data)
      .then(response => {
        this.tableData = JSON.parse(response.data.data)
        //  console.log(this.tableData)
      })
      .catch(function (error) {
        console.log(error)
      })
    },
    getFjyTodos(){
      let data = new FormData();
      data.append('user','fjy');
      // http://web4web.top:8899/allTodos  全部
      axios.post('http://web4web.top:8899/userQuery', data)
      .then(response => {
        this.tableData = JSON.parse(response.data.data)
        // console.log(this.tableData)
      })
      .catch(function (error) {
        console.log(error)
      })
    },
    getAllTodos(){
      if(this.user == 1){
          this.getLsyTodos()   // 请求 lsy Todo 数据
          console.log("lsy")
      }else if(this.user == 0){
          this.getFjyTodos()   // 请求 fjy Todo 数据
          console.log("fjy")
      }
    },
    tableRowClassName(status) {
        if (status === 1) {
          return 'warning-row';
        } else if (status === 2) {
          return 'success-row';
        }
        return '';
      }
    },
    mounted:function(){
        this.getAllTodos()
    },
  }
</script>