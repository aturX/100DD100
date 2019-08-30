//模板
var todoTemplate = function(title){
    var t = `
        <div class="todo-cell">
            <button class="todo-delete">删除</button>
            <span>${title}</span>
        </div>
    `
    return t
}
//插入
var insertTodo = function(todo){
    var title = todo.title
    var todoCell = todoTemplate(title)
    // 插入TODO list
    todoList.insertAdjacentHTML('beforeend', todoCell)
}

//Ajax 加载
var loadTodos = function(){
    // 调用ajax
    apiTodoAll(
    function(r){
        var todos = JSON.parse(r)
        // 循环添加
        for(var i = 0; i < todos.length; i++){
            var todo = todos[i]
            insertTodo(todo)
        }
    })
}

var bindEventTodoAdd = function() {
    var b = e('#id-button-add')
    // 注意, 第二个参数可以直接给出定义函数
    b.addEventListener('click', function(){
        var input = e('#id-input-todo')
        var title = input.value
        log('click add', title)
        var form = {
            title: title,
        }
        apiTodoAdd(form, function(r) {
            // 收到返回的数据, 插入到页面中
            var todo = JSON.parse(r)
            insertTodo(todo)
        })
    })
}

var bindEvents = function() {
    bindEventTodoAdd()
}

var __main = function() {
    bindEvents()
    loadTodos()
}

//常用套路
__main()