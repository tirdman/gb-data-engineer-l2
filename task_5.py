"""
5. Реализовать структуру «Рейтинг», представляющую собой не
возрастающий набор натуральных чисел
(каждый элемент ряда меньше или равен предыдущему).

У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.

Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.

Набор натуральных чисел можно задать непосредственно в коде,
например, my_list = [7, 5, 3, 3, 2].
"""

int_list = [9, 7, 4]

while True:
    in_num = int(input('Введите новый элемент рейтинга: '))

    # Если новое число больше существующих в списке, то вставляем в начало
    if in_num > max(int_list):
        int_list.insert(0, in_num)

    else:
        # Проверка (с конца листа) является ли новое число меньше существующих в списке
        for index, next_val in enumerate(int_list[::-1]):

            if next_val >= in_num:
                int_list.insert(len(int_list) - index, in_num)
                break

    print(int_list)