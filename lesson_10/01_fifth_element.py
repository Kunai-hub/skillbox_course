# -*- coding: utf-8 -*-

# Умножить константу BRUCE_WILLIS на пятый элемент строки, введенный пользователем

BRUCE_WILLIS = 42

try:
    input_data = input('Если хочешь что-нибудь сделать, сделай это сам: ')
    leeloo = int(input_data[4])
    result = BRUCE_WILLIS * leeloo
    print(f"- Leeloo Dallas! Multi-pass № {result}!")
except ValueError as exc:
    print(f'Невозможно преобразовать к числу {exc}, параметры {exc.args}')
except IndexError as exc:
    print(f'Недостаточно символов/выход за границы списка {exc}, параметры {exc.args}')
except Exception as exc:
    print(f'Неизвестная ошибка - {exc}, параметры {exc.args}')

# Ообернуть код и обработать исключительные ситуации для произвольных входных параметров
# - ValueError - невозможно преобразовать к числу
# - IndexError - выход за границы списка
# - остальные исключения
# для каждого типа исключений написать на консоль соотв. сообщение




