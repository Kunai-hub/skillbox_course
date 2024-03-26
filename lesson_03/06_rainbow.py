# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)


# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
# start_point = sd.get_point(50, 50)
# end_point = sd.get_point(350, 450)
# line = sd.line(start_point, end_point, color = sd.COLOR_RED, width = 4)
# start_point = sd.get_point(55, 50)
# end_point = sd.get_point(355, 450)
# line = sd.line(start_point, end_point, color = sd.COLOR_ORANGE, width = 4)
# start_point = sd.get_point(60, 50)
# end_point = sd.get_point(360, 450)
# line = sd.line(start_point, end_point, color = sd.COLOR_YELLOW, width = 4)
# start_point = sd.get_point(65, 50)
# end_point = sd.get_point(365, 450)
# line = sd.line(start_point, end_point, color = sd.COLOR_GREEN, width = 4)
# start_point = sd.get_point(70, 50)
# end_point = sd.get_point(370, 450)
# line = sd.line(start_point, end_point, color = sd.COLOR_CYAN, width = 4)
# start_point = sd.get_point(75, 50)
# end_point = sd.get_point(375, 450)
# line = sd.line(start_point, end_point, color = sd.COLOR_BLUE, width = 4)
# start_point = sd.get_point(80, 50)
# end_point = sd.get_point(380, 450)
# line = sd.line(start_point, end_point, color = sd.COLOR_PURPLE, width = 4)

def lines(color):
    for x in range(5, 36, 5):
        start_point = sd.get_point(50 + x, 50)
        end_point = sd.get_point(350 + x, 450)
        sd.line(start_point=start_point, end_point=end_point, color=color, width=2)


for c in rainbow_colors:
    print(c)

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
# TODO здесь ваш код

sd.pause()
