# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

row = 0
for y in range(0, 600, 50):
    row += 1
    for x in range(0, 600, 100):
        x_0 = x if row % 2 else x + 50
        point_1 = sd.get_point(x_0, y)
        point_2 = sd.get_point(x_0 + 100, y + 50)
        sd.rectangle(point_1, point_2, width=1)


sd.pause()
