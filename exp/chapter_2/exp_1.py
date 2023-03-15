"""
Напишите программу, в которой пользователь вводит целое число, а программа определяет,
сколько в этом числе цифр 0,1,2 и т.д, до 9
"""

import math


def show_number_in_number():
    number = input('Введите любое число: ')
    temp = [0]*10
    for k in number:
        temp[int(k)]+=1
    text='\n'.join(f'{x[0]}--->{x[1]}' for x in enumerate(temp,0) if x[1]!=0)
    print(text)


def main():
    show_number_in_number()


if __name__ == '__main__':
    main()
