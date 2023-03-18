"""
Напишите программу, которая принимает на вход две строки и определяет,
являются ли они анаграммами. Знаки препинания, пробелы и регистр при этом игнорируются.

Пример ввода:
Цари, вино и сало.
Лисица и ворона.
"""


def get_list_value(val):
    value = sorted([e.lower() for e in val if e.isalnum()])
    return value


def lists_comparison(val_1, val_2):
    check = len(val_1) == len(val_2)
    if check:
        for i in range(len(val_1)):
            if val_1[i] != val_2[i]:
                check = not check
                break
    return check


def main():
    value_1 = input('Введите первую строку для проверки: ')
    value_2 = input('Введите вторую строку для проверки: ')
    value_list_sorted_1 = get_list_value(value_1)
    value_list_sorted_2 = get_list_value(value_2)
    lists_comparison(value_1, value_2)
    is_anagram = lists_comparison(value_1, value_2)
    print(f'Строка {"" if is_anagram else "не "}является анаграммой')


if __name__ == '__main__':
    main()
