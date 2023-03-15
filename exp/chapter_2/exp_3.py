"""
Напишите программу, которая на основе списка из натуральных чисел
формирует целое число. Число формируется "объединением" элементов списка,
если исходный список [12,3,456,78], то программа должна получить число 12345678
"""
import random


def get_list(n):
    list=[random.randint(0,1000) for _ in range(0, n)]
    return list


def get_result_list(numbers):
    list=''
    for i in numbers:
        list+=str(i)
    return list


def main():
    n=int(input('Введите длину списка: '))
    numbers=get_list(n)
    print(numbers)
    result=get_result_list(numbers)
    print(result)

if __name__ == '__main__':
    main()