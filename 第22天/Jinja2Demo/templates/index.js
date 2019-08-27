$(function(){
    $.ajax({
        // 请求方式
        type: 'GET',
        // 文件位置
        url: 'data.json',
        // 返回数据的格式
        dataType: 'json',
        // success 
        success: function(data){
            console.log(data)
        },
        error: function(){
        console.log("error")
        }
        // error
    })
})