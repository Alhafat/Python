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
        '1': 'A' 'E' 'I' 'O' 'U' 'L' 'N' 'S' 'T' 'R',
        '2': 'D' 'G',
        '3': 'B' 'C' 'M' 'P',
        '4': 'F' 'H' 'V' 'W' 'Y',
        '5': 'K',
        '8': 'J' 'X',
        '10': 'Q' 'Z'
    }
    print(dictionary_en)
    temp=0
    text=input('Enter the text: ')
    print('The resulting value:', text)
    text=text.upper()
    array = [i for i in text]
    for i in array:
        for keys,value in dictionary_en.items():
            for k in value:
                if i==k:
                    temp+=eval(keys)
                    continue
    print(f'Вы набрали {temp} очков')


def get_ru_points():
    dictionary_ru = {
        '1': 'А' 'В' 'Е' 'И' 'Н' 'О' 'Р' 'С' 'Т',
        '2': 'Д' 'К' 'Л' 'М' 'П' 'У',
        '3': 'Б' 'Г' 'Ё' 'Ь' 'Я',
        '4': 'Й' 'Ы',
        '5': 'Ж' 'З' 'Х' 'Ц' 'Ч',
        '8': 'Ш' 'Э' 'Ю',
        '10': 'Ф' 'Щ' 'Ъ'
    }
    print(dictionary_ru)

    temp = 0
    text = input('Enter the text: ')
    print('Полученное значение: ', text)
    text = text.upper()
    array = [i for i in text]
    for i in array:
        for keys, value in dictionary_ru.items():
            for k in value:
                if i == k:
                    temp += eval(keys)
                    continue
    print(f'Вы набрали {temp} очков')


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
