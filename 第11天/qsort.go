package main

import "fmt"

/***
Go 语言特点
1. 并发执行
Java： 类似Java的编程语言中，执行并发的思路是使用多个线程，竞争执行一块共享资源，从而实现并发，这样在编程角度更加复杂，在程序角度并不高效。
Go： 在Go语言中并发是其自身具体的特点，采用一种goroutine的并行执行方式，每个线程中可以有成百上千个goroutine并行执行，采用一种叫做通道的数据结构，
可以让 goroutine 之间进行安全的数据通信，避免了资源竞争多个操作修改同一个数据造成的安全问题。


2. 开发速度与执行效率的平衡
Python：  动态语言，开发快速，但程序中的数据类型问题，导致很多问题在程序运行时才会暴露出来。
C++：强类型的静态语言，但编译缓慢，对于程序员不友好，开发难度大而复杂，具有较高的执行执行效率。
Go： Go语言在开发在开发速度和执行效率之间取得平衡，特点在于他的编译器与C++不同，它更专注于对直接被引用的依赖的编译。
而后者则是会遍历所有依赖库。



3. 继承模式与组合模式的对比
Python/Java/C#： 面向对象的继承模式，子类继承父类，具备父类的属性和方法等。对于接口，Java中的类必须实现它的接口中的所有约束。
Go：Go语言中不采用继承的方式，而使用一种组合的设计模式，只需简单地将一个类型嵌入到另一个类型，就能
复用所有的功能。在 Go 语言中，不需要声明某个类型实现了某个接口，编译器会判断一个类型的实例是否
符合正在使用的接口。即：这个特性叫作鸭子类型——如果它叫起来像鸭子，那它就可能是只鸭子。


**/


// 快速排序
/**
思路：
1. 选取一个基准值 (这里选择，中间值)
2. 左右分两段，大于基准的数据放一边，小于基准的数据放另一边
3. 对左边重复1,2过程，直到不能重复为止
4. 对右边重复1,2过程，直到不能重复为止
*/
func QuickSort(values []int)[]int{
	// 特殊情况检测
	if len(values) <= 1{
		return values
	}
	point := values[0]   // 取第一个元素做基准点
	// 用一个头尾 坐标用于数据的交换操作
	head,tail := 0, len(values) - 1

	for i:=1; i <= tail; {
		if values[i] < point{
			// 小于基准的数，放在左侧
			values[i],values[head] = values[head], values[i]
			head++
		}else{
			// 大于基准的数，放在右侧
			values[i],values[tail] = values[tail], values[i]
			tail--
		}

		if head > tail{
			break
		}
	}
	// 左边重复 递归
	QuickSort(values[:head])  // head 和 tail 已经交汇  用values[:tail] 也同理
	// 右边重复 递归
	QuickSort(values[head+1:])
	return values
}


// 使用
func main(){
	s := QuickSort([]int{5, 7, 3, 2, 1})
	fmt.Println(s)
}