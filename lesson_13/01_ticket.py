# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont, ImageColor
import argparse

# Заполнить все поля в билете на самолет.
# Создать функцию, принимающую параметры: ФИО, откуда, куда, дата вылета,
# и заполняющую ими шаблон билета Skillbox Airline.
# Шаблон взять в файле lesson_013/images/ticket_template.png
# Пример заполнения lesson_013/images/ticket_sample.png
# Подходящий шрифт искать на сайте ofont.ru


def make_ticket(fio, from_, to, date):
    im = Image.open(r'C:\Users\neni2\PycharmProjects\Kirill\skillbox_course\lesson_13\images\ticket_template.png')

    draw = ImageDraw.Draw(im=im)
    font = ImageFont.truetype('ofont.ru_Nunito.ttf', size=15)

    draw.text(xy=(50, 120), text=fio, fill=ImageColor.colormap['black'], font=font)
    draw.text(xy=(50, 190), text=from_, fill=ImageColor.colormap['black'], font=font)
    draw.text(xy=(50, 255), text=to, fill=ImageColor.colormap['black'], font=font)
    draw.text(xy=(285, 255), text=date, fill=ImageColor.colormap['black'], font=font)

    im.show()


# fio = input('Введите ФИО: ')
# from_ = input('Откуда отправляетесь: ')
# to = input('Куда отправляетесь: ')
# date = input('Дата отправки: ')

# make_ticket(fio=fio,
#             from_=from_,
#             to=to,
#             date=date)

# Усложненное задание (делать по желанию).
# Написать консольный скрипт c помощью встроенного python-модуля agrparse.
# Скрипт должен принимать параметры:
#   --fio - обязательный, фамилия.
#   --from - обязательный, откуда летим.
#   --to - обязательный, куда летим.
#   --date - обязательный, когда летим.
#   --save_to - необязательный, путь для сохранения заполненнего билета.
# и заполнять билет.

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Вывод билетика.',
                                     add_help=True)

    parser.add_argument('fio', type=str, help='ФИО')
    parser.add_argument('from_', type=str, help='Откуда')
    parser.add_argument('to_', type=str, help='Куда')
    parser.add_argument('date', type=str, help='Дата')

    args = parser.parse_args()

    make_ticket(fio=args.fio,
                from_=args.from_,
                to=args.to_,
                date=args.date)
