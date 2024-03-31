# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

print('Возможные фигуры:\n0 : Треугольник\n1 : Квадрат\n2 : Пятиугольник\n3 : Шестиугольник')


_ = True

while _:
    user_input = int(input('Введите желаемую фигуру: '))
    if user_input == 0:
        n = 3
        _ = False
    elif user_input == 1:
        n = 4
        _ = False
    elif user_input == 2:
        n = 5
        _ = False
    elif user_input == 3:
        n = 6
        _ = False
    else:
        print('Вы ввели некорректный номер фигуры!\nПопробуйте ещё раз!')


def draw_vector(point, angle, n):
    for _ in range(n):
        v = sd.get_vector(start_point=point, angle=angle, length=100, width=5)
        v.draw()
        point = v.end_point
        if n == 3:
            angle += 120
        elif n == 4:
            angle += 90
        elif n == 5:
            angle += 72
        else:
            angle += 60


def figure(start, angle):
    draw_vector(point=start, angle=angle, n=n)


start_0 = sd.get_point(300, 300)
figure(start=start_0, angle=45)


sd.pause()
