'''
Функция print_operation_table()
Реализуйте функцию print_operation_table(), которая принимает три аргумента в следующем порядке:

operation — функция, характеризующая некоторую бинарную операцию
rows — натуральное число
cols — натуральное число
Функция должна составлять и выводить таблицу из rows строк и cols столбцов, в которой элемент со строкой n и столбцом
m имеет значение operation(n, m).

Примечание 1. Нумерация строк и столбцов в таблице начинается с единицы.

Примечание 2. Элементы в строках таблицы должны быть разделены одним пробелом, причем выравнивать таблицу
необязательно.

Примечание 3. Бинарная операция — математическая операция, принимающая два аргумента и возвращающая один результат.
'''


def print_operation_table(operation, rows, col):
    matrix = [['_'] * col for _ in range(rows)]

    for n in range(len(matrix)):
        for m in range(len(matrix[n])):
            matrix[n][m] = operation(n + 1, m + 1)
        print(*matrix[n])


if __name__ == "__main__":
    print_operation_table(pow, 5, 4)
    print()
    print_operation_table(lambda a, b: a * b, 5, 5)