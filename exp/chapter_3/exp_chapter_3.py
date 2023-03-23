from copy import deepcopy
from random import *

# x=[1,2,3]
# # x[2:2]=[10]
# y=x
# x+=[10]
# x=x+[10]
# print(x)
# print(y)


# mas = 'Это просто строка https://xakep.ru Еще одна строка https://habr.ru'
# i='https://xakep.ru'
# if i in mas:
#     print(mas)
#
# a=[[0]*3]*2
# print(a)
# a[0][1]=1
# print(a)
# a=[0]*3
# print(a)
# a[0]=1
# print(a)
#
# a,*b,c = 1,2,3,4,5,6
# print(b)

# a='seed(2019)'
# show(a)
# print(ord('A'))
# print(chr(75)+chr(73)+chr(82)+chr(73)+chr(76)+chr(76)) #дает возможность обратиться к символу
# print(chr(ord('A'))) # выводит номер символа из таблицы

# text = 'Happy birthday, Kirill!!!'
# array=[]
# for i in text:
#     array.append(ord(i))
# print(array)
#
# text=[72, 97, 112, 112, 121, 32, 98, 105, 114, 116, 104, 100, 97, 121, 44, 32, 75, 105, 114, 105, 108, 108, 33, 33, 33]
# array=''
# for i in text:
#     array+=(chr(i))
# print(array)

a = [1, 3, [10, 20], 'python', [40, 50]]
b = a[:]
c = a.copy()
d = deepcopy(a)

print('a: ', a)
print('b: ', b)
print('c: ', c)
print('d: ', d)

a[0] = [100, 200]
a[2][1] = 300
a[3] = 'java'
a[4] = 90
c[4][1] = 'c++'

print('a: ', a)
print('b: ', b)
print('c: ', c)
print('d: ', d)
