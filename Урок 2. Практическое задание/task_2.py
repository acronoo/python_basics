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

new_elements = input('Введите целые числа через пробел: ')
new_list = new_elements.split()
for ind, el in enumerate(new_list):
    if ind % 2 == 0:
        new_list.pop(ind)
        new_list.insert(ind + 1, el)
print(new_list)
