# # 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск). 
# # Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый. 
# # Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение. 
# # Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый). 
# # Проверить работу примера, создав экземпляр и вызвав описанный метод.
import time
from datetime import datetime as dt

class TrafficLight(object):
	 def __init__(self):
		 self._color = {'r':7,'y':2,'g':2}
		 print(sum(self._color.values()))
	
	 def turn_on(self): #сеттер )
		 self.__beg_time = dt.now()
		 # грязный хак в том, что светофор можно в любой момент ребутнуть, дёрнув сеттер
		 # мне кажется, это очень мило соответствует объективной реальности )) "выключи и включи его снова"

	 def get_color(self): #геттер )
		 time_res = int((dt.now()-self.__beg_time).total_seconds()) % sum(self._color.values())
		 # граничных условий не было, сделал приведение в инт
		 # на 6.9999999 секунд ещё горит красный, на 7.00 уже жёлтый
		 if time_res < self._color['r']: return 'red'
		 elif time_res < self._color['r'] + self._color['y']: return 'yellow'
		 else: return 'green'

tl = TrafficLight()
tl.turn_on() 
time.sleep(4) # дебажить туть
print(tl.get_color())

# # 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). 
# # Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. 
# # Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна. 
# # Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
# # Например: 20м * 5000м * 25кг * 5см = 12500 т

class Road(object):
	 def __init__(self, length, width):
		 self._length = length
		 self._width = width

	 def coumt_mass(self,mass,height):
		 return f'{self._length*self._width*mass*height/1000} т'

road = Road(20, 5000)
print(road.coumt_mass(25,5))


# # 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход). 
# # Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}. 
# # Создать класс Position (должность) на базе класса Worker. 
# # В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income). 
# # Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker(object):
	def __init__(self, name, surname, position, wage, bonus):
		self.name = name
		self.surname = surname
		self.position = position
		self._income = {"wage": wage, "bonus": bonus} # зачем такое (((( даже в учебных целях смотрится странно (((

class Position(Worker):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

	def get_full_name(self):
		return self.name + ' ' + self.surname

	def get_total_income(self):
		return self._income['wage'] + self._income['bonus']

vasya = Position('Vasya', 'Pupkin', 'loh', 10000, 1)
print(vasya.get_full_name())
print(vasya.get_total_income())


# # 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево). 
# # А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда). 
# # Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. 
# # Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. 
# # Для классов TownCar и WorkCar переопределите метод show_speed. 
# # При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

class Car(object):
	def __init__(self, speed, color, name, is_police):
		self.speed = speed
		self.color = color
		self.name = name
		self.is_police = is_police
		if color == 'red' : self.speed += 10 # coz red goez fasta!

	def go(self):
		self.speed += 1
		print('Ya edu')
	def stop(self):
		self.speed -= 1
		print('Ya tormozhu')
	def turn(self, direction):
		print(f'Ya povernul {direction}')
	def upal(self):
		print('Ya upal')

	def show_speed(self):
		print(self.speed)


class TownCar(Car):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

	def show_speed(self):
		print('Damn, it\'s too fast, YEEEHAAAW!!!!!' if self.speed > 60 else self.speed)

class SportCar(Car):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

class WorkCar(Car):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

	def show_speed(self):
		print('Damn, it\'s too fast, YEEEHAAAW!!!!!' if self.speed > 40 else self.speed)

class PoliceCar(Car):
	def __init__(self, speed, color, name):
		super().__init__(speed, color, name, is_police = True)

bycicle = TownCar(49, 'red', 'scarlet fury', False)
bycicle.show_speed()
bycicle.stop()
bycicle.show_speed()
bycicle.go()
bycicle.show_speed()
bycicle.turn('napravo')
bycicle.turn('nalevo')
bycicle.go()
bycicle.go()
bycicle.go()
bycicle.show_speed()
print('"Initial D - Deja Vu" PLAYING IN THE DISTANCE')
bycicle.turn('napravo')
bycicle.upal()


# 5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw (отрисовка). 
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). 
# В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен выводить уникальное сообщение. 
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.


class Stationery(object):
	def __init__(self, title):
		self.title = title
	def draw(self):
		print('Запуск отрисовки')

class Pen(Stationery):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
	def draw(self):
		print('This is a pen drawing')

class Pencil(Stationery):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
	def draw(self):
		print('This is a pencil drawing')

class Handle(Stationery):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
	def draw(self):
		print('This is a handle drawing')

hand = Stationery('dirty hand')
hand.draw()
pen = Pen('pen')
pen.draw()
pencil = Pencil('pencil')
pencil.draw()
handle = Handle('handle')
handle.draw()
