"""Дано натуральное число n>1.
Выведите все простые множители этого числа в порядке неубывания с учетом кратности.
Алгоритм должен иметь сложность O(logn)
"""

def prime_factors(n, divisor=2):
    if n == 1:
        return
    if n % divisor == 0:
        print(divisor, end=" ")
        prime_factors(n//divisor, divisor)
    else:
        prime_factors(n, divisor+1)


def main():
    n = int(input('Введите число: '))
    prime_factors(n)


if __name__ == '__main__':
    main()
