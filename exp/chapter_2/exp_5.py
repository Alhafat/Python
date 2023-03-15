"""
Напишите следующую программу. Пользователь вводит список целочисленных значений,
а также верхнюю границу для вычисления суммы. Программа вычисляет сумму натуральных чисел,
но за исключением тех, которые входят в список. Например, если пользователь ввел список
[2, 5, 6] и 10 в качестве верхней границы суммы, то программа должна вычислить сумму чисел от 1 до 10,
но без учета чисел 2, 5 и 6.
"""


# numbers = [1, 2, 8, 9]
# n = int(input('Введите границу вычисления суммы: '))
# numbers_user = [x for x in range(0, n + 1)]
# print(numbers_user)
# for i in numbers_user[::-1]:
#     for k in numbers:
#         if i == k:
#             del numbers_user[i.__index__()]
#             # numbers_user.remove(i)
#             # numbers_user[i.__index__()]=0
# print(numbers_user)
# print(sum(numbers_user))


def all_combinations(a):
    if len(a) <= 1:
        yield a
    else:
        head = ''
        tail = list(a)
        while len(tail) > 0:
            head += tail.pop(0)
            for s in all_combinations(tail):
                yield [head] + s


def all_signs(n):
    if n == 0:
        yield ()
    else:
        for tail in all_signs(n-1):
            for s in '+-':
                yield (s,) + tail


def perform_operations(nums, signs):
    nums = list(map(int, nums))
    result = nums.pop(0)
    # n = 1
    for s in signs:
        if s == '+':
            result += nums.pop(0)
        if s == '-':
            result -= nums.pop(0)
        # n += 1
    return result


for numbers in all_combinations(tuple(map(str, range(1, 10)))):
    #print(numbers)
    for signs in all_signs(len(numbers) - 1):
        #print(signs)
        summ = perform_operations(numbers, signs)
        if summ == 100:
            print(''.join(map(lambda x: ''.join(x), zip(numbers, signs))) + numbers[-1])