"""
Задача №13. Решение в группах
Уставшие от необычно теплой зимы, жители решили узнать,
действительно ли это самая длинная оттепель за всю историю
наблюдений за погодой. Они обратились к синоптикам, а те, в
свою очередь, занялись исследованиями статистики за
прошлые годы. Их интересует, сколько дней длилась самая
длинная оттепель. Оттепелью они называют период, в
который среднесуточная температура ежедневно превышала
0 градусов Цельсия. Напишите программу, помогающую
синоптикам в работе.
Пользователь вводит число N – общее количество
рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках
располагается N целых чисел.
Каждое число – среднесуточная температура в
соответствующий день. Температуры – целые числа и лежат в
диапазоне от –50 до 50
Input: 6 -> -20 30 -40 50 10 -10
Output: 2
"""
import random


def get_list(n):
    array = [random.randint(-50, 50) for _ in range(n)]
    return array


def find_days_above_zero(days):
    count = 0
    array = []
    for temp in days:
        if temp > 0:
            count += 1
            array.append(count)
        else:
            count = 0
    return array


def main():
    n = int(input('Введите количество дней: '))
    days = get_list(n)
    print(days)
    result = find_days_above_zero(days)
    print(f'Максимальная продолжительность оттепели составила {max(result)} суток')


main()
