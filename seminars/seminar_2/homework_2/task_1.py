"""
Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
решкой, а некоторые – гербом. Определите минимальное число
монеток, которые нужно перевернуть, чтобы все монетки были
повернуты вверх одной и той же стороной. Выведите минимальное
количество монет, которые нужно перевернуть.
5 -> 1 0 1 1 0
2
"""

import random


def checking_the_input(n):
    if n == 1:
        print('Сколько не верти, лучше не станет!')
    elif n == 0:
        print('Может для начала разложим монеты?..')
    elif n < 0:
        print('Совсем что-ле?..')
    else:
        resource = get_array(n)
        get_how_much_to_turn_over(resource)


def get_array(n):
    array = [random.choice(['O', 'R']) for _ in range(0, n)]
    return array


def get_how_much_to_turn_over(resource):
    count = 0
    temp = 0
    for i in resource:
        if i == 'R':
            count += 1
        else:
            temp += 1
    print(resource)
    array = [count, temp]
    if count == 0 or temp == 0:
        print('Ничего не нужно переворачивать!')
    elif count != temp:
        print(f'Минимальное количество монет к перевороту: {min(array)}')
    else:
        print('Не важно какие переворачивать!')


def main():
    checking_the_input(n=int(input('Введите количество монет: ')))


main()
