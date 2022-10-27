class Rectangle:
	def __init__(self, a, b):
		self.a = a 
		self.b = b 

	def area(self):
		return self.a * self.b 

class Square:
	def __init__(self, a):
		self.a = a 

	def area(self):
		return self.a * self.a 

class Employee:
	def __init__(self, name, email, phone):
		self.name = name
		self.email = email
		self.phone = phone 

	def show(self):
		print(self.name, self. email, self.phone)