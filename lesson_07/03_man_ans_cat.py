# -*- coding: utf-8 -*-

from random import randint

# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.

class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None
        self.cat = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness)

    def eat(self):
        if self.house.food >= 10:
            print('{} поел'.format(self.name))
            self.fullness += 10
            self.house.food -= 10
        else:
            print('У {} нет еды'.format(self.name))

    def work(self):
        print('{} сходил на работу'.format(self.name))
        self.house.money += 150
        self.fullness -= 10

    def watch_MTV(self):
        print('{} смотрел MTV целый день'.format(self.name))
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            print('{} сходил в магазин за едой'.format(self.name))
            self.house.money -= 50
            self.house.food += 50
        else:
            print('У {} деньги кончились!'.format(self.name))

    def shopping_cat(self):
        if self.house.money >= 50:
            print('{} сходил в магазин за кормом коту'.format(self.name))
            self.house.money -= 50
            self.house.bowl_cat += 50
        else:
            print('У {} деньги кончились!'.format(self.name))

    def cleaning(self):
        print('{} убрался'.format(self.name))
        self.fullness -= 20
        self.house.mud -= 100

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        print('{} Вьехал в дом'.format(self.name))

    def pick_up_cat(self, cat):
        self.cat = cat
        self.cat.house = self.house
        print('{} Подобрал кота'.format(self.name))

    def act(self):
        if self.fullness <= 0:
            print('{} умер...'.format(self.name))
            return
        dice = randint(1, 6)
        if self.fullness <= 20:
            self.eat()
        elif self.house.food <= 10:
            self.shopping()
        elif self.house.money < 50:
            self.work()
        elif self.house.bowl_cat <= 10:
            self.shopping_cat()
        elif self.house.mud >= 120:
            self.cleaning()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.watch_MTV()


class House:

    def __init__(self):
        self.food = 50
        self.money = 0
        self.bowl_cat = 0
        self.mud = 0

    def __str__(self):
        return 'В доме еды осталось {}, денег осталось {}\nЕды для кота {}, грязи {}'.format(
            self.food, self.money, self.bowl_cat, self.mud)


class Cat:

    def __init__(self, name):
        self.name = name
        self.fullness_cat = 50
        self.house = None

    def __str__(self):
        return 'Кот {}, сытость {}'.format(self.name, self.fullness_cat)

    def sleep(self):
        print('Кот {} поспал'.format(self.name))
        self.fullness_cat -= 10

    def eat(self):
        if self.house.bowl_cat >= 10:
            print('Кот {} поел'.format(self.name))
            self.fullness_cat += 20
            self.house.bowl_cat -= 10
        else:
            print('Нет корма для кота')

    def peel_off_wallpaper(self):
        print('Кот {} дерет обои'.format(self.name))
        self.fullness_cat -= 10
        self.house.mud += 5

    def act(self):
        if self.fullness_cat <= 0:
            print('Кот {} умер...'.format(self.name))
            return
        dice = randint(1, 3)
        if self.fullness_cat <= 20:
            self.eat()
        elif dice == 1:
            self.sleep()
        else:
            self.peel_off_wallpaper()


#
my_sweet_home = House()

# --- Для одного человека и одного питомца ---

# citisen = Man(name='Кенни')
# new_cat = Cat(name='Барсик')
# citisen.go_to_the_house(house=my_sweet_home)
# citisen.pick_up_cat(cat=new_cat)

# for day in range(1, 366):
#     print('================ день {} =================='.format(day))
#     citisen.act()
#     new_cat.act()
#     print('--- в конце дня ---')
#     print(citisen)
#     print(new_cat)
#     print(my_sweet_home)

# --- Для нескольких людей и нескольких питомцев ---

citizens = [
    Man(name='Бивис'),
    Man(name='Батхед'),
    Man(name='Кенни'),
]

cats = [
    Cat(name='Тоха'),
    Cat(name='Картоха'),
    Cat(name='Дошик')
]

for citisen in citizens:
    citisen.go_to_the_house(house=my_sweet_home)

for cat in cats:
    citisen.pick_up_cat(cat=cat)

for day in range(1, 366):
    print('================ день {} =================='.format(day))
    for citisen in citizens:
        citisen.act()
    for cat in cats:
        cat.act()
    print('--- в конце дня ---')
    for citisen in citizens:
        print(citisen)
    for cat in cats:
        print(cat)
    print(my_sweet_home)

# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
