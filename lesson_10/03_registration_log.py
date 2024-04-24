# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.

class NotNameError(Exception):
    pass


class NotEmailError(Exception):
    pass


with open('registrations.txt', 'r', encoding='utf8') as file:
    for line in file:
        line_split = line.split()
        try:
            if len(line_split) == 3:
                print(f'Строка соответствует требованиям: {line_split}')
            else:
                raise ValueError(f'Строка не соответствует требованиям: {line_split}')

            if line_split[0].isalpha():
                print(f'Имя состоит только из букв: {line_split[0]}')
            else:
                # print(f'Имя содержит не только буквы: {line_split[0]}')
                raise NotNameError(f'Имя содержит не только буквы: {line_split[0]}')

            if '@' and '.' in line_split[1]:
                print(f'Емейл удовлетворяет требованиям: {line_split[1]}')
            else:
                # print(f'Емейл не содержит один из символов: "@", ".": {line_split[1]}')
                raise NotEmailError(f'Емейл не содержит один из символов: "@", ".": {line_split[1]}')

            if 10 <= int(line_split[2]) <= 99:
                print(f'Возраст в пределах 10-99: {line_split[2]}')
            else:
                raise ValueError(f'Возраст не в пределах 10-99: {line_split[2]}')

        except NotNameError as exc:
            print(f'Ошибка имени: {exc}')
        except NotEmailError as exc:
            print(f'Ошибка емайла: {exc}')
        except ValueError as exc:
            print(f'Ошибка длины строки: {exc}')
        except ValueError(f'Возраст не в пределах 10-99: {line_split[2]}') as exc:
            print(f'Ошибка возраста: {exc}')