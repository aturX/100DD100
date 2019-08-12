package stack


/**
数据结构：  栈
栈：  先进后出 ， 后进先出的特点 （类似洗碟子）

**/

type Item interface {}


type ItemStack struct {
	items []Item
}

// 定义栈  接口
type ItemStacker interface {
	New() *ItemStack   // 创建栈
	Push(item Item)    // 入栈
	Pop() Item         // 出栈
}

// 创建 栈
func (s *ItemStack) New() *ItemStack {
	s.items = []Item{}

	return s
}

// 入栈
func (s *ItemStack) Push(t Item) {
	s.items = append(s.items, t)        // 入栈  进入到最后
}

// 出栈
func (s *ItemStack) Pop() *Item {
	item := s.items[len(s.items) - 1]   // 出栈 出最后一个
	s.items = s.items[0:len(s.items)-1]
	return &item
}



