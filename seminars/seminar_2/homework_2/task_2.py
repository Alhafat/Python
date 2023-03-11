"""
Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
школьница. Петя помогает Кате по математике. Он задумывает два
натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
этого Петя делает две подсказки. Он называет сумму этих чисел S и их
произведение P. Помогите Кате отгадать задуманные Петей числа.
4 4 -> 2 2
5 6 -> 2 3
"""
import random
import math

def get_unknown_numbers():
    array = [random.randint(1, 1000) for _ in range(2)]
    print(array)
    array = [sum(array), math.prod(array)]
    return array
    return array

def get_numbers(numbers):
    x = 0
    while x*(numbers[0] - x) < numbers[1]:
        x += 1
    y = numbers[0] - x
    print(f'Числа загаданные Петей {x} и {y}')

def main():
    numbers=get_unknown_numbers()
    print('Сумма', sum(numbers))
    print('Произведение', math.prod(numbers))
    get_numbers(numbers)

main()
