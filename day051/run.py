# 多进程
import hashlib
from time import sleep

# TODO  多进程
from multiprocessing import Process
import os

# 演示函数 1 ： 工作量证明
def proof_fo_work():
	"""
	简单的工作量证明:
         - 查找一个 p' 使得 hash(pp') 以4个0开头
         - p 是上一个块的证明,  p' 是当前的证明
        :param last_proof: <int>
        :return: <int>
	:return:
	"""
	originHash = hashlib.sha256("lsy".encode()).hexdigest()
	print("Origin Hash：", originHash)
	proof = 0
	hard = "0"
	while True:
		guessStr = f"{originHash}{proof}".encode()
		guessHash = hashlib.sha256(guessStr).hexdigest()
		if guessHash[:1] == hard:
			print("***符合要求***: ", guessHash)
			print("***Proof***: ", proof)
			sleep(6)
			hard = hard + "0"
		else:
			print(guessHash)
			proof = proof + 1

# 演示函数 2 ： 打印
def t(name):
	sleep(1)
	print(f"子进程： {name}, {os.getpid()}")

# 进程的使用： 启动进程分别执行 函数1,2
def use_process():
	print(f"主进程: {os.getpid()}")
	# 创建test进程
	p = Process(target=t, args=('testProcess',))
	# 创建proof_fo_work 进程
	p2 = Process(target=proof_fo_work)
	p2.start()
	#p2.join()   # 使用之后，p进程将等待p2结束才执行
	print("启动测试进程")
	p.start()


# 进程池的使用
def pool_process():
	from multiprocessing import Pool

	# 如果要启动大量的子进程，可以用进程池的方式批量创建子进程：
	p = Pool(4)  # 4为 CPU 核心数， 四核CPU 最多执行4 ， 大于4 也只执行4个进程
	for i in range(5):
		p.apply_async(t, args=(i,))
		print("完成全部进程的创建启动", i)
		sleep(1)
	p.close()
	p.join()

# 进程的通信： 多线程 生成者+消费者 Queue 实现
def message_process():
	from multiprocessing import Queue

	q = Queue()

	pw = Process(target=producer, args=(q,))   # 生产进程
	pr = Process(target=consumer, args=(q, "P1"))   # 消费进程 1
	pr2 = Process(target=consumer, args=(q, "P2"))  # 消费进程 2
	pr3 = Process(target=consumer, args=(q, "P3"))  # 消费进程 3
	pr4 = Process(target=consumer, args=(q, "P4"))  # 消费进程 4
	pr5 = Process(target=consumer, args=(q, "P5"))  # 消费进程 5

	pw.start()
	pr.start()
	pr2.start()
	pr3.start()
	pr4.start()
	pr5.start()

	# 等待pw结束:
	pw.join()
	# 队列消费完成 结束进程
	while True:
		if q.qsize() == 0:
			# pr,pr2进程里是死循环，无法等待其结束，只能强行终止:
			pr.terminate()
			pr2.terminate()
			pr3.terminate()
			pr4.terminate()
			pr5.terminate()
			print("队列数据： ", q.qsize())
			break


# 往队列里生产数据
def producer(q):
	import random, time
	print('Hash生成进程: %s' % os.getpid())
	# 生产 100个
	for i in range(100):
		num = random.randint(0, 1000)
		value_hash = hashlib.sha256(str(num).encode()).hexdigest()
		print('生成地址：[ %s ] to queue...' % value_hash)
		q.put(value_hash)  # 数据写入队列


# 消费队列里的数据
def consumer(q, name):
	import random, time
	print('获取地址消费: %s ' % os.getpid())
	while True:
		value = q.get(True)
		print(f'**{name}-读取地址: [ {value} ] from queue.')
		time.sleep(random.random())


if __name__ == "__main__":
	message_process()


