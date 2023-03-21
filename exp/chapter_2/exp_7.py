"""
Напишите программу, в которой пользователь вводит три числа, а программа определяет,
являются ли эти числа тремя последовательными элементами арифметической последовательности.
В арифметической последовательности каждый новый член получается прибавлением к предыдущему
определенного фиксированного числа.
"""

# numbers = [int(i) for i in input('введите последовательность чисел через пробел: ').split()]
# print('Получены следующие значения: ', *numbers)
# d = numbers[1] - numbers[0]
# for i in range(len(numbers) - 1):
#     if numbers[i + 1] - numbers[i] == d:
#         continue
#     else:
#         print('no')
#         break
# else:
#     print('yes')

sequence = [15, 10, 5]
sequence_steps = set(map(lambda i: sequence[i - 1] - sequence[i], range(1, len(sequence))))
print(True if len(sequence_steps) == 1 else False)