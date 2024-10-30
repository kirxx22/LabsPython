import os
import time
import plotly.express as px
import sys


# Константы
RED = '\u001b[41m'
WHITE = '\u001b[47m'
BLACK = '\033[40m'
END = '\u001b[0m'
SEP = '\n' + '─' * 30 + '\n'

'''
Задание № 1
Сгенерировать при помощи escape-символов в консоли изображение флага,
соответственно варианту (столбец "Страна")
'''
for i in range(6):
    if i < 3:
        print(f"{WHITE}{' ' * 16}{END}")
    else:
        print(f"{RED}{' ' * 16}{END}")

print(SEP)

'''
Задание № 2
Сгенерировать в консоли повторяющийся узор (столбец "Узор").
'''
def make_image(mat: list[list[int]]) -> str:
    return '\n'.join([''.join(map(str, row)) for row in mat])

plot_list = [[0 for i in range(10)] for i in range(10)]
exist = f'{BLACK}  {END}'
not_exist = f'{WHITE}  {END}'

for i in range(10):
    if i in (0, 1, 4, 5, 8, 9):
        plot_list[i] = [exist for i in range(10)]
    elif i in (2, 3):
        plot_list[i] = [not_exist for _ in range(4)] + [exist]
        plot_list[i] =  plot_list[i] + plot_list[i][::-1]
    else:
        plot_list[i] = [not_exist, exist, exist, not_exist, not_exist]
        plot_list[i] = plot_list[i] + plot_list[i][::-1]

print(make_image(plot_list))

print(SEP)

'''
Задание № 3
Сгенерировать в консоли график функции (1 четверти) при помощи escape-символов,
минимум 9 строк в высоту (столбец "Функция").
'''
plot_list = [[0 for i in range(10)] for i in range(10)]
result = []

for i in range(10):
    result.append(round(i ** 0.5, 3))

step = round(abs(result[0] - result[9]) / 9, 3)

for i in range(10):
    for j in range(10):
        if j == 0:
            plot_list[i][j] = round(step * (8-i) + step, 3)

for i in range(9):
    for j in range(10):
        if abs(plot_list[i][0] - result[9 - j]) < step:
            for k in range(9):
                if 8 - k == j:
                    plot_list[i][k+1] = 1
print('\t\t↑ y')
for i in range(9):
    line = ''
    for j in range(10):
        if j == 0:
            line += '\t' + str(plot_list[i][j]) + '\t│'
        if plot_list[i][j] == 0:
            line += '--'
        if plot_list[i][j] == 1:
            line += '!!'
    print(line)
print('\t\t└' + '─' * 18 + '→')
print('\t0\t1 2 3 4 5 6 7 8 9  x')

print(SEP)

'''
Задание № 4
Используя прилагаемый файл с числовой последовательностью sequence.txt,
вывести диаграмму процентного соотношения согласно варианту.
'''
path = 'Lab-1/sequence.txt'
with open(path, 'r') as f:
    data = list(map(float, f.readlines()))

data = [abs(i) for i in data]

first = round(sum(data[:125]) / 125, 3)
second = round(sum(data[125:]) / 125, 3)
s = first + second

first_percent = round(first / s, 4)
second_percent = round(second / s, 4)

print(f'{RED}' + ' ' * int(first_percent * 30) + f'{END}' + ' ' + str(first_percent * 100))
print(f'{WHITE}' + ' ' * int(second_percent * 30) + f'{END}' + ' ' + str(second_percent * 100))
