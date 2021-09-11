# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. 
# Об окончании ввода данных свидетельствует пустая строка.

with open('file1.txt', 'w') as file:
    def line_adder(file):
        i = input('blank line is a stop sequence \n')
        if i:
            file.write(i+'\n')
            # это грязный хак с переносом строки, явно можно как-то красивее, но мне лень искать. Может и в лекции будет
            # судя по всему тут надо было открывать в режиме 'a', но мне уже лень переделывать
            line_adder(file)
        else:
            return True
    line_adder(file)


# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.
with open('file2.txt', 'r') as file:
    lines = file.readlines()
    print(f'File consists of {len(lines)} lines')
    for k,v in enumerate(lines):
        print(f'line {k} consists of {len(v)} chars')
    print('(counting \'\\n\' as one char)')


# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. 
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
from statistics import mean
salary=[]
with open('file3.txt', 'r') as file:
    for line in file.readlines():
        line = line.split(' ')
        if int(line[1]) < 20000 : print(line[0])
        salary.append(int(line[1]))
print(mean(salary))

# 4. Создать (не программно) текстовый файл со следующим содержимым (...):
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. 
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

megadict = {'One':'Один',
'Two':'Один два раза',
'Three':'два нуля до тракториста',
'Four':'Четыыыыыыре'}
with open('file4_new.txt', 'a') as file4_new:
    with open('file4.txt', 'r') as file4:
        for line in file4:
            line = line.split()
            line[0] = megadict[line[0]]
            line = ' '.join(line)
            print(line, file=file4_new)


# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. 
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from random import sample
from functools import reduce
with open('file5.txt', 'w') as file5:
    print(*sample(range(1, 10), 5), file=file5)
    # file5.mode = 'r' # так почему-то не хочет, надо переоткрывать, или изначально быть в r+ ((
with open('file5.txt', 'r') as file5:
    line = file5.readline()
    print(line, 'sum ==', sum(map(lambda x: int(x),line.split())))


# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных, 
# практических и лабораторных занятий по этому предмету и их количество. 
# Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему. 
# Вывести словарь на экран.

import re
task6 = {}
with open('file6.txt', 'r') as file6:
    for line in file6.readlines():
        line = line.split(':')
        task6[line[0]] = sum(map(lambda x: int(x), re.findall('([\d]+)', line[1])))
print(task6)


# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

from statistics import mean
from json import dumps

firms = {}
with open('file7.txt', 'r') as file:
    for line in file.readlines():
        line = line.strip().split(' ')
        firms[line[0]] = int(line[2]) - int(line[3])
output = [firms, {"average_profit": mean([p for p in [*firms.values()] if p > 0])}]
with open('file7_new.txt', 'w') as file:
    print(dumps(output), file=file)