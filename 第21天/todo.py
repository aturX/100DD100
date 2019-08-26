from models import Model

class Todo(Model):
	def __init__(self, form):
		print("创建Todo")
		self.id = form.get('id', None)
		self.title = form.get('title', '')
		self.time = form.get('time', 'now')
