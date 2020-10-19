"""
6. *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

Пример готовой структуры:
[
    (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
    (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
    (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]

Далее необходимо собрать аналитику о товарах. Реализовать словарь,
в котором каждый ключ — характеристика товара, например название,
а значение — список значений-характеристик, например список названий товаров.

Пример:

{
“названия”: [“компьютер”, “принтер”, “сканер”],
“цены”: [20000, 6000, 2000],
“количества”: [5, 2, 7],
“ед”: [“шт.”]
}
"""

list_product = []

while True:
    name_product, price_product, quantity_product, unit_product = None, None, None, None
    while not name_product:
        name_product = input('Введите название товара: ')
        if not name_product:
            print('===> Вы не ввели значение.')

    while not price_product:
        price_product = float(input('Введите стоимость товара: '))
        if not price_product:
            print('===> Вы не ввели значение.')

    while not quantity_product:
        quantity_product = int(input('Введите количество товара: '))
        if not quantity_product:
            print('===> Вы не ввели значение.')

    while not unit_product:
        unit_product = input('Введите единицу измерения товара(по умолчанию "шт."): ') or 'шт.'
        if not unit_product:
            print('===> Вы не ввели значение.')

    new_product = {
        'название': name_product, 'цена': price_product, 'количество': quantity_product, 'eд': unit_product
    }

    while True:
        is_add_new_item = input(f'Добавить новый товар в корзину [да/нет]? {new_product}: ')
        if is_add_new_item.lower() == 'да':
            list_product.append((len(list_product) + 1, new_product))
            break
        elif is_add_new_item.lower() == 'нет':
            break

    is_exit_adding_items = input(f'Для выхода из процедуры добавления товара введите 0: ')
    if is_exit_adding_items == '0':
        break

print(f'Итоговый лист товаров\n{list_product}')

