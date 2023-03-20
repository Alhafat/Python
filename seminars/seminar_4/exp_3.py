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
    numbers = [randint(1111, 10000) for _ in range(n)]
    print(numbers)
    return numbers


def get_max_number(numbers):
    array=numbers.copy()
    count = 0
    n=-1
    # while n!=0:
    #     if temp>0:
    #         n=temp%10
    #         temp=array[count]=array[count]//10
    #     elif count<len(numbers)-1:
    #         count += 1
    #         temp=array[count]
    #     else:
    #         break
    while n != 0:
        if array[count] > 0:
            n = array[count] % 10
            array[count] = array[count] // 10
        elif count < len(numbers) - 1:
            count += 1
        else:
            break
    if count==0 and n==0:
        print(f'Элемент последовательности включающей 0 расположен первым ---> {numbers[0]}')
    elif 0<count<len(numbers) and n==0:
        print(f'Значение наибольшего элемента последовательности, '
            f'которая завершается первым встретившимся нулем равно {max(numbers[:count])}')
    else:
        print('Некорректная последовательность, значение 0 отсутствует')


def main():
    n = int(input('Введите длину последовательности: '))
    if n==0:
        print('Пустая последовательность.')
        return
    numbers = get_list(n)
    get_max_number(numbers)


if __name__ == '__main__':
    main()
