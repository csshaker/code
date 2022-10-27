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

	def circumference(self):
		return 4 * self.a 

class Triangle:
	def __init__(self, base, height):
		self.base = base
		self.height = height

	def area(self):
		return 0.5 * self.base * self.height

class Employee:
	def __init__(self, name, email, phone):
		self.name = name
		self.email = email
		self.phone = phone 

	def show(self):
		print(self.name, self. email, self.phone)

	def returnEmployee(self):
		return self

	def returnEmail(self):
		return self.email

class UnitConversion:
	def __init__(self, unit):
		self.unit = unit 