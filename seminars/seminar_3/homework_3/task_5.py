"""
Напишите функцию, которая принимает словарь с параметрами и возвращает строку запроса,
сформированную из отсортированных в лексикографическом порядке параметров.

Пример:

Код print(query({'course': 'python', 'lesson': 2, 'challenge': 17})) должен возвращать строку:

challenge=17&course=python&lesson=2
"""

# print(({'course': 'python', 'lesson': 2, 'challenge': 17}))


def print_dict(values):
    text=sorted([f'{key}={value}' for key,value in values.items()])
    text='&'.join(text)
    print(text)


def main():
    dictionary={'course': 'python', 'lesson': 2, 'challenge': 17}
    print_dict(dictionary)

if __name__ == '__main__':
    main()

