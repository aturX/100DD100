/***
任务： 完成一个TODO List 页面 逻辑
1. button 进行事件绑定
2. 事件处理函数，获取input的值
3. 组合一个Todo对象函数的HTML字符串
4. 插入到需要的todo-list 中
***/

// 封装console.log 函数 为log
var log = function(){
    console.log.apply(console, arguments)
}
// 获取元素的函数封装  为e   支持 css  id
var e = function(sel) {
    return document.querySelector(sel)
}
//log('test')
//log(e('button'))

//功能： 构建模板对象
var todoTemplate = function(todo){
    var t = `
        <div class="todo-cell">
            <span>${todo}</span>
            <button class="todo-delete">删除</button>
        </div>
    `
    return t
}

// 功能： 插入元素模板
var insertTodo = function(todo){
     var todoCell = todoTemplate(todo)
     // 插入
     var todoList = e('.todo-list')
     todoList.insertAdjacentHTML('beforeend', todoCell)
}

// 功能： 为“添加”按钮绑定事件

// 1. 获取button
var bt = e('#id-button-add')
// 监听函数
bt.addEventListener('click',function(){
    log('click')
    // 取值
    var input = e('#id-input-todo')
    var todo = input.value
    log('todo', todo)
    // 插入
    insertTodo(todo)
})

//  功能： 删除完成的任务
// 1. 找到元素
var todoList = e('.todo-list')
// 事件响应函数 传入响应的事件
todoList.addEventListener('click', function(event){
    log('event', event)
    var self = event.target
    // 通过比较被点击元素的 class 来判断元素是否是我们想要的
    //log(self.classList)
    if(self.classList.contains('todo-delete')){
        log('点到了删除按钮')
        // 删除 self 的父节点
        // parentElement 可以访问到元素的父节点
        self.parentElement.remove()
    } else {
        log('点击的不是删除按钮')
    }
})














