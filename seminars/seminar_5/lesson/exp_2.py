"""Задача №33. Решение в группах
Хакер Василий получил доступ к классному журналу и
хочет заменить все свои минимальные оценки на
максимальные. Напишите программу, которая
заменяет оценки Василия, но наоборот: все
максимальные – на минимальные.
Input: 5 -> 1 3 3 3 4
Output: 1 3 3 3 1"""
import random


def get_new_rating(rating, n, count=0, new_rating=None):
    if new_rating is None:
        new_rating = []
    if count == n:
        return new_rating
    else:
        new_rating.append(1) if rating[count] > 3 else new_rating.append(rating[count])
    return get_new_rating(rating, n, count + 1, new_rating)


def main():
    n = int(input('Введите общее количество оценок: '))
    rating = [random.randint(1, 5) for _ in range(n)]
    print(rating)
    print(get_new_rating(rating, n))


if __name__ == '__main__':
    main()
