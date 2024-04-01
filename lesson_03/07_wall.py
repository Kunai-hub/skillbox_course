# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for


# start_x = -50
# end_x = 50
# start_y = 0
# end_y = 50
# step = -500
#
# for y in range(0, 600, 50):
#     step += 50
#     for x in range(0, 1500, 100):
#         point_1 = sd.get_point(start_x + x + step, start_y + y)
#         point_2 = sd.get_point(end_x + x + step, end_y + y)
#         sd.rectangle(point_1, point_2, width=1)


row = 0
for y in range(0, 600, 50):
    row += 1
    for x in range(0, 600, 100):
        x_0 = x if row % 2 else x + 100 // 2
        point_1 = sd.get_point(x_0, y)
        point_2 = sd.get_point(x_0 + 100, y + 50)
        sd.rectangle(point_1, point_2, width=1)


sd.pause()
