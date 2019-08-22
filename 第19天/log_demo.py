#演示 使用 loguru管理日志输出
from loguru import logger

def demo_log():
	logger.debug("这是一条debug日志")
	logger.info("这是一条info日志")
	logger.error("这是一条error日志")

def demo_log_to_file():
	logger.add("log/file_{time}.log")
	demo_log()

def demo_log_level():
	logger.add("log/error_file_{time}.log", format="{time} {level} {message}", filter="", level="ERROR")
	demo_log()

@logger.catch
def demo_log_catch():
	print("log catch")

demo_log()
demo_log_to_file()
demo_log_level()
demo_log_catch()
