"""
Задача №29. Решение в группах
Ваня и Петя поспорили, кто быстрее решит
следующую задачу: “Задана последовательность
неотрицательных целых чисел. Требуется определить
значение наибольшего элемента
последовательности, которая завершается первым
встретившимся нулем (число 0 не входит в
последовательность)”. Однако 2 друга оказались не
такими смышлеными. Никто из ребят не смог до
конца сделать это задание. Они решили так: у кого
будет меньше ошибок в коде, тот и выиграл спор. За
помощью товарищи обратились к Вам, студентам.
Примечание: Программные коды на следующих
слайдах

Ваня:
n = int(input())
max_number = 1000
while n != 0:
 n = int(input())
 if max_number > n:
 max_number = n
print(max_number)

Петя:
n = int(input())
max_number = -1
while n < 0:
 n = int(input())
 if max_number < n:
 n = max_number
print(n)
"""
from random import randint


def get_list(n):
    numbers = [randint(0, 10) for _ in range(n)]
    print(numbers)
    return numbers


def get_max_number(numbers):
    i = 0
    count = 0
    if numbers[0] == 0:
        print('0 первое число последовательности.')
    elif i in numbers:
        while i != numbers[count]:
            count += 1
        print(f'Значение наибольшего элемента последовательности, '
              f'которая завершается первым встретившимся нулем равно {max(numbers[:count])}')
    else:
        print('0 в последовательности отсутствует')


def main():
    n = int(input('Введите длину последовательности: '))
    numbers = get_list(n)
    get_max_number(numbers)


if __name__ == '__main__':
    main()
