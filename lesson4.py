# # 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. 
# # В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# # Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv
print(int(argv[1])*int(argv[2])+int(argv[3]))

# # 2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# # Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
# # Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# # Результат: [12, 44, 4, 10, 78, 123].

a = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
b = [v for k,v in enumerate(a) if v > a[k-1] and k!=0]
# как тут нормально хэндлить начальный элемент, чтобы он не сравнивался с последним? я не придумал ничего изящнее хардкода граничного условия
print(b)


# # 3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
# # Подсказка: использовать функцию range() и генератор.
'''
Господь Всемогущий, когда, и за каким хуем "List Comprehensions" успело стать "генератором", если термин "генератор" уже существует десятилетиями?
как же невероятно сильно у меня БОМБИТ
лучи ярости просто во все стороны
хорошо хоть не переопределили термин "int", или там "функция"
'''
print([i for i in range(241) if i != 0 and (i % 20 == 0 or i % 21 == 0)])
# вы хотите увидеть в этом задании range (20, 241), но без него веселее ))

# # 4. Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать итоговый массив чисел, соответствующих требованию. 
# # Элементы вывести в порядке их следования в исходном списке. Для выполнения задания обязательно использовать генератор.
# # Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# # Результат: [23, 1, 3, 10, 4, 11]

a = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print([i for i in a if a.count(i) == 1])

# # 5. Реализовать формирование списка, используя функцию range() и возможности генератора. 
# # В список должны войти четные числа от 100 до 1000 (включая границы). Необходимо получить результат вычисления произведения всех элементов списка.
# # Подсказка: использовать функцию reduce().
from functools import reduce

r = [i for i in range(100, 1001, 2)]
print(reduce(lambda x,y: x*y, r))

# # 6. Реализовать два небольших скрипта:
# # а) итератор, генерирующий целые числа, начиная с указанного,
# # б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# # Подсказка: использовать функцию count() и cycle() модуля itertools. 
# # Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
# # Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл. 
# # Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
from itertools import count, cycle

def my_count(beg):
    limit = 10
    max = limit+beg
    for i in count(beg):
        if i == max:
            break
        else:
            yield i
print([i for i in my_count(3)])

def my_cycle(lst):
    limit = 10
    if isinstance(lst, (list, tuple, str)):
        for k,v in enumerate(cycle(lst)):
            if k == limit:
                break
            else:
                yield v
print([i for i in my_cycle('actg')])

# 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение. 
# При вызове функции должен создаваться объект-генератор. Функция должна вызываться следующим образом: for el in fact(n). 
# Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

#попроще
from math import factorial
def fact(n):
    for i in range(1,n+1):
        yield factorial(i)
print([el for el in fact(5)])

#повеселее
def recurse_fact(maxn,step=1,current=1):
    current *= step
    yield current
    if step != maxn:
        yield from recurse_fact(maxn,step+1,current)
print([el for el in recurse_fact(5)])