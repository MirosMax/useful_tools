'''
Болотная сортировка

Болотная сортировка (Bogosort) — неэффективный алгоритм сортировки, используемый только в образовательных целях и
противопоставляемый другим, более реалистичным алгоритмам.

Принцип работы алгоритма прост, как плесень. Перетряхиваем список случайным образом до тех пор пока он внезапно не
отсортируется. Процесс может счастливо завершиться сразу, а может длиться до тепловой смерти Вселенной.
Это уж как повезёт.

'''


import random
import time


def is_sort(nums):                   # отсортирован ли список?
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            return False
    return True


def bogosort(nums):                  # реализация алгоритма болотной сортировки
    count = 0
    start = time.time()
    while not is_sort(nums):
        random.shuffle(nums)
        count += 1
    stop = time.time()
    print(f'Время сортировки заняло: {stop - start} сек.\nПонадобилось итераций: {count:,}')
    return nums


numbers = list(range(10))
random.shuffle(numbers)              # перемешиваем начальный список
print(numbers)                       # выводим начальный список

sorted_numbers = bogosort(numbers)

print(sorted_numbers)