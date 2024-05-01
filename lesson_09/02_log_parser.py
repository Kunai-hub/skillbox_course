# -*- coding: utf-8 -*-
from pprint import pprint

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

from collections import defaultdict
import re

file_name = 'events.txt'
pattern_datetime = re.compile('\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}).+\]')
date_by_counter = defaultdict(int)

with open(file_name) as file:
    for line in file:
        if 'NOK' not in line:
            continue

        match = pattern_datetime.search(line)
        if match:
            date_str = match.group(1)
            date_by_counter[date_str] += 1

for k, v in date_by_counter.items():
    print(f'[{k}] {v}')

# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
