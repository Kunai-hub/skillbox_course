# -*- coding: utf-8 -*-
import re
import json
from datetime import datetime
from decimal import Decimal, ROUND_HALF_EVEN
import csv
from collections import defaultdict

# Задача: подсчитать выплату суточных агенту 007.
#
# Дано: файл с зашифрованными посланиями, в которых содержатся информация о датах, городах и потраченных суммах:
# external_data/Bond.json
#
# Шифр следующий:
# в каждом послании среди случайных символов содержатся:
# - дата в формате "jbdDDMMYY"
# - город в формате "jbcCITYNAMEjbc"
# - сумма потраченных за день денег в местной валюте в формате "jbeFLOATjbe"
#
# Требуется: составить два файла с тратами по дням, и по месяцам для бухгалтерии МИ-6.


re_date = r'jbd(\d{6})'
re_city = r'jbc(\w+)jbc'
re_money = r'jbe(\d+\.\d+)jbe'

with open(r'C:\Users\neni2\PycharmProjects\Kirill\skillbox_course\lesson_15\python_snippets\external_data\Bond.json',
          mode='r') as file_data:
    data = json.load(file_data)

exchanges = {
    'берлин': Decimal(0.84),
    'лондон': Decimal(1.0),
    'токио': Decimal(0.005),
    'москва': Decimal(0.0091)
}


def str_date_to_datetime(str_date):
    return datetime.strptime(str_date, '%d%m%y')


def str_money_to_decimal(str_money, city):
    return Decimal(str_money) * exchanges[city]


result = []
for number, message in data.items():
    str_date = re.search(re_date, message)[1]
    city = re.search(re_city, message)[1]
    str_money = re.search(re_money, message)[1]
    result.append({
        'date': str_date_to_datetime(str_date),
        'city': city,
        'expenses': str_money_to_decimal(str_money, city)
    })

result = sorted(result, key=lambda x: x['date'])

result_formatted = [
    {
        'date': res['date'].strftime('%d-%m-%Y'),
        'city': res['city'],
        'expenses': str(res['expenses'].quantize(Decimal('1.00'), ROUND_HALF_EVEN))
    }
    for res in result
]

with open(r'C:\Users\neni2\PycharmProjects\Kirill\skillbox_course\lesson_15\My_Detail.csv',
          mode='w', encoding='utf8', newline='') as file_out_detail:
    writter = csv.DictWriter(file_out_detail, fieldnames=[
        'date', 'city', 'expenses'
    ])
    writter.writeheader()
    writter.writerows(result_formatted)

#======================================================================================================================

result_aggregated_temp = defaultdict(lambda: {'cities': set(), 'expenses_sum': Decimal(0),
                                              'month': '', 'date_for_sort': ''})
for res in result:
    month_datetime = datetime(year=res['date'].year, month=res['date'].month, day=1)
    month = month_datetime.strftime('%m-%Y')
    result_aggregated_temp[month]['cities'].add(res['city'])
    result_aggregated_temp[month]['expenses_sum'] += res['expenses']
    result_aggregated_temp[month]['month'] = month
    result_aggregated_temp[month]['date_for_sort'] = month_datetime

result_aggregated = sorted(result_aggregated_temp.values(), key=lambda x: x['date_for_sort'])

result_aggregated_formatted = [
    {
        'month': month,
        'cities': ', '.join(res['cities']),
        'expenses_sum': str(res['expenses_sum'].quantize(Decimal('1.00'), ROUND_HALF_EVEN))
    }
    for res in result_aggregated
]

with open(r'C:\Users\neni2\PycharmProjects\Kirill\skillbox_course\lesson_15\My_Detail_Aggregate.csv',
          mode='w', encoding='utf8', newline='') as file_out_detail_aggregate:
    writter_aggregate = csv.DictWriter(file_out_detail_aggregate, fieldnames=['month', 'cities', 'expenses_sum'])
    writter_aggregate.writeheader()
    writter_aggregate.writerows(result_aggregated_formatted)
