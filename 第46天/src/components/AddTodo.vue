<template>
    <div>
        <el-header> 
          <!-- <el-button round type="primary" icon="el-icon-user"></el-button>   -->
          <el-input v-model="NewTodo" class="add-input" placeholder="请输入待办事项"></el-input>
          <el-button @click="addTodo(NewTodo)"  plain type="primary" icon="el-icon-circle-plus">{{username}}</el-button>  
        </el-header>
       
    </div> 
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
 .add-input {
    width: 50%;
}
.el-button{
    width: 30%; 
    margin: 5px;
}
</style>

<script>
import axios from 'axios'
export default {
  name: 'AddTodo',
  props: {
    username: String
  },
    data() {
    return {
        NewTodo: '',
        checkTodo: ''
    }
  },
    methods: {
    addTodo(NewTodo){
        var user = ""
        if("房锦妍" == this.username){
            console.log("添加TODO 房锦妍")
            console.log(NewTodo)
            user = "fjy"

        }

        if("李思毅" == this.username){
            console.log("添加TODO 李思毅")
            console.log(NewTodo)
            user = "lsy"
        }
 
        var item = {
            id:"",
            user:user,
            things:NewTodo,
            status:"1",
            // createTime:"",
            doc:"",
            // closeTime:"",
            itemid:(new Date()).valueOf(),
            other3:""
        }
        
        axios.post('http://web4web.top:8899/addItem',JSON.stringify(item), {
        headers: {
          'Content-Type': 'application/json;charset=UTF-8'
        },
      })
      .then(response => {
        this.checkTodo = JSON.parse(response.data.data)
        //  console.log(this.tableData)
        this.$forceUpdate();
      })
      .catch(function (error) {
        console.log(error)
      })
    }
  }
}
</script>