# -*- coding: utf-8 -*-
import os
import threading
from collections import defaultdict
from lesson_12.python_snippets.utils import time_track


# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПОТОЧНОМ стиле
#
# Бумаги с нулевой волатильностью вывести отдельно.
# Результаты вывести на консоль в виде:
#   Максимальная волатильность:
#       ТИКЕР1 - ХХХ.ХХ %
#       ТИКЕР2 - ХХХ.ХХ %
#       ТИКЕР3 - ХХХ.ХХ %
#   Минимальная волатильность:
#       ТИКЕР4 - ХХХ.ХХ %
#       ТИКЕР5 - ХХХ.ХХ %
#       ТИКЕР6 - ХХХ.ХХ %
#   Нулевая волатильность:
#       ТИКЕР7, ТИКЕР8, ТИКЕР9, ТИКЕР10, ТИКЕР11, ТИКЕР12
# Волатильности указывать в порядке убывания. Тикеры с нулевой волатильностью упорядочить по имени.

class Volatility(threading.Thread):

    def __init__(self, SECID, sourse, lock, results, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.file_name = SECID
        self.sourse = sourse
        self.volatility, self.max_price, self.min_price = 0, 0, 0
        self.lock = lock
        self.results = results

    def run(self):
        self.max_price, self.min_price = 0, 0
        full_file_path = os.path.join(self.sourse, self.file_name)
        with open(file=full_file_path, mode='r', encoding='cp1251') as data:
            file_content = data.read().split('\n')
            for line in file_content:
                if line != '':
                    price = line.split(',')[2]
                    if price != 'PRICE':
                        price = float(price)
                        if self.max_price != 0 and self.min_price != 0:
                            if price > self.max_price:
                                self.max_price = price
                            elif price < self.min_price:
                                self.min_price = price
                        else:
                            self.max_price, self.min_price = price, price
        half_sum = (self.max_price + self.min_price) / 2
        self.volatility = round(((self.max_price - self.min_price) / half_sum) * 100, 2)
        with self.lock:
            self.results[self.file_name] = self.volatility


@time_track
def main():
    sourse = r'C:\Users\neni2\PycharmProjects\Kirill\kunai\lesson_12\trades'
    SECIDS = os.listdir(sourse)
    lock = threading.Lock()
    result = defaultdict(int)
    volatilities = [Volatility(SECID=SECID, sourse=sourse, lock=lock, results=result) for SECID in SECIDS]
    for volatility in volatilities:
        volatility.start()
    for volatility in volatilities:
        volatility.join()

    print('Максимальная волатильность:')
    counter = 0
    number_of_max_and_min_volatility = 3
    for num_max in sorted(result.items(), key=lambda x: x[1], reverse=True):
        if counter == number_of_max_and_min_volatility:
            break
        print(' ' * 4, num_max[0].split('.')[0], '-', num_max[1], '%')
        counter += 1

    print('Минимальная волатильность:')
    counter = 0
    for num_min in sorted(result.items(), key=lambda x: x[1]):
        if num_min[1] != 0:
            if counter == number_of_max_and_min_volatility:
                break
            print(' ' * 4, num_min[0].split('.')[0], '-', num_min[1], '%')
            counter += 1

    print('Нулевая волатильность:')
    list_of_zero_volatility = []
    for i in sorted(result.items(), key=lambda x: x[0]):
        if i[1] == 0:
            list_of_zero_volatility.append(i[0].split('.')[0])
    print(' ' * 4, ', '.join(list_of_zero_volatility))


if __name__ == '__main__':
    main()
