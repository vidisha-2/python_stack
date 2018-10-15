class MathDojo:
	def __init__(self):
		self.result=0
	def add(self, *args):
		for num in args:
			self.result += num

		return self
	def sub(self, *args):
		for num in args:
			self.result -= num
		
		return self		

md=MathDojo()
x=md.add(2,4,8).sub(1,2).result
print(x)


