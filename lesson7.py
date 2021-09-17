class GoFuckYourselveError(Exception):
	pass

# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.

class Matrix(list):
	def __init__(self, listlist):
		for i in listlist:
			if not isinstance(i, list): raise GoFuckYourselveError
			for j in i:
				if not isinstance(j, (int, float)): raise GoFuckYourselveError
		super().__init__(listlist)

	def __str__(self):
		ret_str = ''
		for i in self:
			ret_str += ' '.join([str(j) for j in i]) + '\n'
		return ret_str

	def __add__(self, other):
		if (len(self) != len(other)) or (len(self[0]) != len(other[0])): raise GoFuckYourselveError
		for i in range(len(self)): #enumerate тут будет только мешать
			for j in range(len(self[i])):
				self[i][j] += other[i][j]
		return self

m = Matrix([[1,2,3],[4,5,6]])
print(m)
q = Matrix([[1,2,3.0],[4,2,8]])
print(q)
print(type(m+q))
print(m+q)


# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды. 
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название. 
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). 
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). 
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. 
# Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

'''Описание задачи писали творческие люди. Сделаю как пойдёт. 
Одежда может иметь определённое название = "Плащ пылающей ярости", "Штаны загадочного коричневого пятна сзади", "Майка Пивозавра +2d4 на бросок алкоголизма".
'''


class Clothes(object):
	def __init__(self, name):
		self.name = name
		super().__init__()

	@property
	def square(self):
		return 'пусть тут будет эта лабуда, чтобы при создании дочерних классов ХОТЬ ЧТО-ТО переопределилось, и этот класс не был 100% бесполезным.'

class Coat(Clothes):
	def __init__(self, name, v: int):
		if type(v) not in (int, float) or v <= 0: raise GoFuckYourselveError('в игры со мной играть удумал?')
		self.v = v
		super().__init__(name)

	@property	
	def square(self):
		return self.v/6.5 + 0.5


class Suit(Clothes):
	def __init__(self, name, h: int):
		if type(h) not in (int, float) or h <= 0: raise GoFuckYourselveError('в игры со мной играть удумал?')
		self.h = h
		super().__init__(name)

	@property
	def square(self):
		return self.h*2 + 0.3

clothes_list = []

clothes_list.append(Coat('cool coat', 6.5))
clothes_list.append(Suit('tuxedo for masked guy', 10))
total_square = sum([cl.square for cl in clothes_list])

print(clothes_list[0].square)
print(clothes_list[1].square)
print(total_square)

# 3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка. 
# В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число). 
# В классе должны быть реализованы методы перегрузки арифметических операторов: 
# сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
# Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и обычное (не целочисленное) деление клеток, соответственно. 
# В методе деления должно осуществляться округление значения до целого числа.
# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
# Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
# Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу. Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n*****.
# Подсказка: подробный список операторов для перегрузки доступен по ссылке.

'''
Это задание вообще загадочно описано. 
'''

class Nope(UserWarning, ValueError):
	pass

class Cell(object):
	def __init__(self, i):
		self.i = i
		super().__init__()

	def make_order(self, l: int):
		if type(l) !=int or l <= 0: raise GoFuckYourselveError
		return (('*'*l)+'\n')*(self.i//l)+('*'*(self.i%l))

	def __truediv__(self, other):
		if type(other) != Cell: raise GoFuckYourselveError
		try:
			return Cell(self.i // other.i)
		except:
			raise GoFuckYourselveError('есть подозрительное ощущение, что тут происходит ZeroDivisionError')

	def __mul__(self, other):
		if type(other) != Cell: raise GoFuckYourselveError
		return Cell(self.i * other.i)

	def __add__(self, other):
		if type(other) != Cell: raise GoFuckYourselveError
		return Cell(self.i + other.i)

	def __sub__(self, other):
		if type(other) != Cell: raise GoFuckYourselveError
		if self.i <= other.i:
			raise Nope('маленькость значения необъяснима')
		else:
			return Cell(self.i - other.i)

c = Cell(5)
print(c.make_order(5))
m = Cell(5)
print(c + 1)
print((c*m).make_order(5))
print((c/m).make_order(5))
print((c-m).make_order(5))
print((c+m).make_order(5))