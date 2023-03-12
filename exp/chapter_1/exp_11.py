"""
Напишите программу, в которой описана функция, возвращающая результатом
второе по величине число в списке, переданном функции в качестве аргумента.
"""
import random


def get_array(n):
    array = [random.randint(-50, 50) for i in range(n)]
    array = sorted(array)
    print(array)
    print(array[-2])


def main():
    n = int(input('Введите длину списка: '))
    get_array(n)


main()
