import tkinter as tk
import tkinter.messagebox

class Chess(object):
	def __init__(self):
		# 存放所有棋子状态： 0 - 无子, 1 - 黑子, 2 - 白子
		self.allChess = [[0 for i in range(19)] for j in range(19)]
		self.line_distance = 20
		self.game_status = True
		self.user = 0  # 0 - 黑棋 1 - 白棋
		self.last_point = (0, 0)

	def draw_point(self, color, point, tag=False):
		if tag == True:
			r = (self.line_distance/2) // 2 - 2
		else:
			r = self.line_distance // 2 - 2
		if "white" == color:
			color = "#FFF"
		if "black" == color:
			color = "#000"
		game_table.create_oval(point[0] - r, point[1] - r, point[0] + r, point[1] + r, fill=color)


	def game_ing(self):
		# 绘制 黑白棋
		for i in range(19):
			for j in range(19):
				if self.allChess[i][j] == 0:
					continue
				if self.allChess[i][j] == 1:
					self.draw_point("black", (self.line_distance * i, self.line_distance * j))
				if self.allChess[i][j] == 2:
					self.draw_point("white", (self.line_distance * i, self.line_distance * j))

	def draw_paint(self):
		"""
		画板： 每次下子，重新画一次棋盘  19 X 19     6   10   14
		:return:
		"""
		canvas_width = 400
		canvas_height = 400
		for x in range(self.line_distance, canvas_width, self.line_distance):
			game_table.create_line(x, 0, x, canvas_height, fill="#476042")

		for y in range(self.line_distance, canvas_height, self.line_distance):
			game_table.create_line(0, y, canvas_width, y, fill="#476042")

		# 标记点
		self.draw_point("black", (self.line_distance*4, self.line_distance*4), tag=True)
		self.draw_point("black", (self.line_distance*4, self.line_distance*16), tag=True)
		self.draw_point("black", (self.line_distance*16, self.line_distance*4), tag=True)
		self.draw_point("black", (self.line_distance*16, self.line_distance*16), tag=True)
		self.draw_point("black", (self.line_distance*10, self.line_distance*10), tag=True)
		self.game_ing()
		return game_table

	def check_five(self, point_index):
		# 把要下的棋子颜色保存
		x = point_index[0]
		y = point_index[1]
		color = self.allChess[x][y]
		# 计算已连棋子个数
		count = 1
		# 判断横向右边是否五子
		for i in range(1, 6):
			if x >= 15:  # 19列最少留5个位置 15
				break
			if color == self.allChess[x + i][y]:
				count = count + 1
			self.check_win(count, color)
		count = 1
		#判断横向左边是否五子
		for i in range(1, 6):
			if x <= 3:  # 当棋子竖向上边无法连成五子，直接退出
				break
			if color == self.allChess[x - i][y]:
				count = count + 1
			self.check_win(count, color)

		count = 1
		# 判断竖向下边是否五子
		for i in range(1,6):
			if y >= 15:  # 19列最少留5个位置 15
				break
			if color ==  self.allChess[x][y + i]:
				count = count + 1
			self.check_win(count, color)

		count = 1
		# 判断竖向上边是否五子
		for i in range(1, 6):
			if y <= 3:
				break
			if color == self.allChess[x][y - i]:
				count = count + 1
			self.check_win(count, color)

		count = 1
		# 判断右斜上边是否五子
		for i in range(1, 6):
			if y <= 3 or x >= 15:  # 当棋子右斜上边无法连成五子，直接退出
				break
			if color == self.allChess[x + i][y - i]:
				count = count + 1
			self.check_win(count, color)

		count = 1
		# 判断左斜向下边是否五子
		for i in range(1, 6):
			if x <= 3 or y >= 15:  # 当棋子右斜上边无法连成五子，直接退出
				break
			if color == self.allChess[x - i][y + i]:
				count = count + 1
			self.check_win(count, color)

		count = 1
		# 判断左斜向上边是否五子
		for i in range(1, 6):
			if x <= 3 or y <= 3:  # 当棋子右斜上边无法连成五子，直接退出
				break
			if color == self.allChess[x - i][y - i]:
				count = count + 1
			self.check_win(count, color)

		count = 1
		# 判断右斜向下边是否五子
		for i in range(1, 6):
			if y >= 15 or x >= 15:  # 当棋子右斜上边无法连成五子，直接退出
				break
			if color == self.allChess[x + i][y + i]:
				count = count + 1
			self.check_win(count, color)



	def check_win(self, count, color):
		if count >= 5:
			if color == 1:
				print(f"黑方 获胜！")
				tk.messagebox.showinfo(title='游戏结束', message='黑方 获胜！')
				ch.game_status = False
			if color == 2:
				print(f"白方 获胜！")
				tk.messagebox.showinfo(title='游戏结束', message='白方 获胜！')
				ch.game_status = False

	def restart(self):
		print("重新开始游戏")
		global game_table
		game_table = tk.Canvas(windows, bg='white', height=400, width=400)
		game_table.grid(row=0, column=1, padx=10, pady=10)
		game_table.bind("<Button>", print_mouse_click)  # 鼠标单击事件
		for i in range(19):
			for j in range(19):
				ch.allChess[i][j] = 0
		ch.game_status = True
		ch.user = 0
		ch.draw_paint()



	def reback(self):
		print("悔棋")
		ch.allChess[ch.last_point[0]][ch.last_point[1]] = 0

	def exit(self):
		print("退出游戏")


# 打印单击的鼠标
def print_mouse_click(event):
	if ch.game_status == True:
		if ch.user == 0:
			# 黑棋 先走
			point_index = (int(event.x / 20), int(event.y / 20))
			ch.allChess[point_index[0]][point_index[1]] = 1
			ch.draw_paint()

			ch.user = 1
			ch.check_five(point_index)

		else:
			# 白棋 再走
			point_index = (int(event.x / 20), int(event.y / 20))
			ch.allChess[point_index[0]][point_index[1]] = 2
			ch.draw_paint()

			ch.user = 0
		ch.last_point = point_index





if __name__ == "__main__":
	windows = tk.Tk()
	windows.title('python')

	windows.geometry('600x500')
	game_table = tk.Canvas(windows, bg='white', height=400, width=400)
	game_table.grid(row=0, column=1, padx=10, pady=10)
	game_table.bind("<Button>", print_mouse_click)  # 鼠标单击事件
	# 初始化
	ch = Chess()
	ch.draw_paint()
	game_table.update()


	# 命令
	bt_restart = tk.Button(windows, text='重新开始', width=8, height=2, command=ch.restart)  # 点击按钮式执行的命令
	bt_reback = tk.Button(windows, text='悔棋', width=8, height=2, command=ch.reback)  # 点击按钮式执行的命令
	bt_exit = tk.Button(windows, text='退出', width=8, height=2, command=ch.exit)  # 点击按钮式执行的命令
	bt_restart.grid(row=1, column=0, padx=10, pady=10)
	bt_reback.grid(row=1, column=1, padx=0, pady=10)
	bt_exit.grid(row=1, column=2, padx=0, pady=10)

	windows.mainloop()
