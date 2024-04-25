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


class RegistrationLog:

    def __init__(self, file_line):
        self.line = file_line
        self.line_split = None

    def check_line(self):
        self.line_split = self.line.split()
        if len(self.line.split()) == 3:
            print(f'В строке есть три поля: {self.line}')
            self._check_name()
        else:
            with open('registrations_bad.log', 'a', encoding='utf8') as bad:
                bad.write(self.line + '\n')
            raise ValueError(f'НЕ присутствуют все три поля: {self.line}')

    def _check_name(self):
        if self.line_split[0].isalpha():
            print(f'Поле имени содержит только буквы: {self.line_split[0]}')
            self._check_email()
        else:
            with open('registrations_bad.log', 'a', encoding='utf8') as bad:
                bad.write(self.line + '\n')
            raise NotNameError(f'Поле имени содержит НЕ только буквы: {self.line_split[0]}')

    def _check_email(self):
        if '@' in self.line_split[1] and '.' in self.line_split[1]:
            print(f'Поле емейл содержит "@" и ".": {self.line_split[1]}')
            self._check_age()
        else:
            with open('registrations_bad.log', 'a', encoding='utf8') as bad:
                bad.write(self.line + '\n')
            raise NotEmailError(f'Поле емейл не содержит одно из "@", ",": {self.line_split[1]}')

    def _check_age(self):
        if 10 <= int(self.line_split[2]) <= 99:
            print(f'Поле возраст является числом от 10 до 99: {self.line_split[2]}')
            with open('registrations_good.log', 'a', encoding='utf8') as good:
                good.write(self.line + '\n')
        else:
            with open('registrations_bad.log', 'a', encoding='utf8') as bad:
                bad.write(self.line + '\n')
            raise ValueError(f'Поле возраст НЕ является числом от 10 до 99: {self.line_split[2]}')


with open(file='registrations.txt', mode='r', encoding='utf8') as file:
    for line in file:
        reg_log = RegistrationLog(file_line=line[:-1])
        try:
            reg_log.check_line()
        except NotNameError as exc:
            print(f'Ошибка имени: {exc}')
        except NotEmailError as exc:
            print(f'Ошибка емайла: {exc}')
        except ValueError as exc:
            if 'три' in exc.args[0]:
                print(f'Ошибка длины строки: {exc} {exc.args}')
            else:
                print(f'Ошибка возраста: {exc}')
        print('==========================================')