"""
Задача №15. Решение в группах
Иван Васильевич пришел на рынок и решил
купить два арбуза: один для себя, а другой для тещи.
Понятно, что для себя нужно выбрать арбуз
тяжелее, а для тещи полегче. Но вот незадача:
арбузов слишком много и он не знает как же выбрать
самый легкий и самый тяжелый арбуз? Помогите ему!
Пользователь вводит одно число N – количество
арбузов. Вторая строка содержит N чисел,
записанных на новой строчке каждое. Здесь каждое
число – это масса соответствующего арбуза
Input: 5 -> 5 1 6 5 9
Output: 1 9
"""


import random


def get_weight_array(n):
    array = [random.randint(1, 10) for _ in range(0, n + 1)]
    return array


def main():
    n = int(input('Введите количество арбузов: '))
    weight_array = get_weight_array(n)
    print(weight_array)
    print(f'Арбуз с минимальным весом {min(weight_array)}')
    print(f'Арбуз с максимальным весом {max(weight_array)}')


main()
