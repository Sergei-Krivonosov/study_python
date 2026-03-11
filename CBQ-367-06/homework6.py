# Модуль.
# - Перенесите ваши функции из прошлого домашнего задания в отдельный
# файл и импортируйте их в основной (исполняемый) файл.
# - Запустите каждую вашу функцию по 1 или более раз в исполняемом файле.


from my_functions6 import sum_ignore_non_numbers

result = sum_ignore_non_numbers([1, 2, 6.7, 10.0, 'Hey', None, 4.3])
print(result)


from my_functions6 import is_triangle

result = is_triangle(3, 4, 5)
print(result)


from my_functions6 import average

result = average(1, 2, 3, 4, 5, 6, 7, 8)
print(result)





# Анонимная функция.
# - Создайте анонимную функцию pow, которая принимает 2 аргумента x и y.
# Функция должна возвращать x, возведенное в степень y.

def pow(x, y):

    result = x ** y
    return result

print(pow(2, 3))

# и тот же вариант с лямбдой:

result = lambda x, y: x ** y
print(result(2, 4))



# Змея.
# - Создайте функцию snake_talk, которая принимает 1 аргумент text (строка).
# - Функция должна создать новую строку, где все гласные буквы
# aeiouyAEIOUY в строке text дублируются.
# - Например, такой вызовы функции snake_talk(“Harry”) должен вернуть
# строку “Haaryy”.


def snake_talk(text):
    result = ''
    for i in text:
        if i in 'aeiouyAEIOUY':
            result += i + i
        else:
            result += i
    return result

print(snake_talk('Harry'))





