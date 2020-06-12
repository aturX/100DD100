# Python 3.5 之后简化并更好地标识异步IO 使用 async/await
from datetime import datetime
from time import sleep
import threading
import asyncio

def hello():
	print("1111")
	sleep(3)
	print("2222")

def world():
	print("3333")
	sleep(2)
	print("4444")

def demo_no_async():
	start = datetime.now()
	# 传统方式 顺序执行  耗时约 5 秒
	hello()
	world()
	print(datetime.now() - start)

# demo_no_async()


# Python 3.5 之前写法 ： 协程实现单线程并发， 最快继续边界是最大耗时操作时长  即 5秒
@asyncio.coroutine
def hello0():
	print('Hello world! (%s)' % threading.currentThread())
	yield from asyncio.sleep(5)
	print('Hello again! (%s)' % threading.currentThread())

@asyncio.coroutine
def hello1():
	print('Hello world! (%s)' % threading.currentThread())
	yield from asyncio.sleep(2)
	print('Hello again! (%s)' % threading.currentThread())

@asyncio.coroutine
def hello2():
	print('Hello world! (%s)' % threading.currentThread())
	yield from asyncio.sleep(3)
	print('Hello again! (%s)' % threading.currentThread())


def run():
	start = datetime.now()
	loop = asyncio.get_event_loop()
	tasks = [hello0(), hello1(),hello1(),hello1(), hello2(), hello2(), hello2(), hello0()]
	loop.run_until_complete(asyncio.wait(tasks))
	loop.close()
	print(datetime.now() - start)

# run()

# python3.5 之后  异步IO 实现 单线程高并发效果
async def async_hello():
	print('async_hello! (%s)' % threading.currentThread())
	await asyncio.sleep(4)
	print('async_hello again! (%s)' % threading.currentThread())

async def async_world():
	print('async_world! (%s)' % threading.currentThread())
	await asyncio.sleep(7)
	print('async_world again! (%s)' % threading.currentThread())

def demo_async():
	start = datetime.now()
	loop = asyncio.get_event_loop()
	# 异步IO方式 执行 任务
	tasks = [async_hello(), async_world()]
	loop.run_until_complete(asyncio.wait(tasks))
	loop.close()
	print(datetime.now() - start)

# demo_async()

