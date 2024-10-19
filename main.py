# Задание
# Напишите программу, которая выводит на экран все четные числа на интервале от 1 до 250 с шагом 3.

# for i in range(1, 251, 3):
#     print(i, end=' ')




# Задание
# Напишите программу для подсчета суммы четных чисел на интервале от 10 до 150 с шагом 5.

# res_sum = 0  #variant 1
# for i in range(10, 151, 5):
#     if i % 2 == 0:
#         res_sum += i
# print(res_sum)
#
# res_sum2 = sum([i for i in range(10, 151, 5) if i % 2 == 0])  #variant 2
# print(res_sum2)
#
# res_sum3 = sum(filter(lambda x: x % 2 == 0, [i for i in range(10, 151, 5)]))  #variant 3
# print(res_sum3)




# Задание
# У нас есть список, содержащий информацию о среднедневной температуре в Фаренгейтах за произвольный период
# по странам
# (структура данных в примере).
# Необходимо написать код, который рассчитает среднюю температуру за период в Цельсиях(!) для каждой страны.
# Формула перевода F в С °C = (°F - 32) × 5/9.
# Пример работы программы:
# countries_temperature = [
# ['Thailand', [75.2, 77, 78.8, 73.4, 68, 75.2, 77]],
# ['Germany', [57.2, 55.4, 59, 59, 53.6]],
# ['Russia', [35.6, 37.4, 39.2, 41, 42.8, 39.2, 35.6]],
# ['Poland', [50, 50, 53.6, 57.2, 55.4, 55.4]]
# ]

# countries_temperature = [
#     ['Thailand', [75.2, 77, 78.8, 73.4, 68, 75.2, 77]],
#     ['Germany', [57.2, 55.4, 59, 59, 53.6]],
#     ['Russia', [35.6, 37.4, 39.2, 41, 42.8, 39.2, 35.6]],
#     ['Poland', [50, 50, 53.6, 57.2, 55.4, 55.4]]
# ]
#
# def convert_temp(temp):
#     return (temp - 32) * 5/9
#
# data = []
# for country in countries_temperature:
#     sum_ = 0
#     for temp_f in country[1]:
#         temp_c = convert_temp(temp_f)
#         sum_ += temp_c
#     data.append([country[0], sum_ / len(country[1])])
# print(data)
#
# data2 = []
# for country in countries_temperature:
#     data2.append([country[0], sum(map(lambda x: (x - 32) * 5/9, country[1])) / len(country[1])])
# print(data2)




# Задание
# Дан список:
# list_01 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 14, 46, 273, 22, 99, 15, 1000]
# Напишите алгоритм, который выводит сумму элементов списка, которые больше 10, но меньше 100,
# или которые больше 200,
# но меньше 500.

# list_01 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 14, 46, 273, 22, 99, 15, 1000]
# sum_ = 0
# for el in list_01:
#     if 10 < el < 100 or 200 < el < 500:
#         sum_ += el
# print(sum_)  #variant_1
#
# print(sum([el for el in list_01 if 10 < el < 100 or 200 < el < 500]))  #variant_2
#
# print(sum(filter(lambda el: 10 < el < 100 or 200 < el < 500, list_01)))  #variant_3




# Задание
# Напишите функцию для расчета заработной платы.
# На вход функции передаются два аргумента: отработанные часы (hours) и почасовая ставка оплаты труда (pay_rate).
# Функция возвращает зарплату: pay = hours * pay_rate

# def payment(hours, pay_rate):
#     return hours * pay_rate
# print(payment(160, 20))




# Задание
# Создайте функцию is_palindrome для проверки того, что переданное слово одинаково
# читается в обоих направлениях. Функция возвращает значения True или False.

# def is_palendrom(s: str) -> bool:
#     new_s = s.lower().strip()
#     return new_s == new_s[::-1]
# print(is_palendrom('abba'))
# print(is_palendrom('abcd'))
# print(is_palendrom('а роза упала на лапу Азора'))




# Задание
# Напишите собственную функцию, не используя стандартную abs, для поиска
# абсолютного значения числа.
# Пример вызова функции:
# my_abs(-2)

# def my_abs(x):
#     return x if x >= 0 else -x
# print(my_abs(-2))




# Задание
# Напишите функцию str_lower(), которая принимает на вход строку (набор слов через
# пробел), а возвращает список ее элементов в нижнем регистре.
# Пример:
# Входные данные:
# "В лесу родилась ёлочка В лесу она росла"
# Выходные данные:
# ['в', 'лесу', 'родилась', 'ёлочка', 'в', 'лесу', 'она', 'росла']

# def str_lower(s: str):
#     return s.lower().split()
# print(str_lower("В лесу родилась ёлочка В лесу она росла"))




# Задание
# С помощью метода join из списка lst = [4, '5', '6', 8] получить '4568'

# lst = [4, '5', '6', 8]
# def join_list(data: list):
#     for i in range(len(data)):
#         if not isinstance(data[i], str):
#             data[i] = str(data[i])
#     return ''.join(data)
# print(join_list(lst))  #variant_1
#
# print(''.join(map(str, lst)))  #variant_2
# print(''.join([str(el) for el in lst]))  #variant_3




# Задание
# Напишите функцию, которая ищет общие элементы двух списков (списки - входные
# аргументы) и возвращает список, состоящий из найденных элементов.

# data_1_ = [1, 2, 3, 4, 4]
# data_2_ = [4, 5, 6, 4]
# def inter_lists(data_1, data_2):
#     if len(data_1) > len(data_2):
#         new_data_1 = data_2
#         new_data_2 = data_1
#     else:
#         new_data_1 = data_1
#         new_data_2 = data_2
#     data_res = []
#     for el in new_data_1:
#         if el in new_data_2:
#             data_res.append(el)
#     return data_res
# print(inter_lists(data_1_, data_2_))
#
# def inter_lists_ver2(data_1, data_2):
#     return list(set(data_1).intersection(data_2))
# print(inter_lists_ver2(data_1_, data_2_))




# Задание
# Написать функцию, которая принимает в качестве аргумента строку и подсчитывает в
# ней количество символов в верхнем и нижнем регистре.

# def func(s: str):
#     count_l, count_u = 0, 0
#     for ch in s:
#         if ch.islower():
#             count_l += 1
#         elif ch.isupper():
#             count_u += 1
#     print(f'Количество нижних = {count_l}\nКоличество верхних = {count_u}')
# func('sllkLKJSVLKMSlmsv')




# Задание
# Написать функцию, которая принимает строку с разделенными дефисом словами и
# возвращает эту же строку со словами отсортированными в алфавитном порядке.
# Например, строка “green-red-yellow-black-white” должна быть преобразована в строку
# “black-green-red-white-yellow”.

# def sorted_str(s):
#     return '-'.join(sorted(s.split('-')))
# print(sorted_str('green-red-yellow-black-white'))





# Задание
# Напишите программный код, который будет создавать новый список,
# содержащий в качестве элементов квадратные корни всех чисел из списка [2, 4, 9, 16, 25].

# data_ = [2, 4, 9, 16, 25]
# print([el ** 2 for el in data_])  #variant_1
#
# def list_squares(data):
#     res_data = []
#     for el in data:
#         res_data.append(el ** 2)
#     return res_data
# print(list_squares(data_))  #variant_2
#
# print(list(map(lambda el: el ** 2, data_)))  #variant_3
