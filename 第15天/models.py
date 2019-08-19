from flask import json

from utils import log


def save(data, path):
	"""
	    本函数把一个 dict 或者 list 写入文件
	    data 是 dict 或者 list
	    path 是保存文件的路径
	    """
	# json 是一个序列化/反序列化(上课会讲这两个名词) list/dict 的库
	# indent 是缩进
	# ensure_ascii=False 用于保存中文
	s = json.dumps(data, indent=2, ensure_ascii=False)
	with open(path, "a+", encoding='utf-8') as f:
		log('save', data)
		f.write(s)
