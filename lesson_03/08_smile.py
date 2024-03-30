# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd

# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

# point_center = sd.get_point(300, 300)
# point_1_smile = sd.get_point(265, 285)
# point_2_smile = sd.get_point(285, 270)
# point_3_smile = sd.get_point(315, 270)
# point_4_smile = sd.get_point(335, 285)
# point_list = [point_1_smile, point_2_smile, point_3_smile, point_4_smile]
# point_1_eye = sd.get_point(275, 315)
# point_2_eye = sd.get_point(325, 315)
# sd.circle(point_center)
# sd.lines(point_list)
# sd.circle(point_1_eye, radius=5)
# sd.circle(point_2_eye, radius=5)

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
