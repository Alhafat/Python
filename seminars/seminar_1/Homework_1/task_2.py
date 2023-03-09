# Задача 2: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

# # Вариант 1
# print('\n\tЗадача 2: Найдите сумму цифр трехзначного числа.',end='\n\n')
# while True:
#     number=input('Введите трехзначное число: ')
#     if len(number)!=3:
#         print('Введено неверное число! Введите трехзначное!!!')
#     else: break
# print('Сумма цифр введенного числа равна',sum([int(x) for x in number]))

# # Вариант 2
print('\n\tЗадача 2: Найдите сумму цифр трехзначного числа.', end='\n\n')
number = None
while number is None or len(number) !=3 and not number.isdigit():
    print('Введите трехзначное число:' if number is None else 'Введено неверное число! Введите трехзначное:', end=' ')
    number = input()
print('Сумма цифр введенного числа равна', sum([int(x) for x in number]))