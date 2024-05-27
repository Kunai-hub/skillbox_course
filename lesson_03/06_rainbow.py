# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)


# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)

x_1 = 50
x_2 = 350

for color in rainbow_colors:
    start_point = sd.get_point(x_1, 50)
    end_point = sd.get_point(x_2, 450)
    sd.line(start_point=start_point, end_point=end_point, color=color, width=3)
    x_1 += 5
    x_2 += 5

sd.sleep(1)
sd.clear_screen()

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво

radius = 400

for color in rainbow_colors[::-1]:
    point = sd.get_point(500, -50)
    sd.circle(center_position=point, radius=radius, color=color, width=15)
    radius += 15

sd.sleep(1)
sd.clear_screen()
sd.pause()
