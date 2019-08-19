
# Web
- 模式架构： MVC ( Model View Control )


# MVC 模式
## 页面-View：  HTML/CSS/JS + 图片 （静态资源）
- 用户打开一个网页，看到了内容的展示。

## 逻辑-Control：  Python
- 用户输入了登录的账号密码，传递到后台，Python代码获取用户的登录信息，实现增删改查逻辑（CURD）

## 数据-Model：  Mysql
- 程序的数据来自数据层，可能是数据库，可能是其他程序，可能是一个问题等等。数据被Python获取后进行操作。

# 实现一个MVC Web 框架

## (UI/前端)
- static： 目录保存图片
- templates：目录存为网页HTML、CSS、JavaScript

## （后端）
- routes.py：服务器路径和路由函数，即“我要XXX” -> “XXX在YYY那里”
- server.py：我们的服务器代码（核心），即“这里有XXX，AAA，BBB等待用户选择使用哪一个”
- utils.py： 我们工具箱，写代码会封装一些功能函数，“打印日志函数”、“通过身份证号获取年龄”，“计算登录时长”，“文件上传功能”

## （数据库/运维）
- models.py： 数据存储的代码， 用来将数据处理，存储的函数。

# 具体实践 

- 业务流程
 1. 用户打开登录页 -> 用户输入用户名密码登录 -> 页面跳转至主页 -> 展示一张图片
 2. 用户在主页留言板留言 -> 留言后展示留言用户名、留言时间、留言内容

- 静态资源
 1. static： doge.gif 猫狗图片 
 2. template： login.html (登录页), index.html (主页面)
 
- 后端实现
 1. routes.py: 项目的导航员    login,index 
    - 映射函数
    - 功能函数（读图片、读页面、读文件等）

 2. server.py: 核心服务，(1)接收用户的请求 (2)返回给用户响应
 if __name__ == '__main__': 的讲解
 装包 与 解包 的讲解
 socket 的网络过程讲解
 网络请求Request 的讲解
 面向对象的讲解
 byte 类型 str 字符串类型的讲解  （编码格式UTF-8）
    -   response_for_path(path)：  函数功能静态资源 获取 
           get 方法的讲解 
    -   error(request, code=404) : 页面未找到
  面向对象： 多种参数的配置 Request 的讲解
  页面 GET  POST 请求的讲解
  path 解析的讲解
  unquote 的讲解
  
  3. models.py: 数据层 服务数据的持久化
  

  
     
