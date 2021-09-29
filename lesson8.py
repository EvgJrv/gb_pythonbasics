# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год». 
# В рамках класса реализовать два метода. 
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». 
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12). 
# Проверить работу полученной структуры на реальных данных.
import datetime

class MyDate(object):
    return_int = True

    def __init__(self, datestring):
        self.datestring = datestring
        self.d = ""
        self.m = ""
        self.yyyy = ""

    @classmethod
    # я вообще не придумал, зачем этому методу быть методом класса, поэтому пусть будет какая-то переменная класса, которую он будет использовать.
    def to_int(cls, datestring):
        datestring_split = datestring.split("-")
        if cls.return_int:
            return list(map(int, datestring_split))
        else:
            return datestring_split

    @staticmethod
    def validate(datestring):
        try:
            datetime.datetime.strptime(datestring, '%d-%m-%Y')
            return 'Date OK'
        except ValueError:
            return 'Your date is crap. Make it DD-MM-YYYY'
        
a = MyDate("11-13-2011")
print(*MyDate.to_int(a.datestring))
print(*MyDate.validate(a.datestring))

# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных, вводимых пользователем. 
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class MyZDError(ZeroDivisionError):
	pass

def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError as exc:
        print('Dude, i smell some zero division here')
        raise MyZDError from exc

a,b = 1,0
try:
    print(divide(a,b))
except MyZDError:
    print('there was no abnormal abortion')
print('proceed')


# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел. 
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список. 
# Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта, введя, например, команду “stop”. 
# При этом скрипт завершается, сформированный список выводится на экран.
# Подсказка: для данного задания примем, что пользователь может вводить только числа и строки. 
# При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить его в список, только если введено число. 
# Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение. При этом работа скрипта не должна завершаться.

class NotIntError(ValueError):
	pass

'''к чёрту пользователя, ненавижу input(), будем его эмулировать'''

user_input = ['1', '2', '3', 'dude', '4', '5', 'hi', '6', '7', 'sudo shutdown now']
result = []
for i in user_input:
    try:
        try:
            result.append(int(i))
        except ValueError: 
            raise NotIntError
    except NotIntError:
        if i == 'sudo shutdown now': break
        print('non-integer input')
print(result)

# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. 
# А также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). 
# В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

from pprint import pprint

class Warehouse:
    def __init__(self) -> None:
        self.equip_list = []

class OfficeEquip(object):
    def __init__(self, warehouse, name) -> None:
        self.name = name
        warehouse.equip_list.append(self)

class Printer(OfficeEquip):
    def __init__(self, ppi, *args, **kwargs) -> None:
        self.ppi = ppi
        super().__init__(*args, **kwargs)

class Scaner(OfficeEquip):
    def __init__(self, size, *args, **kwargs) -> None:
        self.size = size
        super().__init__(*args, **kwargs)

class Copier(OfficeEquip):
    def __init__(self, speed, *args, **kwargs) -> None:
        self.speed = speed
        super().__init__(*args, **kwargs)

wh = Warehouse()
pr = Printer(666, wh, 'canon')
sc = Scaner('A4', wh, 'kyocera')
c = Copier(90, wh, 'xerox')
pprint(vars(wh))
pprint(vars(pr))
pprint(vars(sc))
pprint(vars(c))


# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании. 
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь.
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. 
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.


class Department:
    def __init__(self) -> None:
        pass
    def add_equipment(self, equipment, qty):
        pass

class Warehouse:
    def __init__(self) -> None:
        self.equip_dict = dict()

    def add_equip(self, equip, qty):
        if type(qty) is not int: raise ValueError
        dict_qty = self.equip_dict.get(equip)
        if dict_qty:
            self.equip_dict.update({equip: qty+dict_qty})
        else: 
            self.equip_dict.update({equip: qty})

    def push_equip(self, equip, qty, department):
        if type(qty) is not int: raise ValueError
        dict_qty = self.equip_dict.get(equip)
        if dict_qty > qty:
            self.equip_dict[equip] = dict_qty-qty
            department.add_equipment(equip, qty)
        elif dict_qty == qty:
            self.equip_dict.pop(equip)
            department.add_equipment(equip, qty)
        else:
            print('Nope')

class OfficeEquip(object):
    def __init__(self, name) -> None:
        self.name = name

wh = Warehouse()
pr = OfficeEquip('canon')
wh.add_equip(pr, 10)
print(wh.equip_dict)
wh.add_equip(pr, 2)
print(wh.equip_dict)
dep = Department()
wh.push_equip(pr, 5, dep)
print(wh.equip_dict)


# 7. Реализовать проект «Операции с комплексными числами». ....

'''Это писали на одном из уроков. Мне ОЧЕНЬ не хочется копипастить этот код'''