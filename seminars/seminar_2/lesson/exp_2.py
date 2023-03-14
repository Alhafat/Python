"""
Задача №11. Решение в группах
Дано натуральное число A > 1. Определите, каким по
счету числом Фибоначчи оно является, то есть
выведите такое число n, что φ(n)=A. Если А не
является числом Фибоначчи, выведите число -1.
Input: 5
Output: 6
"""


# def array_fibo(n):
#     array = [0,1]
#     while n>array[-1]:
#         array.append(array[-1] + array[-2])
#     true=f'Введенное число {n} в последовательности расположено под номером {len(array)}'
#     print(true) if array[-1]==n else print("-1")
#
#
# def main():
#     n = int(input('Введите число для поиска в последовательности: '))
#     array_fibo(n)
#
#
# main()


n = 13
a, b = 1, 1
print(a, b, end=" ")
for k in range(n - 2):
    a, b = b, a + b
    print(b, end=" ")