"""
Задача №11. Решение в группах
Дано натуральное число A > 1. Определите, каким по
счету числом Фибоначчи оно является, то есть
выведите такое число n, что φ(n)=A. Если А не
является числом Фибоначчи, выведите число -1.
Input: 5
Output: 6
"""


def array_fibo(n):
    array = [0, 1]
    for k in range(1, n + 1):
        temp = array[k] + array[k - 1]
        array.append(temp)
    return array


def find_number(result, n):
    count = 1
    for number in result:
        if number == n:
            print(f'Введенное число {n} в последовательности расположено под номером {count}')
            return
        count += 1
    else: print("-1")


def main():
    n = int(input('Введите количество чисел последовательности: '))
    result = array_fibo(n)
    print(result)
    find_number(result, n)


main()
