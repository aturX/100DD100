"""
这样保证密码在保存时，不是明文存储，且保存的密码摘要可做登录验证
"""

def demo():
	import hashlib
	salt = '%@!lsy'
	password = "123456789"
	password2 = "abcdef"
	password3 = "1"
	password4 = "123abc"
	password5 = "adfasgfdgdhafsgdsgreewrsdggds"
	def sha256(ascii_str):
		# 采用sha256加密方式
		return hashlib.sha256(ascii_str.encode('ascii')).hexdigest()
	hash1 = sha256(password)
	hash2 = sha256(hash1 + salt)

	return hash2

def demo2(pwd):
	import hashlib
	# 用 ascii 编码转换成 bytes 对象
	p = pwd.encode('ascii')
	s = hashlib.sha256(p)
	# 返回摘要字符串
	return s.hexdigest()

print(demo2("123"))
# demo()
s = "a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3"

print(demo2("123") == s)