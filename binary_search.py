a, b = input('Введите диапазон чисел, где будем искать, в формате "a:b"\n').split(':')
x = int(input('Какое целое число ищем?\n'))

arr = range(int(a), int(b) + 1)

left, right = 0, len(arr) - 1
counter = 0
if x > int(b) or x < int(a):
    print('Такого числа нет в диапазоне')
else:
    while True:
        counter += 1
        temp = (right - left) // 2 + left
        if arr[temp] == x:
            print(f'Индекс искомого числа: {temp}\nПопыток потребовалось: {counter}')
            break
        elif arr[temp] > x:
            right = temp - 1
        elif arr[temp] < x:
            left = temp + 1
