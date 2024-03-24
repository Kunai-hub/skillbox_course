# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
# point = sd.get_point(500, 500)
# radius = 50
# for _ in range(3):
#     sd.circle(point, radius)
#     radius += 5

# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
# def bubbles(point, step):
#     radius = 50
#     for _ in range(3):
#         sd.circle(point, radius)
#         radius += step

# Нарисовать 10 пузырьков в ряд
# for x in range(100, 1001, 100):
#     point = sd.get_point(x, 300)
#     bubbles(point, 10)

# Нарисовать три ряда по 10 пузырьков
# for y in range(100, 301, 100):
#     for x in range(200, 1101, 100):
#         point = sd.get_point(x, y)
#         bubbles(point, 15)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
# for _ in range(100):
#     point = sd.random_point()
#     bubbles(point, 5)
#

sd.pause()