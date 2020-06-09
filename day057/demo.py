# Python 多线程 与 多进程
import time, threading


# 新线程执行的代码:
def say_some():
	print('--------线程 [{}] 开始运行...'.format(threading.current_thread().name))
	n = 0
	while n < 7:
		n = n + 1
		print('thread [{}] >>> [{}]'.format(threading.current_thread().name, n))
		time.sleep(n)
	print('线程 [{}] 结束运行...'.format(threading.current_thread().name))


def demo1():
	print('--------线程 [{}] 开始运行...'.format(threading.current_thread().name))
	t = threading.Thread(target=say_some, name='SaySomeThread')
	t.start()
	t.join()  # 线程结束后继续执行
	print('线程 [{}] 结束运行...'.format(threading.current_thread().name))


# 线程的锁
'''
多线程和多进程最大的不同在于，多进程中，同一个变量，
各自有一份拷贝存在于每个进程中，互不影响，而多线程中，
所有变量都由所有线程共享，所以，任何一个变量都可以被任何一个线程修改，
因此，线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了。
所以，和多进程相比，多线程需要对特定的变量加锁，保证其修该操作不会乱。
'''

# 锁
lock = threading.Lock()


def run_thread(n):
	for i in range(100000):
		# 先要获取锁:
		lock.acquire()
		try:
			# 修改变量
			n = n + 1
		finally:
			# 改完了一定要释放锁:
			lock.release()


# 包含锁的某段代码实际上只能以单线程模式执行，效率就大大地下降了。


# Python “伪”多线程原因：GIL锁
'''
使用C、C++或Java来写特定死循环，直接可以把全部核心跑满，4核就跑到400%，
但是Python跑相同代码，只能将CPU跑到100%左右。

Python的线程虽然是真正的线程，但解释器执行代码时，有一个GIL锁：Global Interpreter Lock，
任何Python线程执行前，必须先获得GIL锁，然后，每执行100条字节码，
解释器就自动释放GIL锁，让别的线程有机会执行。

GIL全局锁实际上把所有线程的执行代码都给上了锁，
所以，多线程在Python中只能交替执行，
即使100个线程跑在100核CPU上，也只能用到1个核。

解决方案： 多进程
Python虽然不能利用多线程实现多核任务，但可以通过多进程实现多核任务。
多个Python进程有各自独立的GIL锁，互不影响。
'''

# 线程全局变量

# 创建全局ThreadLocal对象:
local_something = threading.local()

# 1  执行线程
def process_say_someting():
	# 获取当前线程关联的student:
	text = local_something.content
	print('Hello, %s (in %s)' % (text, threading.current_thread().name))


# 2  赋值线程
def process_thread(t):
	# 为该线程，绑定ThreadLocal的值:
	local_something.content = t
	process_say_someting()


t1 = threading.Thread(target=process_thread, args=('hhhhh',), name='Thread-A')
t2 = threading.Thread(target=process_thread, args=('wwwwww',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()
