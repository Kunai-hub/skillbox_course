# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join


from district.central_street.house1 import room1 as central_1_1
from district.central_street.house1 import room2 as central_1_2


from district.central_street.house2 import room1 as central_2_1
from district.central_street.house2 import room2 as central_2_2


from district.soviet_street.house1 import room1 as soviet_1_1
from district.soviet_street.house1 import room2 as soviet_1_2


from district.soviet_street.house2 import room1 as soviet_2_1
from district.soviet_street.house2 import room2 as soviet_2_2


print('На районе живут:', ', '.join(central_1_1.folks), ', '.join(central_1_2.folks),
      ', '.join(central_2_1.folks), ', '.join(central_2_2.folks),
      ', '.join(soviet_1_1.folks), ', '.join(soviet_1_2.folks),
      ', '.join(soviet_2_1.folks), ', '.join(soviet_2_2.folks))