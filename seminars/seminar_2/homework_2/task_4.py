# У вас есть девять цифр: 1, 2, …, 9. Именно в таком порядке. Вы можете вставлять между ними знаки «+», «-» или ничего.
# У вас будут получаться выражения вида 123+45-6+7+89. Найдите все из них, которые равны 100.
#
# numbers = "123456789"
# plus_sign="+"
# minus_sign="-"
# array=["0"]
# count=0
# for n in numbers:
#     array.append(numbers[count:])
#     for i in numbers[count+1:]:
#         if eval("".join(array))<100:
#             array.append(plus_sign)
#             array.append(i)
#         elif eval("".join(array)) == 100:
#             print(array)
#         else:
#             array.append(minus_sign)
#             array.append(i)
#         del array[1:]
#     count+=1

#
# def all_combinations(a):
#     if len(a) <= 1:
#         yield a
#     else:
#         head = ''
#         tail = list(a)
#         while len(tail) > 0:
#             head += tail.pop(0)
#             for s in all_combinations(tail):
#                 yield [head] + s
#
# def all_signs(n):
#     if n == 0:
#         yield ()
#     else:
#         for tail in all_signs(n-1):
#             for s in '+-':
#                 yield (s,) + tail
#
# def perform_operations(nums, signs):
#     nums = list(map(int, nums))
#     result = nums.pop(0)
#     n = 1
#     for s in signs:
#         if s == '+':
#             result += nums.pop(0)
#         if s == '-':
#             result -= nums.pop(0)
#         n += 1
#     return result
#
# for numbers in all_combinations(tuple(map(str, range(1, 10)))):
#     #print(numbers)
#     for signs in all_signs(len(numbers) - 1):
#         #print(signs)
#         summ = perform_operations(numbers, signs)
#         if summ == 100:
#             print(
#                 ''.join(map(
#                     lambda x: ''.join(x),
#                     zip(numbers, signs)))
#                 + numbers[-1])

# s, d, summ, count = '123456789', {'0': '', '1': '+', '2': '-'}, 100, 0
#
# for n in range(int('22222222', 3)):
#     lst, rslt = [], ''
#
#     if n == 0: lst.append('0')
#     while n:
#         lst.append(str(n % 3)); n //= 3
#
#     num = f"{''.join(lst):0>8}"
#
#     for i, j in list(zip(s, num)): rslt += i + d[j]
#
#     if eval(rslt + '9') == summ:
#         print(f'{rslt + "9"}={summ}'); count += 1
#
# print(f'Всего {count} выражений')
