 
var log = function(logdata){
    console.log("Log", logdata)
    alert(logdata)
}

function sumAB(a, b){
	r = parseInt(a) + parseInt(b)
	return r
}


function decAB(a, b){
    r = parseInt(a) - parseInt(b)
    return r
} 



function mulAB(a, b){
	r = parseInt(a) * parseInt(b)
	return r
}


function divAB(a, b){
	if(parseInt(b) !== 0){
        r =parseInt(a) / parseInt(b)
    }else{
        r = False
    }
	return r
}
	

function run(a, ch, b){
    a = parseInt(a)
    b = parseInt(b)

	if(ch === "+"){
        r = sumAB(a, b)
    }else if(ch === "-"){
        r = decAB(a, b)
    }else if(ch === "*"){
        r = mulAB(a, b)
    }else if(ch === "/"){
        r = divAB(a, b)
    }else{
        r = False
    }	
	return r 
}
	

function main(){
	a = prompt("输入a： ")
	ch = prompt("输入运算符：")
	b = prompt("输入b:  ")
	r = run(a, ch, b)
	log(r)
}

main()