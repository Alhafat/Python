"""Задача №37. Решение в группах
15 минут
Дано натуральное число N и последовательность из N элементов.
Требуется вывести эту последовательность в обратном порядке.
Примечание. В программе запрещается объявлять массивы и использовать циклы
(даже для ввода и вывода).
Input: 2 -> 3 4
Output: 4 3"""


def get_source_numbers(n, numbers='', count=0):
    numbers += str(count)
    if len(numbers) == n:
        return numbers
    return get_source_numbers(n, numbers, count + 1)


def get_reverse_numbers(n, source_numbers, reverse_numbers=''):
    reverse_numbers += str(n - 1)
    if len(reverse_numbers) == len(source_numbers):
        return reverse_numbers
    return get_reverse_numbers(n - 1, source_numbers, reverse_numbers)


def main():
    n = int(input('Введите длину последовательности: '))
    source_numbers = get_source_numbers(n)
    print(' '.join(source_numbers))
    # result=' '.join(source_numbers[::-1])
    # print(result)
    print(' '.join(get_reverse_numbers(n, source_numbers)))


if __name__ == '__main__':
    main()
