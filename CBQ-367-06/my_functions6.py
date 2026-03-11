def sum_ignore_non_numbers(items):

    total = 0
    for i in items:
        if type(i) == int or type(i) == float:
            total += i

    return total

# print(sum_ignore_non_numbers([1, 2, 6.7, 10.0, 'Hey', None, 4.3]))




def is_triangle(length_1, length_2, length_3):
    if ((length_1 + length_2 > length_3) and
    (length_1 + length_3 > length_2) and
    (length_3 + length_2 > length_1)):
        return True
    else:
        return False
#
# print(is_triangle(3, 4, 5))
#
#
#
#
def average(*args):
    summ = 0

    if len(args) == 0:
        return 0
    for i in args:
        summ += i

    result = summ / len(args)
    return result
#
# print(average(1, 2, 3, 4, 5, 6, 7, 8))
#
#
#
#
# text = input('Введите текст: ')
# result = ''
#
# for i in range(len(text)):
#     symbol = text[i]
#
#     if i % 2 == 0:
#         symbol = symbol.upper()
#     else:
#         symbol = symbol.lower()
#
#     result = result + symbol
#
# print(result)