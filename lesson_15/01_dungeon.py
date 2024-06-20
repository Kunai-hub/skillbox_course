# -*- coding: utf-8 -*-
import csv
import datetime
import json
from decimal import Decimal, getcontext
import re

# С помощью JSON файла rpg.json задана "карта" подземелья.
# Подземелье было выкопано монстрами и они всё ещё скрываются где-то в его глубинах,
# планируя набеги на близлежащие поселения.
# Само подземелье состоит из двух главных разветвлений и нескольких развилок,
# и лишь один из путей приведёт вас к главному Боссу
# и позволит предотвратить набеги и спасти мирных жителей.

# Напишите игру, в которой пользователь, с помощью консоли,
# сможет:
# 1) исследовать это подземелье:
#   -- передвижение должно осуществляться присваиванием переменной и только в одну сторону
#   -- перемещаясь из одной локации в другую, пользователь теряет время, указанное в конце названия каждой локации
# Так, перейдя в локацию Location_1_tm500 - вам необходимо будет списать со счёта 500 секунд.
# Тег, в названии локации, указывающий на время - 'tm'.
#
# 2) сражаться с монстрами:
#   -- сражение имитируется списанием со счета персонажа N-количества времени и получением N-количества опыта
#   -- опыт и время указаны в названиях монстров (после exp указано значение опыта и после tm указано время)
# Так, если в локации вы обнаружили монстра Mob_exp10_tm20 (или Boss_exp10_tm20)
# необходимо списать со счета 20 секунд и добавить 10 очков опыта.
# Теги указывающие на опыт и время - 'exp' и 'tm'.
# После того, как игра будет готова, сыграйте в неё и наберите 280 очков при положительном остатке времени.

# По мере продвижения вам так же необходимо вести журнал,
# в котором должна содержаться следующая информация:
# -- текущее положение
# -- текущее количество опыта
# -- текущая дата (отсчёт вести с первой локации с помощью datetime)
# После прохождения лабиринта, набора 280 очков опыта и проверки на остаток времени (remaining_time > 0),
# журнал необходимо записать в csv файл (назвать dungeon.csv, названия столбцов взять из field_names).

# Пример лога игры:
# Вы находитесь в Location_0_tm0
# У вас 0 опыта и осталось 1234567890.0987654321 секунд
# Прошло уже 0:00:00
# Внутри вы видите:
# -- Монстра Mob_exp10_tm0
# -- Вход в локацию: Location_1_tm10400000
# -- Вход в локацию: Location_2_tm333000000
# Выберите действие:
# 1.Атаковать монстра
# 2.Перейти в другую локацию
# 3.Выход

remaining_time = '1234567890.0987654321'
# если изначально не писать число в виде строки - теряется точность!
field_names = ['current_location', 'current_experience', 'current_date']


class RpgGame:

    def __init__(self):
        self.remaining_time = remaining_time
        self.time = Decimal(0)
        self.exp = 0
        self.mobs = []
        self.travel_location = []
        self.location_object = []
        self.location_name = []
        self.exp_re = r'exp(\d+)'
        self.tm_re = r'tm(\d.+)'
        self.float_count = getcontext().prec = 20
        self.exp_to_win = 280
        self.writter = None
        self.file = None
        self.field_names = field_names
        self.result_game = []

    def create_file(self):
        with open('dungeon.csv', mode='w', newline='') as out_file:
            self.writter = csv.writer(out_file)
            self.writter.writerow(self.field_names)

    def save_result(self):
        with open('dungeon.csv', mode='a', newline='') as out_result:
            self.writter = csv.writer(out_result)
            self.result_game.extend([self.location_name[0], self.exp, datetime.datetime.now()])
            self.writter.writerow(self.result_game)

    def open_maps(self):
        with open('rpg.json', mode='r') as rpg:
            self.file = json.load(rpg)
            self.location_object.extend(self.file['Location_0_tm0'])
            self.location_name.extend(self.file.keys())

    def create_location(self):
        for index, new_obj in enumerate(self.location_object):
            if isinstance(new_obj, str):
                self.mobs.append((index, new_obj))
            elif isinstance(new_obj, dict):
                names = list(new_obj.keys())[0]
                self.travel_location.append((index, names))

    def printing(self):
        print(f'Вы находитесь в локации {self.location_name[0]}\n'
              f'У вас {self.exp} опыта и осталось {datetime.timedelta(seconds=float(self.remaining_time))}\n'
              f'Прошло времени: {datetime.timedelta(seconds=float(self.time))}\n'
              f'Внутри вы видите: ')
        for mob in self.mobs:
            print(f'Монстра -- {mob[1]}')
        for lok in self.travel_location:
            print(f'Вход в локацию -- {lok[1]}')
        print('Выберите действие:\n'
              '1. Атаковать монстра\n'
              '2. Перейти в другую локацию\n'
              '3. Сдаться и выйти из игры')

    def user_input(self):
        while True:
            self.printing()
            choice = input('Чем займетесь?: ')
            if choice == '1':
                if not self.mobs:
                    print('Нет монстров для атаки!')
                    continue
                else:
                    for count, monster in enumerate(self.mobs):
                        print(f'{count + 1}: {monster[1]}')
                    select = input('Выберите монстра для атаки: ')
                    if select.isalpha():
                        print('Вводить необходимо цифры!')
                        continue
                    elif int(select) > len(self.mobs):
                        print('Не правильно введено число!')
                        continue
                    else:
                        select_mobs = self.mobs[int(select) - 1]
                        count_exp = re.search(self.exp_re, select_mobs[1])
                        self.exp += Decimal(count_exp[1])
                        count_time = re.search(self.tm_re, select_mobs[1])
                        self.time += Decimal(count_time[1])
            elif choice == '2':
                if not self.travel_location:
                    if self.mobs:
                        continue
                    else:
                        return print('Мы попали в тупик... Прийдется начать игру  начала...')
                else:
                    for count, locations in enumerate(self.travel_location):
                        print(f'{count + 1}: {locations[1]}')
                    choice_location = input('В какую локацию выдвигаемся?: ')
                    if choice_location.isalpha():
                        print('Вводить необходимо цифры!')
                        continue
                    elif int(choice_location) > len(self.travel_location):
                        print('Не правильно введено число!')
                        continue
                    elif 'Hatch' in self.travel_location[0][1]:
                        if self.exp < self.exp_to_win:
                            return print('Слишком мало опыта для перехода в локацию...')
                        else:
                            return print('You are Winner!!!')
                    else:
                        your_choice = self.travel_location[int(choice_location) - 1]
                        count_lok_tm = re.search(self.tm_re, your_choice[1])
                        self.time += Decimal(count_lok_tm[1])
                        self.location_object = self.location_object[your_choice[0]][your_choice[1]]
                        self.mobs.clear()
                        self.travel_location.clear()
                        self.create_location()
                        self.location_name.append(your_choice[1])
                        self.location_name.pop(0)
                        self.save_result()
                        self.result_game.clear()
            elif choice == '3':
                return print('Беги, глупец!')
            elif not choice.isdigit() or not choice.isalpha():
                print('Что ты вводишь? Цифры, пожалуйста!')

    def run(self):
        self.create_file()
        self.open_maps()
        self.create_location()
        while True:
            self.user_input()
            game_of_white_thrones = input('Если ты хочешь продолжить, введи - "yes",\n'
                                          'если ты хочешь выйти, введи - "q": ')
            if game_of_white_thrones == 'yes':
                continue
            elif game_of_white_thrones == 'q':
                print('Game over')
                break

if __name__ == '__main__':
    game = RpgGame()
    game.run()

# Учитывая время и опыт, не забывайте о точности вычислений!

