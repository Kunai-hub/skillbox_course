from random import sample

_bulls_cows = {}

def guess_number():
    _digits = list('0123456789')
    _first_digit = sample(_digits[1:], 1)
    _digits.remove(_first_digit[0])
    global _number
    _number = ''.join(_first_digit + sample(_digits, 3))
    return _number

def check_number(user_number):
    count_bulls = 0
    count_cows = 0
    for i, item in enumerate(_number):
        if item in user_number:
            if user_number.index(item) == i:
                count_bulls += 1
            else:
                count_cows += 1

    _bulls_cows['bulls'] = count_bulls
    _bulls_cows['cows'] = count_cows
    return _bulls_cows


# def guess_number():
#     _digits = list('0123456789')
#     _first_digit = sample(_digits[1:], 1)
#     _digits.remove(_first_digit[0])
#     _number = ''.join(_first_digit + sample(_digits, 3))
#     global res
#     res = [int(x) for x in _number]
#     return res
#
# def check_number(user_number):
#     count_bulls = 0
#     count_cows = 0
#     list_user_number = [int(x) for x in user_number]
#     for i, item in enumerate(res):
#         if item in list_user_number:
#             if list_user_number.index(item) == i:
#                 count_bulls += 1
#             else:
#                 count_cows += 1
#
#     _bulls_cows['bulls'] = count_bulls
#     _bulls_cows['cows'] = count_cows
#     return _bulls_cows