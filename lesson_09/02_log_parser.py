# -*- coding: utf-8 -*-
# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.
import os
from collections import defaultdict
import re

# file_name = 'events.txt'
# pattern_datetime = re.compile('\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}).+\]')
# date_by_counter = defaultdict(int)
#
# with open(file_name) as file:
#     for line in file:
#         if 'NOK' not in line:
#             continue
#
#         match = pattern_datetime.search(line)
#         if match:
#             date_str = match.group(1)
#             date_by_counter[date_str] += 1
#
# for k, v in date_by_counter.items():
#     print(f'[{k}] {v}')


class LogParser:

    def __init__(self, file_in=None, file_out=None):
        self.file_in = file_in
        self.file_out = file_out
        self.log_stat = {}

        # if not self.file_out:
        #     self.file_out = self.file_in + '.nok'

        # if os.path.exists(self.file_out):
        #     os.remove(self.file_out)

    def line_parsing(self, line):
        date, time, res = line.split(' ')
        dt = date + ' ' + time[:5] + time[-1:]
        return dt, res

    def parse(self):
        with open(self.file_in, 'r') as file:
            for line in file:
                dt, res = self.line_parsing(line)
                res = res.replace('\n', '')
                if res == 'NOK':
                    if dt not in self.log_stat.keys():
                        for date, cnt in self.log_stat.items():
                            print(f'{date} {cnt}')
                        # self.write()
                        self.log_stat = {}
                    self.log_stat[dt] = self.log_stat.setdefault(dt, 0) + 1

    # def write(self):
    #     with open(file=self.file_out, mode='a', encoding='utf8') as file:
    #         for date, cnt in self.log_stat.items():
    #             file.write(f'{date} {cnt} \n')


if __name__ == '__main__':
    log = LogParser(file_in='events.txt')
    log.parse()

# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
