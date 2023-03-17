"""
Напишите программу, которая принимает на вход две строки и определяет,
являются ли они анаграммами. Знаки препинания, пробелы и регистр при этом игнорируются.

Пример ввода:
Цари, вино и сало.
Лисица и ворона.
"""


value_1=input('Введите первую строку для проверки: ')
value_2=input('Введите вторую строку для проверки: ')


value_1=sorted(e.lower() for e in value_1 if e.isalnum())
value_2=sorted(e.lower() for e in value_2 if e.isalnum())


if len(value_1)!=len(value_2):
    print('Строки не являются анаграммами.')
else:
    dict_1=dict((key,0) for key in set(value_1))
    dict_2=dict((key,0) for key in set(value_2))
    dict_1 = dict()

    [i for i in value_1 if i==eval(key)]

    print(dict_1)
    # print(dict_2)
    dict()