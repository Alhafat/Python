"""
 №21. Решение в группах
Напишите программу для печати всех уникальных значений в словаре.
Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
{"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
":" S007 "}]
Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
Примечание: Список словарей задан изначально. Пользователь его не вводит
"""


def get_result(dictionary):
    result = list()
    for i in dictionary:
        [result.append(values) for keys, values in i.items()]
    result = set(result)
    print(result)


def main():
    dictionary = [
        {"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
        {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"},
        {"VIII": "S007"}]
    get_result(dictionary)


if __name__ == '__main__':
    main()
