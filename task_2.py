"""
Задание 2. Для списка реализовать обмен значений соседних элементов,
т.е. значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().

Пример:
Введите целые числа через пробел: 1 2 3 4
Результат: 2 1 4 3

Введите целые числа через пробел: 1 2 3
Результат: 2 1 3
"""

in_numbers_list = [int(item) for item in input('Введите целые числа через пробел: ').split()]

for index, next_num in enumerate(in_numbers_list):

    if index % 2 == 0 and index + 1 < len(in_numbers_list):
        in_numbers_list[index], in_numbers_list[index + 1] = in_numbers_list[index + 1], in_numbers_list[index]

print(in_numbers_list)
