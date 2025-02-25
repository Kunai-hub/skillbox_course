# -*- coding: utf-8 -*-

from random import randint

######################################################## Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умрает от депресии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.


# class House:
#
#     def __init__(self):
#         self.money = 100
#         self.food = 50
#         self.mud = 0
#
#     def __str__(self):
#         return (f'В доме на данный момент: денег {self.money} в тумбочке, еды {self.food} в холодильнике и {self.mud} '
#                 f'грязи')
#
#
# class People:
#     total_food = 0
#     total_money = 0
#     total_fur_coat = 0
#
#     def __init__(self, name, house):
#         self.name = name
#         self.fullness = 30
#         self.happiness = 100
#         self.house = house
#
#     def __str__(self):
#         return f'Меня зовут {self.name}, степень сытости {self.fullness}, степень счастья {self.happiness}!'
#
#     def eat(self):
#         amount_of_food = randint(10, 30)
#         if self.house.food > amount_of_food:
#             self.fullness += amount_of_food
#             self.house.food -= amount_of_food
#             People.total_food += amount_of_food
#             print(f'{self.name} поел(а)')
#         else:
#             print('В доме нет еды')
#
#
# class Husband(People):
#
#     def __init__(self, name, house):
#         super().__init__(name=name, house=house)
#
#     def __str__(self):
#         return super().__str__()
#
#     def work(self):
#         print(f'{self.name} пошёл на работу')
#         self.fullness -= 10
#         self.house.money += 150
#         People.total_money += 150
#
#     def gaming(self):
#         print(f'{self.name} играет в WOT!')
#         self.fullness -= 10
#         self.happiness += 20
#
#     def act(self):
#         if self.fullness <= 0:
#             print(f'{self.name} умер...')
#             return
#         if self.happiness <= 10:
#             print(f'{self.name} умер...')
#             return
#         if self.house.mud >= 90:
#             self.happiness -= 10
#         self.house.mud += 10
#         dice = randint(1, 4)
#         if self.fullness <= 30:
#             self.eat()
#         elif self.house.money <= 50:
#             self.work()
#         elif dice == 1:
#             self.work()
#         elif dice == 2:
#             self.gaming()
#         else:
#             self.eat()
#
#
# class Wife(People):
#
#     def __init__(self, name, house):
#         super().__init__(name=name, house=house)
#
#     def __str__(self):
#         return super().__str__()
#
#     def shopping(self):
#         amount_of_food = randint(40, 60)
#         if self.house.money >= amount_of_food:
#             print(f'{self.name} пошла в магазин за продуктами')
#             self.fullness -= 10
#             self.house.food += amount_of_food
#             self.house.money -= amount_of_food
#         else:
#             print('Денег нет на покупку продуктов')
#
#     def buy_fur_coat(self):
#         if self.house.money >= 350:
#             print(f'{self.name} пошла в магазин за шубой!')
#             self.fullness -= 10
#             self.happiness += 60
#             self.house.money -= 350
#             People.total_fur_coat += 1
#         else:
#             print('Денег нет на покупку шубы')
#
#     def clean_house(self):
#         if self.house.mud == 0:
#             print('Уборка не требуется')
#         elif self.house.mud < 100:
#             print(f'{self.name} убирает в доме')
#             self.house.mud -= self.house.mud
#             self.fullness -= 10
#         else:
#             print(f'{self.name} убирает в доме')
#             self.house.mud -= 100
#             self.fullness -= 10
#
#     def act(self):
#         if self.fullness <= 0:
#             print(f'{self.name} умер...')
#             return
#         if self.happiness <= 10:
#             print(f'{self.name} умер...')
#             return
#         if self.house.mud >= 90:
#             self.happiness -= 10
#         dice = randint(1, 4)
#         if self.fullness <= 30:
#             self.eat()
#         elif self.house.food <= 50:
#             self.shopping()
#         elif self.house.mud > 90:
#             self.clean_house()
#         elif dice == 1:
#             self.shopping()
#         elif dice == 2:
#             self.eat()
#         elif self.house.money > 350:
#             self.buy_fur_coat()
#         else:
#             self.eat()
#
#
# home = House()
# serge = Husband(name='Сережа', house=home)
# masha = Wife(name='Маша', house=home)
#
# for day in range(1, 366):
#     print('================== День {} =================='.format(day))
#     serge.act()
#     masha.act()
#     print(serge)
#     print(masha)
#     print(home)
#
# print(f'Еды съедено: {People.total_food}')
# print(f'Денег заработано: {People.total_money}')
# print(f'Шуб куплено: {People.total_fur_coat}')


######################################################## Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов

# class House:
#
#     def __init__(self):
#         self.money = 100
#         self.food = 50
#         self.mud = 0
#         self.cat_food = 30
#
#     def __str__(self):
#         return (f'В доме на данный момент: денег {self.money} в тумбочке, еды в холодильнике {self.food}, грязи '
#                 f'{self.mud}, корма для кота {self.cat_food}')
#
#
# class People:
#     total_food = 0
#     total_money = 0
#     total_fur_coat = 0
#
#     def __init__(self, name, house):
#         self.name = name
#         self.fullness = 30
#         self.happiness = 100
#         self.house = house
#
#     def __str__(self):
#         return f'Меня зовут {self.name}, степень сытости {self.fullness}, степень счастья {self.happiness}!'
#
#     def eat(self):
#         amount_of_food = randint(10, 30)
#         if self.house.food > amount_of_food:
#             self.fullness += amount_of_food
#             self.house.food -= amount_of_food
#             People.total_food += amount_of_food
#             print(f'{self.name} поел(а)')
#         else:
#             print('В доме нет еды')
#             if self.fullness >= 10:
#                 self.fullness -= 10
#             else:
#                 self.fullness -= self.fullness
#
#     def pet_the_cat(self):
#         print(f'{self.name} гладит кота')
#         self.happiness += 5
#         self.fullness -= 10
#
#
# class Husband(People):
#
#     def __init__(self, name, house):
#         super().__init__(name=name, house=house)
#
#     def __str__(self):
#         return super().__str__()
#
#     def work(self):
#         print(f'{self.name} пошёл на работу')
#         self.fullness -= 10
#         self.house.money += 150
#         People.total_money += 150
#
#     def gaming(self):
#         print(f'{self.name} играет в WOT!')
#         self.fullness -= 10
#         self.happiness += 20
#
#     def act(self):
#         if self.fullness <= 0:
#             print(f'{self.name} умер...')
#             return
#         if self.happiness <= 10:
#             print(f'{self.name} умер...')
#             return
#         if self.house.mud >= 90:
#             self.happiness -= 10
#         self.house.mud += 10
#         dice = randint(1, 4)
#         if self.fullness < 30:
#             self.eat()
#         elif self.house.money < 100:
#             self.work()
#         elif self.happiness <= 20:
#             self.gaming()
#         elif dice == 1:
#             self.work()
#         elif dice == 2:
#             self.gaming()
#         else:
#             self.pet_the_cat()
#
#
# class Wife(People):
#
#     def __init__(self, name, house):
#         super().__init__(name=name, house=house)
#
#     def __str__(self):
#         return super().__str__()
#
#     def shopping(self):
#         amount_of_food = randint(80, 120)
#         if self.house.money >= amount_of_food:
#             print(f'{self.name} пошла в магазин за продуктами')
#             self.fullness -= 10
#             self.house.food += amount_of_food
#             self.house.money -= amount_of_food
#         else:
#             print('Денег нет на покупку продуктов')
#
#     def cat_shopping(self):
#         if self.house.money >= 50:
#             print(f'{self.name} пошла в магазин за кормом коту')
#             self.fullness -= 10
#             self.house.cat_food += 50
#             self.house.money -= 50
#         else:
#             print('Денег нет на покупку продуктов')
#
#     def buy_fur_coat(self):
#         if self.house.money > 350:
#             print(f'{self.name} пошла в магазин за шубой!')
#             self.fullness -= 10
#             self.happiness += 100
#             self.house.money -= 350
#             People.total_fur_coat += 1
#         else:
#             print('Денег нет на покупку шубы')
#
#     def clean_house(self):
#         if self.house.mud == 0:
#             print('Уборка не требуется')
#         elif self.house.mud < 100:
#             print(f'{self.name} убирает в доме')
#             self.house.mud -= self.house.mud
#             self.fullness -= 10
#         else:
#             print(f'{self.name} убирает в доме')
#             self.house.mud -= 100
#             self.fullness -= 10
#
#     def act(self):
#         if self.fullness <= 0:
#             print(f'{self.name} умер...')
#             return
#         if self.happiness <= 10:
#             print(f'{self.name} умер...')
#             return
#         if self.house.mud >= 90:
#             self.happiness -= 10
#         dice = randint(1, 4)
#         if self.fullness < 30:
#             self.eat()
#         elif self.house.food < 50:
#             self.shopping()
#         elif self.house.cat_food < 20:
#             self.cat_shopping()
#         elif self.house.mud > 90:
#             self.clean_house()
#         elif self.house.money > 350:
#             self.buy_fur_coat()
#         elif self.happiness <= 20:
#             self.pet_the_cat()
#         elif dice == 1:
#             self.shopping()
#         elif dice == 2:
#             self.cat_shopping()
#         else:
#             self.pet_the_cat()
#
#
# class Cat:
#     total_cat_food = 0
#
#     def __init__(self, name, house):
#         self.name = name
#         self.cat_fullness = 30
#         self.house = house
#
#     def __str__(self):
#         return f'Кот по кличке {self.name}, степень сытности {self.cat_fullness}'
#
#     def eat(self):
#         if self.house.cat_food >= 10:
#             print(f'Кот {self.name} поел')
#             self.cat_fullness += 20
#             self.house.cat_food -= 10
#             Cat.total_cat_food += 10
#         else:
#             print('Нет корма для кота')
#
#     def sleep(self):
#         print(f'Кот {self.name} спит')
#         self.cat_fullness -= 10
#
#     def peel_off_wallpaper(self):
#         print(f'Кот {self.name} дерет обои!')
#         self.cat_fullness -= 10
#         self.house.mud += 5
#
#     def act(self):
#         if self.cat_fullness <= 0:
#             print(f'Кот {self.name} умер...')
#             return
#         dice = randint(1, 4)
#         if self.cat_fullness <= 20:
#             self.eat()
#         elif dice == 1:
#             self.sleep()
#         else:
#             self.peel_off_wallpaper()
#
#
# home = House()
# serge = Husband(name='Сережа', house=home)
# masha = Wife(name='Маша', house=home)
# murzik = Cat(name='Мурзик', house=home)
#
# for day in range(1, 366):
#     print('================== День {} =================='.format(day))
#     serge.act()
#     masha.act()
#     murzik.act()
#     print(serge)
#     print(masha)
#     print(murzik)
#     print(home)
# print('\n')
# print(f'Еды съедено: {People.total_food}')
# print(f'Денег заработано: {People.total_money}')
# print(f'Шуб куплено: {People.total_fur_coat}')
# print(f'Корма для кота съедено: {Cat.total_cat_food}')


######################################################## Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда == 100 ;)

class House:

    def __init__(self):
        self.money = 100
        self.food = 50
        self.mud = 0
        self.cat_food = 30

    def __str__(self):
        return (f'В доме на данный момент: денег {self.money} в тумбочке, еды в холодильнике {self.food}, грязи '
                f'{self.mud}, корма для кота {self.cat_food}')


class People:
    total_food = 0
    total_money = 0
    total_fur_coat = 0

    def __init__(self, name, house):
        self.name = name
        self.fullness = 30
        self.happiness = 100
        self.house = house

    def __str__(self):
        return f'Меня зовут {self.name}, степень сытости {self.fullness}, степень счастья {self.happiness}!'

    def eat(self):
        amount_of_food = randint(10, 20)
        if self.house.food > amount_of_food:
            self.fullness += amount_of_food
            self.house.food -= amount_of_food
            People.total_food += amount_of_food
            print(f'{self.name} поел(а)')
        else:
            print('В доме нет еды')
            if self.fullness >= 10:
                self.fullness -= 10
            else:
                self.fullness -= self.fullness

    def pet_the_cat(self):
        print(f'{self.name} гладит кота')
        self.happiness += 5
        self.fullness -= 10


class Husband(People):

    def __init__(self, name, house):
        super().__init__(name=name, house=house)

    def __str__(self):
        return super().__str__()

    def work(self):
        print(f'{self.name} пошёл на работу')
        self.fullness -= 10
        self.house.money += 200
        People.total_money += 200

    def gaming(self):
        print(f'{self.name} играет в WOT!')
        self.fullness -= 10
        self.happiness += 20

    def act(self):
        if self.fullness <= 0:
            print(f'{self.name} умер...')
            return
        if self.happiness <= 10:
            print(f'{self.name} умер...')
            return
        if self.house.mud >= 90:
            self.happiness -= 10
        self.house.mud += 10
        dice = randint(1, 4)
        if self.fullness < 30:
            self.eat()
        elif self.house.money < 80:
            self.work()
        elif self.happiness <= 20:
            self.gaming()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.gaming()
        else:
            self.pet_the_cat()


class Wife(People):

    def __init__(self, name, house):
        super().__init__(name=name, house=house)

    def __str__(self):
        return super().__str__()

    def shopping(self):
        amount_of_food = randint(50, 100)
        if self.house.money >= amount_of_food:
            print(f'{self.name} пошла в магазин за продуктами')
            self.fullness -= 10
            self.house.food += amount_of_food
            self.house.money -= amount_of_food
        else:
            print('Денег нет на покупку продуктов')

    def cat_shopping(self):
        if self.house.money >= 50:
            print(f'{self.name} пошла в магазин за кормом коту')
            self.fullness -= 10
            self.house.cat_food += 50
            self.house.money -= 50
        else:
            print('Денег нет на покупку продуктов')

    def buy_fur_coat(self):
        if self.house.money > 350:
            print(f'{self.name} пошла в магазин за шубой!')
            self.fullness -= 10
            self.happiness += 100
            self.house.money -= 350
            People.total_fur_coat += 1
        else:
            print('Денег нет на покупку шубы')

    def clean_house(self):
        if self.house.mud == 0:
            print('Уборка не требуется')
        elif self.house.mud < 100:
            print(f'{self.name} убирает в доме')
            self.house.mud -= self.house.mud
            self.fullness -= 10
        else:
            print(f'{self.name} убирает в доме')
            self.house.mud -= 100
            self.fullness -= 10

    def act(self):
        if self.fullness <= 0:
            print(f'{self.name} умер...')
            return
        if self.happiness <= 10:
            print(f'{self.name} умер...')
            return
        if self.house.mud >= 90:
            self.happiness -= 10
        dice = randint(1, 4)
        if self.fullness < 30:
            self.eat()
        elif self.house.food < 50:
            self.shopping()
        elif self.house.cat_food < 20:
            self.cat_shopping()
        elif self.house.mud > 90:
            self.clean_house()
        elif self.house.money > 350:
            self.buy_fur_coat()
        elif self.happiness <= 20:
            self.pet_the_cat()
        elif dice == 1:
            self.shopping()
        elif dice == 2:
            self.cat_shopping()
        else:
            self.pet_the_cat()


class Cat:
    total_cat_food = 0

    def __init__(self, name, house):
        self.name = name
        self.cat_fullness = 30
        self.house = house

    def __str__(self):
        return f'Кот по кличке {self.name}, степень сытности {self.cat_fullness}'

    def eat(self):
        if self.house.cat_food >= 10:
            print(f'Кот {self.name} поел')
            self.cat_fullness += 20
            self.house.cat_food -= 10
            Cat.total_cat_food += 10
        else:
            print('Нет корма для кота')
            self.cat_fullness -= 10

    def sleep(self):
        print(f'Кот {self.name} спит')
        self.cat_fullness -= 10

    def peel_off_wallpaper(self):
        print(f'Кот {self.name} дерет обои!')
        self.cat_fullness -= 10
        self.house.mud += 5

    def act(self):
        if self.cat_fullness <= 0:
            print(f'Кот {self.name} умер...')
            return
        dice = randint(1, 4)
        if self.cat_fullness <= 20:
            self.eat()
        elif dice == 1:
            self.sleep()
        else:
            self.peel_off_wallpaper()


class Child(People):

    def __init__(self, name, house):
        super().__init__(name=name, house=house)

    def __str__(self):
        return super().__str__()

    def eat(self):
        if self.house.food > 10:
            print(f'Ребенок {self.name} поел')
            self.house.food -= 10
            self.fullness += 10
            People.total_food += 10
        else:
            print('В доме нет еды')
            self.fullness -= 10

    def sleep(self):
        print(f'Ребенок {self.name} спит')
        self.fullness -= 10

    def act(self):
        if self.fullness <= 0:
            print(f'{self.name} умер...')
            return
        dice = randint(1, 3)
        if self.fullness < 20:
            self.eat()
        elif dice == 1:
            self.sleep()
        else:
            self.eat()


home = House()
serge = Husband(name='Сережа', house=home)
masha = Wife(name='Маша', house=home)
murzik = Cat(name='Мурзик', house=home)
kolya = Child(name='Коля', house=home)

for day in range(1, 366):
    print('================== День {} =================='.format(day))
    serge.act()
    masha.act()
    murzik.act()
    kolya.act()
    print(serge)
    print(masha)
    print(murzik)
    print(kolya)
    print(home)
print('\n')
print(f'Еды съедено: {People.total_food}')
print(f'Денег заработано: {People.total_money}')
print(f'Шуб куплено: {People.total_fur_coat}')
print(f'Корма для кота съедено: {Cat.total_cat_food}')


######################################################## Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.


# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')

