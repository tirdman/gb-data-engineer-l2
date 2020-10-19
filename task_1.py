"""
Задание 1. Создать список и заполнить его элементами различных типов данных.
Реализовать проверку типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

Пример:
для списка [5, "string", 0.15, True, None]
результат

<class 'int'>
<class 'str'>
<class 'float'>
<class 'bool'>
<class 'NoneType'>
"""

different_types_list = ['str', 937, 45.4, False, (1, 'tuple'), [4, 'list'], {'set'}, {'dict': 1}, ]

for next_type in different_types_list:
    print(type(next_type))
