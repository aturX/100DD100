<template>
    <div>
        <el-header><h1>{{ title }}</h1></el-header>
       
    </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

h1{
    letter-spacing:8px;
    font-family: "FangSong", "Times New Roman", 
             "Microsoft YaHei", "FangSong", "华文细黑", serif;
    font-weight:bold;
}

.el-header, .el-footer {
    background-color: #409EFF;
    color: #333;
    text-align: center;
    line-height: 60px;
    border-radius: 4px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04)
  }
  
  .el-aside {
    background-color: #D3DCE6;
    color: #333;
    text-align: center;
    line-height: 200px;
  }
  
  .el-main {
    background-color: #F2F6FC;
    color: #333;
    text-align: center;
    line-height: 160px;
  }
  
  body > .el-container {
    margin-bottom: 40px;
  }
  
  .el-container:nth-child(5) .el-aside,
  .el-container:nth-child(6) .el-aside {
    line-height: 260px;
  }
  
  .el-container:nth-child(7) .el-aside {
    line-height: 320px;
  }
</style>

<script>
export default {
  name: 'Title',
  props: {
    title: String
  }
}
</script>