import time 
def countdown(n):
    while n > 0:
        print('T-minus', n)
        n = n - 1
        time.sleep(5)

from threading import Thread 

t = Thread(target=countdown, args=(10,))
t.start()


if t.is_alive():
    print("线程启动中...")
else:
    print("线程完成任务.")