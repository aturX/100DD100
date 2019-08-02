/**
基础
1.  包
编译工具对源码目录有严格要求，每个工作空间 (workspace) 必须由 bin、pkg、src 三个目录组成。
目录结构：
workspace
 |
 +--- bin         // go install 安装目录。
 | |
 | +--- learn
 +--- pkg         // go build ⽣成静态库 (.a) 存放目录。
 | |
 | +--- darwin_amd64
 | |
 | +--- mylib.a
 | |
 | +--- mylib
 | |
 | +--- sublib.a
 |
 +--- src         // 项目源码目录  （我们写代码的地方）
 |
 +--- learn
 | |
 | +--- main.go
 |
 +--- mylib       // 库
 |  |
 |	+--- mylib.go
 |
 +--- sublib
 |  |
 |	+--- sublib.go

导入包：
import "fmt" -> /usr/local/go/pkg/darwin_amd64/fmt.a
import "os/exec" -> /usr/local/go/pkg/darwin_amd64/os/exec.a
解决命名冲突：
import M "yuhen/test" // 包重命名: M.A
import . "yuhen/test" // 简便模式: A

未使⽤的导⼊包，会被编译器视为错误


2.  风格
编码: 源码⽂件必须是 UTF-8 格式，否则会导致编译器出错。
结束: 语句以 ";" 结束，多数时候可以省略。
命名: 采⽤ camelCasing (驼峰命名)⻛格，不建议使⽤下划线。
源⽂件: 头部以 "package <name>" 声明包名称
可执⾏⽂件: 必须包含 package main，⼊⼝函数 main


3.  函数
Go 不⽀持 嵌套 (nested)、重载 (overload) 和 默认参数 (default parameter),左⼤括号依旧不能另起⼀⾏

func test(x, y int, s string) (int, string) { // 类型相同的相邻参数可合并。
 n := x + y                                   // 多返回值必须⽤括号。
 return n, fmt.Sprintf(s, n)
}

* 函数是第⼀类对象，可作为参数传递  (建议如下做法： 定义函数类型，类比Java的泛型)

func test(fn func() int) int {
 return fn()
}
type FormatFunc func(s string, x, y int) string // 定义函数类型。

func format(fn FormatFunc, s string, x, y int) string {
 return fn(s, x, y)
}

* 匿名函数
s1 := test(func() int { return 100 }) // 直接将匿名函数当参数。
func main(){}  // 主函数

4.  数据类型
* 变量
* 常量
* 枚举
* 常用类型： string、array、struct、slice、map、channel、interface、function、空 nil



**/



// 1. 包
package main
import (
"fmt"
"strconv"
"strings"
)

// 2. 风格
//（一位）  8421-BCD码 转换 十进制数字
func BcdToNumber10(bcd string) string {

	// 4. 数据类型
	a := strings.Split(bcd,"")
	bit,error := strconv.Atoi(a[0])
	number := bit * 8
	bit,error = strconv.Atoi(a[1])
	number += bit * 4
	bit,error = strconv.Atoi(a[2])
	number += bit * 2
	bit,error = strconv.Atoi(a[3])
	number += bit * 1
	if error != nil{
		fmt.Println("转换格式错误！")
	}


	fmt.Println()
	return strconv.Itoa(number)
}



//（一位）  十进制数字  转换 8421-BCD码
func Number10ToBcd(number string) string {

	digit,error := strconv.Atoi(number)

	var numArray [4] string

	numArray[0] = strconv.Itoa(digit / 8)
	digit = digit % 8
	numArray[1] = strconv.Itoa(digit / 4)
	digit = digit % 4
	numArray[2] = strconv.Itoa(digit / 2)
	digit = digit % 2
	numArray[3] = strconv.Itoa(digit / 1)

	var BCD string
	for i,v := range numArray {
		if i >= len(numArray){
			break
		}
		BCD += v
	}

	fmt.Println()
	if error != nil{
		fmt.Println("字符串转换成整数失败")
	}

	return BCD
}


/**
多位
*/
// 3. 函数
func N2B(numberStr string) string{
	// 简单判断符合十进制标准 （实际会有很多情况）
	_,e := strconv.Atoi(numberStr)
	if e != nil {
		fmt.Println("不是规范的十进制数!")
	}

	// 转码
	numbers := strings.Split(numberStr,"")
	var result = ""
	for _,n := range numbers {
		n = Number10ToBcd(n)
		result += n
	}
	return result
}


func B2N(bcdStr string) string{
	// 简单判断符合BCD码标准 （实际会有很多情况）
	if len(bcdStr) % 4 != 0 {
		fmt.Println("不是规范的BCD编码!")
	}

	// while  Go语言没有while和do...while语法
	var result = ""
	for {

		if len(bcdStr) < 4 {
			break
		}
		t := bcdStr[:4]
		result +=  BcdToNumber10(t)
		bcdStr = bcdStr[4:]
	}
	return result
}


func main() {

	var flag = "Y"
	for {
		// 输入
		bcd := ""
		number := ""
		fmt.Println("输入BCD码: ")
		fmt.Scanln(&bcd)
		fmt.Println("输入10进制数字：")
		fmt.Scanln(&number)


		// 输出
		BCD := N2B(number)
		fmt.Println("Number => BCD : " , number, " => ",BCD)

		NUM := B2N(bcd)
		fmt.Println("BCD => Number : " , bcd," => ",NUM)

		fmt.Println("--------------------------------------------")
		fmt.Println("是否继续： （Y/N）")
		fmt.Scanln(&flag)

		if flag == "N" {
			break
		}
	}


}