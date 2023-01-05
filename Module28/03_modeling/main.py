# TODO здесь писать код

class Figure:
	figure_name = 'Фигура'
	
	def __init__(self, figure_name):
		self.figure_name = figure_name
	
	def show_name(self):
		print(self.figure_name)

class Circle(Figure):
	def __init__(self, radius):
		super().__init__('Круг')
		self.radius = radius

	def get_square(self):
		return(3.14 * self.radius**2)
	
	def get_perimeter(self):
		return(2 * 3.14 * self.radius)

class Quad(Figure):
	def __init__(self, a, b):
		super().__init__('Четырехугольник')
		self.a = a
		self.b = b
		
	def get_square(self):
		return(self.a * self.b)
	
	def get_perimeter(self):
		return(2 * (self.a + self.b))

class Square(Figure):
	def __init__(self, a):
		super().__init__('Квадрат')
		self.a = a
		
	def get_square(self):
		return(self.a**2)
	
	def get_perimeter(self):
		return(4 * self.a)

class Triangle(Figure):
	def __init__(self, a, b, c):
		super().__init__('Треугольник')
		self.a = a
		self.b = b
		self.c = c
		
	def get_square(self):
		return(self.a * self.b * self.c)
	
	def get_perimeter(self):
		return(self.a + self.b + self.c)

