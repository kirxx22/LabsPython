import csv
import pandas as pd
from pprint import pprint

SEP = '\n' + '─' * 30 + '\n'
PATH = 'Lab-2/result.txt'
CSV = 'Lab-2/books-en.csv'
XML = 'Lab-2/currency.xml'

'''
Задание № 1
Вывести количество записей, у которых в поле Название строка длиннее 30 символов.
'''
data = pd.read_csv(CSV, delimiter=';', encoding='cp1252')
data.Downloads = data.Downloads.apply(int)
data.Price = data.Price.apply(lambda x: float(x.replace(',', '.')))

count = len([i for i in data['Book-Title'].values if len(i) > 30])
print(count)

print(SEP)

'''
### Задание № 2
Реализовать поиск книги по автору,
использовать ограничение на выдачу в зависимости от варианта.
**Ограничение**: _До 200 рублей_
'''

author = input('Введите запрос: ')
print()
response = data[(data.Price < 200) & (data['Book-Author'] == author)]
if len(response) == 0:
    print('Ничего не найдено')
else:
    print(response)

print(SEP)

'''
Задание № 3
Реализовать генератор библиографических ссылок вида ```<автор>. <название> - <год>``` для 20 записей.
Записи выбрать произвольно.
Список сохраняется как отдельный файл текстового формата с нумерацией строк.
'''

pattern = '{}. {} - {}\n'
f = open(PATH, 'w')
for _ in range(20):
    row = data.loc[_]
    f.write(pattern.format(row['Book-Author'], row['Book-Title'], row['Year-Of-Publication']))
f.close()

'''
Задание № 4
Распарсить файл и извлечь данные, согласно варианту.
Выполнить приведения типов по необходимости.

Тип данных: Словарь "NumCode - CharCode"
'''

data = pd.read_xml(XML, encoding='cp1252')
result = data.loc[:, 'NumCode':'CharCode']
sl = {i: j for i, j in zip(result.NumCode.values, result.CharCode.values)}
pprint(sl)

print(SEP)

print('ДОПЗАДАНИЕ')

'''
## Допзадание

- Вывести перечень всех тегов без повторений (для books-en.csv - перечень издательств без повторений).
- Самые популярные 20 книг.
'''

print(SEP)

data = pd.read_csv(CSV, delimiter=';', encoding='cp1252')
data.Downloads = data.Downloads.apply(int)
data.Price = data.Price.apply(lambda x: float(x.replace(',', '.')))

print(data.Publisher.unique())

print(SEP)

result = data.sort_values(by='Downloads', ascending=False).reset_index()[:20]
print(result)