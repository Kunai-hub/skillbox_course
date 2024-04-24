# -*- coding: utf-8 -*-
import random

# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.


class IamGodError(Exception):
    pass


class DrunkError(Exception):
    pass


class CarCrashError(Exception):
    pass


class GluttonyError(Exception):
    pass


class DepressionError(Exception):
    pass


class SuicideError(Exception):
    pass


ENLIGHTENMENT_CARMA_LEVEL = 777
carma_lvl = 0
exception = [IamGodError('Я сегодня БОГ'), DrunkError('Я сегодня НАПИЛСЯ'),
             CarCrashError('Я сегодня разбился на ТАЧКЕ'), GluttonyError('Я сегодня ОБОЖРАЛСЯ'),
             DepressionError('Я сегодня в ДЕПРЕССИИ'), SuicideError('Я сегодня СУИСАЙД')]


def one_day():
    res = random.randint(1, 7)
    if 13 == random.randint(1, 13):
        with open('out.txt', 'a', encoding='utf8') as file:
            try:
                raise Exception(random.choice(exception))
            except Exception as exc:
                print(f'Поймали исключение {exc}, {exc.args}')
                print(f'Поймали исключение {exc}, {exc.args}', file=file)
    return res


while carma_lvl < ENLIGHTENMENT_CARMA_LEVEL:
    carma_lvl += one_day()
    print(carma_lvl)


# https://goo.gl/JnsDqu
