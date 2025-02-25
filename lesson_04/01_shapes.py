# -*- coding: utf-8 -*-

import simple_draw as sd

# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg


def triangle(point, angle, length):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=2)
    v1.draw()
    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 120, length=length, width=2)
    v2.draw()
    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 240, length=length, width=2)
    v3.draw()


start_for_triangle = sd.get_point(100, 100)
triangle(point=start_for_triangle, angle=45, length=150)
sd.sleep(1)
sd.clear_screen()


def square(point, angle, length):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=2)
    v1.draw()
    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 90, length=length, width=2)
    v2.draw()
    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 180, length=length, width=2)
    v3.draw()
    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 270, length=length, width=2)
    v4.draw()


start_for_square = sd.get_point(400, 100)
square(point=start_for_square, angle=-15, length=150)
sd.sleep(1)
sd.clear_screen()


def pentagon(point, angle, length):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=2)
    v1.draw()
    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 72, length=length, width=2)
    v2.draw()
    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 144, length=length, width=2)
    v3.draw()
    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 216, length=length, width=2)
    v4.draw()
    v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 288, length=length, width=2)
    v5.draw()


start_for_pentagon = sd.get_point(150, 350)
pentagon(point=start_for_pentagon, angle=30, length=125)
sd.sleep(1)
sd.clear_screen()


def hexagon(point, angle, length):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=2)
    v1.draw()
    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 60, length=length, width=2)
    v2.draw()
    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 120, length=length, width=2)
    v3.draw()
    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 180, length=length, width=2)
    v4.draw()
    v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 240, length=length, width=2)
    v5.draw()
    v6 = sd.get_vector(start_point=v5.end_point, angle=angle + 300, length=length, width=2)
    v6.draw()


start_for_hexagon = sd.get_point(500, 350)
hexagon(point=start_for_hexagon, angle=60, length=100)
sd.sleep(1)
sd.clear_screen()


# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)


def draw_vector(point, angle, n):
    for _ in range(n):
        v = sd.get_vector(start_point=point, angle=angle, length=100, width=2)
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



# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!

sd.sleep(1)
sd.clear_screen()
sd.pause()
