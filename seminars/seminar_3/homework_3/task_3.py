"""
Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
ценность. В случае с английским алфавитом очки распределяются так:
● A, E, I, O, U, L, N, S, T, R – 1 очко;
● D, G – 2 очка;
● B, C, M, P – 3 очка;
● F, H, V, W, Y – 4 очка;
● K – 5 очков;
● J, X – 8 очков;
● Q, Z – 10 очков.
А русские буквы оцениваются так:
● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
● Д, К, Л, М, П, У – 2 очка;
● Б, Г, Ё, Ь, Я – 3 очка;
● Й, Ы – 4 очка;
● Ж, З, Х, Ц, Ч – 5 очков;
● Ш, Э, Ю – 8 очков;
● Ф, Щ, Ъ – 10 очков.
Напишите программу, которая вычисляет стоимость введенного пользователем слова.
Будем считать, что на вход подается только одно слово, которое содержит либо только
английские, либо только русские буквы.
Ввод:
ноутбук
Вывод:
12
"""


def get_en_points():
    dictionary_en = {
        1: 'A' 'E' 'I' 'O' 'U' 'L' 'N' 'S' 'T' 'R',
        2: 'D' 'G',
        3: 'B' 'C' 'M' 'P',
        4: 'F' 'H' 'V' 'W' 'Y',
        5: 'K',
        8: 'J' 'X',
        10: 'Q' 'Z'
    }

    temp = []
    text = input('Enter the text: ')
    print('The resulting value:', text)
    text = text.upper()
    for i in text:
        temp += [keys for keys, value in dictionary_en.items() if i in value]
    print(f'Вы набрали {sum(temp)} очков')


def get_ru_points():
    dictionary_ru = {
        1: 'А' 'В' 'Е' 'И' 'Н' 'О' 'Р' 'С' 'Т',
        2: 'Д' 'К' 'Л' 'М' 'П' 'У',
        3: 'Б' 'Г' 'Ё' 'Ь' 'Я',
        4: 'Й' 'Ы',
        5: 'Ж' 'З' 'Х' 'Ц' 'Ч',
        8: 'Ш' 'Э' 'Ю',
        10: 'Ф' 'Щ' 'Ъ'
    }

    temp = []
    text = input('Введите текст: ')
    print('Полученное значение: ', text)
    text = text.upper()
    for i in text:
        temp += [keys for keys, value in dictionary_ru.items() if i in value]
    print(f'Вы набрали {sum(temp)} очков')


def checking_the_input(language):
    language_ru = 'русский'
    language_en = 'english'
    if language.lower() == language_ru:
        get_ru_points()
    elif language.lower() == language_en:
        get_en_points()
    else:
        print('Введено неверное значение!')
        print('Invalid value entered!')


def main():
    language = input('Введите язык словаря (Enter the dictionary language): ')
    checking_the_input(language)


if __name__ == '__main__':
    main()
