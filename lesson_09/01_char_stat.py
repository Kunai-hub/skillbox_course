# -*- coding: utf-8 -*-
import zipfile
from pprint import pprint

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

# file_name = 'C:\\Users\\neni2\PycharmProjects\\Kirill\kunai\lesson_09\\python_snippets\\voyna-i-mir.txt.zip'
# file_zip = zipfile.ZipFile(file=file_name, mode='r')
#
# for file_txt in file_zip.namelist():
#     file_zip.extract(file_txt)

file_name = 'voyna-i-mir.txt'

stat = {}

with open(file=file_name, mode='r', encoding='cp1251') as file:
    for line in file:
        for char in line:
            if char.isalpha():
                if char in stat:
                    stat[char] += 1
                else:
                    stat[char] = 1
            else:
                pass


letter = 'Буква'
hertz = 'Частота'
plus = '+'
pipe = '|'
total = 'Итого'
print(f'{plus}{plus:-^28}{plus}')
print(f'{pipe}{letter:^12}{pipe:^4}{hertz:^12}{pipe}')
print(f'{plus}{plus:-^28}{plus}')
sorted_hertz = sorted(stat.items(), key=lambda x: x[1], reverse=True)
for char, count in sorted_hertz:
    print(f'{pipe}{char:^12}{pipe:^4}{count:^12}{pipe}')
print(f'{plus}{plus:-^28}{plus}')
print(f'{pipe}{total:^12}{pipe:^4}{sum(stat.values()):^12}{pipe}')
print(f'{plus}{plus:-^28}{plus}')

# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
