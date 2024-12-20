'''
Генератор безопасных паролей

Описание проекта: программа генерирует заданное количество паролей и включает в себя умную настройку на длину пароля,
а также на то, какие символы требуется в него включить, а какие исключить (цифры, строчные буквы, прописные буквы,
символы).
'''

import random

print('\nЗдравствуйте! Я помогу сгенерировать для вас надежные пароли')
print('------------------------------------------------------------')

def setup_generation():
    # создаем строковые константы
    digits = '0123456789'
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    punctuation = '!#$%&*+-=?@^_'

    chars = ''  # здесь будут все символы одобренные пользователем для генерации пароля

    # запрашиваем параметры генерации пароля
    amount_pass = int(input('\nСколько паролей сгенерировать? Введите целое число: '))
    len_pass = int(input('Какой длины будет один пароль? Введите целое число: '))

    flag = True
    while flag:
        include_digits = input('Включать ли цифры 0123456789? (д = да, н = нет) ').strip()
        include_low_alpha = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (д = да, н = нет) ').strip()
        include_upper_alpha = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (д = да, н = нет) ').strip()
        include_punctuation = input('Включать ли символы "!#$%&*+-=?@^_"? (д = да, н = нет) ').strip()

        if include_digits == 'д' or include_low_alpha == 'д' or include_upper_alpha == 'д' or include_punctuation == 'д':
            flag = False
        else:
            print('\nВнимание! Нужно выбрать как минимум один набор символов из которых будет формироваться пароль.')
            print('Попробуем еще раз.\n')

    exclude_chars = input('Исключать ли неоднозначные символы "il1Lo0O"? (д = да, н = нет) ').strip()

    # формируем список символов в зависимости от предпочтений пользователя
    if include_digits.lower() == 'д':
        chars += digits
    if include_low_alpha.lower() == 'д':
        chars += lowercase_letters
    if include_upper_alpha.lower() == 'д':
        chars += uppercase_letters
    if include_punctuation.lower() == 'д':
        chars += punctuation
    if exclude_chars.lower() == 'д':
        chars = list(chars)
        for c in "il1Lo0O":
            if c in chars:
                chars.remove(c)
        chars = ''.join(chars)
    return chars, amount_pass, len_pass


def generate_password(chars, amount_pass, len_pass):
    num = len_pass // len(chars)
    chars *= num + 1  # если длина списка меньше длины запрашиваемого пароля, то кратно увеличиваем список
    print()
    for i in range(amount_pass):
        print(f'Ваш пароль № {i + 1}: ', *random.sample(chars, len_pass), sep='')


generate_password(*setup_generation())

# предлагаем пользователю повторную генерацию пароля
repeat_generate = 'д'
while repeat_generate == 'д':
    print()
    repeat_generate = input('Хотите сгенерировать еще пароли? (д = да, н = нет) ')
    if repeat_generate == 'д':
        generate_password(*setup_generation())
