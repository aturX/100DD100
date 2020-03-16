from routes import template


def template_test():
	r = template("index.html")
	print(r)
