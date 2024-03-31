# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 800)

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 20

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()

x1 = 100
y1 = 750

x2 = 120
y2 = 650

x3 = 140
y3 = 700

while True:
    sd.clear_screen()
    # point = sd.get_point(x1, y1)
    # sd.snowflake(center=point, length=30, color=sd.COLOR_WHITE)
    # y1 -= 30
    # x1 += 15
    # if y1 < -10:
    #     break
    #
    # point = sd.get_point(x2, y2)
    # sd.snowflake(center=point, length=15, color=sd.COLOR_WHITE)
    # y2 -= 30
    # x2 += 30
    # if y2 < -10:
    #     break
    #
    # point = sd.get_point(x3, y3)
    # sd.snowflake(center=point, length=23, color=sd.COLOR_WHITE)
    # y3 -= 30
    # x3 += 10
    # if y3 < -10:
    #     break
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg


