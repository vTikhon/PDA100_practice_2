import string
import random
import statistics

# Задание
# Дана строка:
# string_01 = "History is always written by the winners. hen two cultures clash, the loser is obliterated,
# and the winner writes the history books-books which glorify their own cause and disparage the conquered foe.
# As Napoleon once said, ' What is history, but a fable agreed upon?"
# Посчитайте, сколько в строке символов, исключая пробелы
# Посчитайте, сколько в строке слов.
# Напишите функцию, которая будет принимать в качестве аргумента букву и выводить все слова из строки,
# начинающиеся на эту букву (например, “w”).

string_01 = "History is always written by the winners. hen two cultures clash, the loser is obliterated, " \
            "and the winner writes the history books-books which glorify their own cause and disparage " \
            "the conquered foe. As Napoleon once said, ' What is history, but a fable agreed upon?"

def calc_symbols(s: str) -> int:
    return len(list(s.replace(' ', '')))

def calc_words(s: str) -> int:
    for ch in string.punctuation:
        s = s.replace(ch, ' ')
    return len(list(s.split()))

def print_words(s: str):
    char_ = input('Введите букву: ')
    for ch in string.punctuation:
        s = s.replace(ch, ' ')
    all_words = s.split()
    filtered_words = [word for word in all_words if word.lower().startswith(char_.lower())]
    print(f'Слова, начинающиеся на букву {char_}: {", ".join(filtered_words)}')

print('\n')
print(f'Количество символов в строке, исключая пробелы: {calc_symbols(string_01)}')
print(f'Количество слов в строке, исключая символы: {calc_words(string_01)}')
print_words(string_01)
print('\n')



# Задание
# Создайте список из 100 случайных значений от -100 до 100 и вычислите медиану.

def create_list():
    return [random.randint(-100, 100) for _ in range(100)]

def calc_mediana(list):
    return statistics.median(list)

created_list = create_list()
print(created_list)
print(f'медиана: {calc_mediana(created_list)}')
print('\n')



# Задание
# Для случайно заданного списка из 1000 целых чисел в диапазоне от 100 до 200 определите количество
# и сумму чисел больше 170 и меньше 195.

def create_list():
    return [random.randint(100, 200) for _ in range(1000)]

def calc_quantity_and_sum(list) -> int:
    quantity = 0
    sum = 0
    for el in list:
        if 170 < el < 195:
            quantity += 1
            sum += el
    return quantity, sum

created_list = create_list()
print(created_list)
print(f'кол-во и сумма: {calc_quantity_and_sum(created_list)}')