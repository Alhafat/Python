"""
Задача №31. Решение в группах
Последовательностью Фибоначчи называется
последовательность чисел a0
, a1
, ..., an
, ..., где
a0
 = 0, a1
 = 1, ak
 = ak-1 + ak-2 (k > 1).
Требуется найти N-е число Фибоначчи
Input: 7
Output: 21
Задание необходимо решать через рекурсию
"""


def get_value_fib(fib, n):
    fib.append(fib[-2] + fib[-1])
    if len(fib) == n:
        return fib
    return get_value_fib(fib, n)


def main():
    fib = [0, 1]
    n = int(input('Введите длину последовательности: '))
    print(get_value_fib(fib, n))


if __name__ == '__main__':
    main()
