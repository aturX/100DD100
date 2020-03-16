# your code goes here
def log(*args, **kwargs):
	print("Log", *args, **kwargs)

def sumAB(a, b):
	r = int(a) + int(b)
	return r

def decAB(a, b): 
    r = int(a) - int(b)
    return r


def mulAB(a, b):
	r = int(a) * int(b)
	return r

def divAB(a, b):
	
	if int(b) != 0:
		r = int(a) / int(b)
	else:
		r = False
	return r

def run(a, ch, b):
	
	if ch == "+":
		r = sumAB(a, b)
	elif ch == "-":
		r = decAB(a, b)
	elif ch == "*":
		r = mulAB(a, b)
	elif ch == "/":
		r = divAB(a, b)
	else:
		r = False
	return r 

def main():
	a = input("输入a： ")
	ch = input("输入运算符：")
	b = input("输入b:  ")
	r = run(a, ch, b)
	log("结果是: ", r)
    

main()
    
   