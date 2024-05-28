# -*- coding: utf-8 -*-
import zipfile

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


class Statistic:

    def __init__(self, file_name):
        self.file_name = file_name
        self.stat = {}

    def unzip(self):
        file_zip = zipfile.ZipFile(file=self.file_name, mode='r')
        for file_txt in file_zip.namelist():
            file_zip.extract(file_txt)
        self.file_name = file_txt

    def stat_collection(self):
        if self.file_name.endswith('.zip'):
            self.unzip()
        with open(file=self.file_name, mode='r', encoding='cp1251') as file:
            for line in file:
                self._char_check(line=line)

    def _char_check(self, line):
        for char in line:
            if char.isalpha():
                if char in self.stat:
                    self.stat[char] += 1
                else:
                    self.stat[char] = 1
            else:
                pass

    def stat_print(self):
        letter = 'Буква'
        hertz = 'Частота'
        plus = '+'
        pipe = '|'
        total = 'Итого'

        print(f'{plus}{plus:-^28}{plus}')
        print(f'{pipe}{letter:^12}{pipe:^4}{hertz:^12}{pipe}')
        print(f'{plus}{plus:-^28}{plus}')

        sorted_hertz = sorted(self.stat.items(), key=lambda x: x[1], reverse=True)
        for char, count in sorted_hertz:
            print(f'{pipe}{char:^12}{pipe:^4}{count:^12}{pipe}')

        print(f'{plus}{plus:-^28}{plus}')
        print(f'{pipe}{total:^12}{pipe:^4}{sum(self.stat.values()):^12}{pipe}')
        print(f'{plus}{plus:-^28}{plus}')


stat_voyna = Statistic(file_name='voyna-i-mir.txt')
stat_voyna.stat_collection()
stat_voyna.stat_print()

# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
