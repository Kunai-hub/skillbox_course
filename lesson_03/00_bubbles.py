# -*- coding: utf-8 -*-
import time

import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
point = sd.get_point(500, 500)
radius = 50
for _ in range(3):
    sd.circle(point, radius)
    radius += 5

time.sleep(1)
sd.clear_screen()


# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
def bubbles(point, radius = 50, step = 5, color=sd.COLOR_CYAN):
    for _ in range(3):
        sd.circle(point, radius, color)
        radius += step


# Нарисовать 10 пузырьков в ряд
for x in range(100, 1001, 100):
    point = sd.get_point(x, 300)
    bubbles(point=point, step=10)

time.sleep(1)
sd.clear_screen()

# Нарисовать три ряда по 10 пузырьков
for y in range(100, 301, 100):
    for x in range(100, 1001, 100):
        point = sd.get_point(x, y)
        bubbles(point=point, step=15)

time.sleep(1)
sd.clear_screen()

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
for _ in range(100):
    point = sd.random_point()
    color = sd.random_color()
    time.sleep(0.1)
    bubbles(point=point, step=5, color=color)

time.sleep(1)
sd.clear_screen()

sd.pause()