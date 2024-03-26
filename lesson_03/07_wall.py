# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

# for y_1, y_2 in range(1, 1001, 100):
#     for x_1, x_2 in range(1, 501, 50):
#         point = sd.get_point(x_1, y)
#         sd.rectangle(left_bottom=point, right_top=point)

start_x = -50
end_x = 50
start_y = 0
end_y = 50
step = -500

for y in range(0, 600, 50):
    step += 50
    for x in range(0, 1500, 100):
        point_1 = sd.get_point(start_x + x + step, start_y + y)
        point_2 = sd.get_point(end_x + x + step, end_y + y)
        sd.rectangle(point_1, point_2, width=1)





# point_1 = sd.get_point(-50, 0)
# point_2 = sd.get_point(50, 50)
# sd.rectangle(point_1, point_2, width=2)

sd.pause()
