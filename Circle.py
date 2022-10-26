class Circle:
	def __init__(self, radius):
		self.radius = radius

	def area(self):
		return 3.1416 * self.radius * self.radius

	def circumference(self):
		return 2 * 3.1416 * self.radius

	def returnAll(self):
		return self.area(), self.circumference()