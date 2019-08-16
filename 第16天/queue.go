package main

import "fmt"

/**
 	数据结构：  队列
	先进先出， 后进后出

**/

// 知识点 ： 接口
//接口是⼀个或多个⽅法签名的集合，任何类型的方法集中只要拥有与之对应的全部方法，
//就表示它 "实现" 了该接口，无须在该类型上显式添加接口声明


// 接口命名习惯以 er 结尾，结构体
// 接口只有方法签名，没有实现
// 接口没有数据字段。
// 可在接口中嵌⼊其他接口。
// 类型可实现多个接口。

/**   演示： 接口

// 接口定义
type Adder interface {
	Sum() int
}

// 结构体
type Number struct {
	N1 int
	N2 int
}

// 接口的实现 (两数相加)
func (n *Number) Sum() int {
	sum  := n.N1 + n.N2
	return sum
}

func main() {
	// test 接口 演示
	var s Adder = &Number{3,4}
	fmt.Println(s.Sum())   // 7
}
**/


// 队列单项元素接口
type Item interface {}

// 队列
type ItemQueue struct {
	items []Item
}

// 队列接口
type ItemQueuer interface {
	// 队列参数定义
	New() ItemQueue      // 功能： 创建新队列项
	Enqueue(t Item)      // 功能： 单项元素 入队
	Dequeue() *Item		 // 功能： 头部元素 出队
	IsEmpty() bool		 // 功能： 判断队列是否为空
	Size() int           // 功能： 获取队列长度
}

// 传入队列元素变量 ， 得到一个空队列
func (s *ItemQueue) New() *ItemQueue {
	s.items = []Item{}   // 新建空元素
	return s
}

//  入队操作：  结尾添加元素
func (s *ItemQueue) Enqueue(t Item) {
	s.items = append(s.items, t)
}

//  出队操作：  元素先进先出
func (s *ItemQueue) Dequue() Item {
	item := s.items[0]
	s.items  = s.items[1:len(s.items)]

	return item
}


//  队列判空
func (s *ItemQueue) IsEmpty() bool {
	return len(s.items) == 0
}


//  返回队列长度
func (s *ItemQueue) Size() int {
	size := len(s.items)

	return size
}


/*** test ***/
var que ItemQueue

// 1. 队列初始化
func initQueue() *ItemQueue {
	if que.items == nil {
		que = ItemQueue{}
		que.New()
	}
	return &que
}



func main () {

	// 2. 使用
	que := initQueue()

	// 3. 理解Go 接口的特点： 接口是⼀个或多个⽅法签名的集合，任何类型的方法集中只要拥有与之对应的全部方法， 就表示它 "实现" 了该接口（ItemQueuer），无须在该类型上显式添加接口声明
	que.Enqueue(1)		// 入队操作
	que.Enqueue(3)
	que.Enqueue(5)
	que.Enqueue(7)

	fmt.Println(que.items)   // 队列所有元素

	fmt.Println(que.IsEmpty())  // 队列判空

	fmt.Println(que.Size())     // 队列长度

	fmt.Println(que.Dequue())   // 出队操作

	fmt.Println(que.Size())     // 队列长度

	fmt.Println(que.items)   // 队列所有元素

}

