package stack

import (
	"fmt"
	"testing"
)

var s ItemStack

func initStack() *ItemStack {
	if s.items == nil{
		s = ItemStack{}
		s.New()
	}


	return &s
}


func TestItemStack_Push(t *testing.T) {
	s := initStack()

	s.Push(1)   // 入栈 1
	s.Push("aaaa") // 入栈 “aaaa”

	if size := len(s.items); size != 2{   // 语法糖 ： 在if 后面 ，条件前面， 可添加语句
		t.Errorf("test failed ")
	}

	fmt.Println(s)


}

func TestItemStack_Pop(t *testing.T) {
	s.Pop()

	if size := len(s.items); size !=2 {
		t.Errorf("test failed, excepted 2 and got %d", size)
	}

	s.Pop()
	s.Pop()

	if size := len(s.items); size != 0{
		t.Errorf("test failed, excepted 0 and got %d", size)
	}
}