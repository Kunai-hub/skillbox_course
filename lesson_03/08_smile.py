# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd

# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.


def smile(point):
    point_1_smile = sd.get_point(point.x - 35, point.y - 15)
    point_2_smile = sd.get_point(point.x - 15, point.y - 30)
    point_3_smile = sd.get_point(point.x + 15, point.y - 30)
    point_4_smile = sd.get_point(point.x + 35, point.y - 15)
    point_list = [point_1_smile, point_2_smile, point_3_smile, point_4_smile]
    point_1_eye = sd.get_point(point.x - 25, point.y + 15)
    point_2_eye = sd.get_point(point.x + 25, point.y + 15)
    sd.circle(point)
    sd.lines(point_list)
    sd.circle(point_1_eye, radius=5)
    sd.circle(point_2_eye, radius=5)


for _ in range(10):
    point = sd.random_point()
    smile(point=point)

sd.pause()
