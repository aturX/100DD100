package main
/**
 在Windows中使用命令行的Snack程序

 用windows 自带 CMD 或 PowerShell 启动运行

**/

/*
#include <windows.h>
#include <conio.h>

// 使用了WinAPI来移动控制台的光标
void gotoxy(int x,int y)
{
    COORD c;
    c.X=x,c.Y=y;
    SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE),c);
}

// 从键盘获取一次按键，但不显示到控制台
int direct()
{
    return _getch();
}
*/
import "C"
import (
	"fmt"
	"math/rand"
	"os"
	"time"
)
// go中可以嵌入C语言的函数   固定的格式 放在嵌入的C代码之下一行

//定义光标坐标点
type point struct {
	x int
	y int
}

//一些参数的定义  关于蛇的实体
var (
	areaInfo = [20][20]byte{}       // 记录了蛇、食物的信息
	snackLead byte              // 当前蛇头移动方向
	snackSize int               // 当前蛇身长度
	snackHead point             // 当前蛇头位置
	snackTail point             // 当前蛇尾位置
	snackFood bool              // 当前是否有食物
)

// 产生一个随机点
func randomPlace() point {
	n := rand.Int()  % 400
	return point{n /20, n % 20}
}

//  更新控制台的显示，在指定位置写字符，使用错误输出避免缓冲
func drawPoint(p point, char byte) {
	C.gotoxy(C.int(p.x*2+4), C.int(p.y+2))
	fmt.Fprintf(os.Stderr, "%c", char)
}

// 知识点 ： init 函数  https://studygolang.com/articles/13865?fr=sidebar
/**
init 函数在包级别被定义，主要用于：

1. 初始化那些不能被初始化表达式完成初始化的变量
2. 检查或者修复程序的状态
3. 注册
4. 仅执行一次的计算
5. 更多其它场合
*/
func init(){

	// 本程序用到的功能： 仅执行一次的计算 （即，在开始渲染有效界面）
	// 初始化蛇的位置和方向、首尾；初始化随机数
	snackHead, snackTail = point{4, 4}, point{4, 4}
	areaInfo[4][4] = 'H'
	snackLead, snackSize = 'U', 1
	rand.Seed(int64(time.Now().Unix()))
	// 程序初始画面
	// 知识点： stdout是行缓冲的，他的输出会放在一个buffer里面，只有到换行的时候，才会输出到屏幕。而stderr是无缓冲的，会直接输出
    // 使⽤ "`" 定义不做转义处理的原始字符串，⽀持跨⾏。
	fmt.Fprintln(os.Stderr,
		`
  #-----------------------------------------#
  |                                         |
  |                                         |
  |                                         |
  |                                         |
  |                                         |
  |                                         |
  |                                         |
  |                                         |
  |                                         |
  |                      *                  |
  |                                         |
  |                                         |
  |                                         |
  |                                         |
  |                                         |
  |                                         |
  |                                         |
  |                                         |
  |                                         |
  |                                         |
  #-----------------------------------------#
`)

	/**
	知识点： Go 在语⾔层⾯对并发编程提供⽀持，⼀种类似协程，称作 goroutine 的机制。
	只需在函数调⽤语句前添加 go 关键字，就可创建并发执⾏单元。开发⼈员⽆需了解任何
	执⾏细节，调度器会⾃动将其安排到合适的系统线程上执⾏。goroutine 是⼀种⾮常轻量
	级的实现，可在单个进程⾥执⾏成千上万的并发任务。
	*/

	// 键盘事件 捕捉 函数 Go 语言特性实现
	go func(){
		for {
			switch byte(C.direct()){
			case 72:
				snackLead = 'U'   // 上
			case 75:
				snackLead = 'L'   // 左
			case 77:
				snackLead = 'R'   // 右
			case 80:
				snackLead = 'D'   // 下
			case 32:
				snackLead = 'P'   // 暂停

			}
		}
	}()


}


func main() {
	// 主程序：游戏的本质，一个死循环的界面，不断的刷新，更新状态来实现交互
	for {
		//  程序页面定时刷新，更新周期，400毫秒
		time.Sleep(time.Millisecond * 500)

		// 暂停
		if snackLead == 'P' {
			continue
		}
		// 放置食物 （随机）
		if !snackFood {
			give := randomPlace()
			if areaInfo[give.x][give.y] == 0 { // 食物只能放在空闲位置
				areaInfo[give.x][give.y] = 'F'
				drawPoint(give, '$')  // 绘制食物点
				snackFood = true
			}
		}

		// 记录蛇头位置
		// 我们在蛇头位置记录它移动的方向
		areaInfo[snackHead.x][snackHead.y] = snackLead

		// 根据snackLead来移动蛇头  0,0 点坐标 在左上角 所以向上走是 y--
		switch snackLead {
		case 'U':
			snackHead.y--
		case 'L':
			snackHead.x--
		case 'R':
			snackHead.x++
		case 'D':
			snackHead.y++
		}

		// 判断蛇头是否出界  20 * 20  400 像素坐标大小
		if snackHead.x < 0 || snackHead.x >= 20 || snackHead.y < 0 || snackHead.y >= 20 {
			// 撞墙死亡
			C.gotoxy(0, 23) // 让光标移动到画面下方
			break           // 跳出死循环
		}

		// 获取蛇头位置的原值，来判断是否撞死，或者吃到食物
		eat := areaInfo[snackHead.x][snackHead.y]

		if eat == 'F' { // 吃到食物
			snackFood = false
			// 增加蛇的尺寸，并且不移动蛇尾
			snackSize++
		} else if eat == 0 { // 普通移动

			drawPoint(snackTail, ' ') // 擦除蛇尾
			// 注意我们记录了它移动的方向
			dir := areaInfo[snackTail.x][snackTail.y]

			// 我们需要擦除蛇尾的记录
			areaInfo[snackTail.x][snackTail.y] = 0

			// 移动蛇尾
			switch dir {
			case 'U':
				snackTail.y--
			case 'L':
				snackTail.x--
			case 'R':
				snackTail.x++
			case 'D':
				snackTail.y++
			}
		} else { // 撞车了
			C.gotoxy(0, 23)
			break
		}


		drawPoint(snackHead, '#') // 绘制蛇头
	}

	// 收尾了
	switch {
	case snackSize < 22:
		fmt.Fprintf(os.Stderr, "Faild! You've eaten %d $\\n", snackSize-1)
	case snackSize < 42:
		fmt.Fprintf(os.Stderr, "Try your best! You've eaten %d $\\n", snackSize-1)
	default:
		fmt.Fprintf(os.Stderr, "Congratulations! You've eaten %d $\\n", snackSize-1)
	}
	
}
