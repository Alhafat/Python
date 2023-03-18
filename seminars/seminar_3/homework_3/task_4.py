"""
Напишите программу, которая принимает на вход две строки и определяет,
являются ли они анаграммами. Знаки препинания, пробелы и регистр при этом игнорируются.

Пример ввода:
Цари, вино и сало.
Лисица и ворона.
"""


def get_list_value(val_1, val_2):
    value_1 = sorted([e.lower() for e in val_1 if e.isalnum()])
    value_2 = sorted([e.lower() for e in val_2 if e.isalnum()])
    return value_1, value_2


def lists_comparison(value_1, value_2):
    if len(value_1) == len(value_2):
        for i in range(len(value_1)):
            if value_1[i] == value_2[i]:
                continue
            else:
                print('Строки не являются анаграммами.')
                return
        print('Строки являются анаграммами.')


def main():
    value_1 = input('Введите первую строку для проверки: ')
    value_2 = input('Введите вторую строку для проверки: ')
    value_1, value_2 = get_list_value(value_1, value_2)
    lists_comparison(value_1, value_2)


if __name__ == '__main__':
    main()
