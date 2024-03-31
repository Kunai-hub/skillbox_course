# -*- coding: utf-8 -*-
import simple_draw as sd

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

print('Возможные цвета:\n0 : RED\n1 : ORAGNE\n2 : YELLOW\n3 : GREEN\n4 : CYAN\n5 : BLUE\n6 : PURPLE')


_ = True


while _:
    user_input = int(input('Введите желаемый цвет: '))
    if user_input == 0:
        color = sd.COLOR_RED
        _ = False
    elif user_input == 1:
        color = sd.COLOR_ORANGE
        _ = False
    elif user_input == 2:
        color = sd.COLOR_YELLOW
        _ = False
    elif user_input == 3:
        color = sd.COLOR_GREEN
        _ = False
    elif user_input == 4:
        color = sd.COLOR_CYAN
        _ = False
    elif user_input == 5:
        color = sd.COLOR_BLUE
        _ = False
    elif user_input == 6:
        color = sd.COLOR_PURPLE
        _ = False
    else:
        print('Вы ввели некорректный номер цвета!\nПопробуйте ещё раз!')


def draw_vector(point, angle, n):
    for _ in range(n):
        v = sd.get_vector(start_point=point, angle=angle, length=100, width=5)
        v.draw(color=color)
        point = v.end_point
        if n == 3:
            angle += 120
        elif n == 4:
            angle += 90
        elif n == 5:
            angle += 72
        else:
            angle += 60


def triangle_two(start, angle):
    draw_vector(point=start, angle=angle, n=3)


start_0 = sd.get_point(100, 100)
triangle_two(start=start_0, angle=30)


def square_two(start, angle):
    draw_vector(point=start, angle=angle, n=4)


start_1 = sd.get_point(400, 100)
square_two(start=start_1, angle=15)


def polygon_two(start, angle):
    draw_vector(point=start, angle=angle, n=5)


start_2 = sd.get_point(100, 400)
polygon_two(start=start_2, angle=30)


def hexagon_two(start, angle):
    draw_vector(point=start, angle=angle, n=6)


start_3 = sd.get_point(400, 400)
hexagon_two(start=start_3, angle=15)

sd.pause()
