# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 800)

# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# def draw_branches(start_point, angle, length):
#     v = sd.get_vector(start_point=start_point, angle=angle, length=length, width=2)
#     v.draw()
#     v1 = sd.get_vector(start_point=v.end_point, angle=angle + 30, length=length * 0.8, width=2)
#     v1.draw()
#     v2 = sd.get_vector(start_point=v.end_point, angle=angle - 30, length=length * 0.8, width=2)
#     v2.draw()


# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения

# def draw_branches(start_point, angle, length):
#     if length < 3:
#         return
#     v = sd.get_vector(start_point=start_point, angle=angle, length=length, width=2)
#     v.draw()
#     v1 = sd.get_vector(start_point=v.end_point, angle=angle + 30, length=length * 0.75, width=2)
#     v1.draw()
#     v2 = sd.get_vector(start_point=v.end_point, angle=angle - 30, length=length * 0.75, width=2)
#     v2.draw()
#     next_point_1 = v1.end_point
#     next_angle_1 = angle + 30
#     next_length = length * .75
#     draw_branches(start_point=next_point_1, angle=next_angle_1, length=next_length)
#     next_point_2 = v2.end_point
#     next_angle_2 = angle - 30
#     draw_branches(start_point=next_point_2, angle=next_angle_2, length=next_length)
#
#
# start_point = sd.get_point(600, 30)
# draw_branches(start_point=start_point, angle=90, length=100)

# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()

def draw_branches(start_point, angle, length):
    if length < 5:
        return
    v = sd.get_vector(start_point=start_point, angle=angle, length=length, width=2)
    v.draw()
    v1 = sd.get_vector(start_point=v.end_point, angle=angle + 30, length=length * 0.75, width=2)
    v1.draw()
    v2 = sd.get_vector(start_point=v.end_point, angle=angle - 30, length=length * 0.75, width=2)
    v2.draw()
    next_point_1 = v1.end_point
    next_angle_1 = angle + sd.random_number(15, 45)
    next_length = length * sd.random_number(6, 9) / 10
    draw_branches(start_point=next_point_1, angle=next_angle_1, length=next_length)
    next_point_2 = v2.end_point
    next_angle_2 = angle - sd.random_number(15, 45)
    draw_branches(start_point=next_point_2, angle=next_angle_2, length=next_length)


start_point = sd.get_point(600, 30)
draw_branches(start_point=start_point, angle=90, length=100)


sd.pause()


