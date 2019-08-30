var log = function(){
    console.log.apply(console, arguments)
}
var e = function(sel){
    return document.querySelector(sel)
}

//ajax 函数
var ajax = function(method, path, data, responseCallback){
    var request = new XMLHttpRequest()
    // 设置请求方法 和 请求地址
    request.open(method, path, true)
    // 设置 发送数据格式
    request.setRequestHeader('Content-Type', 'application/json')
    request.onreadystatechange = function(){
        if(request.readyState === 4) {
            reseponseCallback(request.response)
        }
    }
    // 数据转换为JSON  字符串  序列化
    data = JSON.stringify(data)
    // 发送请求
    request.send(data)
}

var apiTodoAll = function(callback) {
    var path = '/api/todo/all'
    ajax('GET', path, '', callback)
}

// 增加一个 todo
var apiTodoAdd = function(form, callback) {
    var path = '/api/todo/add'
    ajax('POST', path, form, callback)
}