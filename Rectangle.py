class Rectangle:
	def __init__(self, a, b):
		self.a = a 
		self.b = b 

	def area(self):
		return self.a * self.b 

	def circumference(self):
		return 2 * (self.a + self.b)

class Square:
	def __init__(self, a):
		self.a = a 

	def area(self):
		return self.a * self.a 
