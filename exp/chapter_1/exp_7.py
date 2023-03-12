"""
Напишите программу, которая создает список и чисел,
при делении на 5 и дающие в остатке 3(вычисляются по формуле 5*k+3, где k=0,1,2...).
Отобразить этот список в прямом и обратном порядках.
"""


def new_list(k):
    array = [5 * k + 3 for k in range(0, k)]
    return array


def main():
    k = int(input('Введите максимальное значение длинны списка k: '))
    list = new_list(k)
    print(list)
    print(sorted(list, reverse=True))

main()
