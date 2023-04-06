"""
Задача №49. Решение в группах.
Создать телефонный справочник с возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер телефона - данные,
которые должны находиться в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в
текстовом файле
3. Пользователь может ввести одну из
характеристик для поиска определенной
записи(Например имя или фамилию
человека)
4. Использование функций. Ваша программа
не должна быть линейной
"""

# import json
# import os.path
#
#
# # def serialization() -> str:
# #     return json.dump()
#
#
# def find_contact(contact: dict) -> dict:
#     what_find = input('Введите искомое значение: ')
#     found = filter(lambda x: what_find in contact, contact)
#     on_screen()
#
#
# def file_path(file_name='exp_1'):
#     return os.path.join(os.path.dirname(__file__), f'{file_name}.txt')
#
#
# def load_from_file():
#     path = file_path()
#     with open(path, 'r', encoding='UTF-8') as file:
#         data = json.load(file)
#     print(data)
#
#
# def save_to_file(contact: dict):
#     path = file_path()
#     with open(path, 'w', encoding='UTF-8') as file:
#         json.dump(contact, file, ensure_ascii=False)
#     print('Значение передано')
#
#
# def on_screen(contact: dict) -> None:
#     decode_keys = dict(
#         first_name='Имя',
#         seond_name='Фамилия',
#         number='Телефон'
#     )
#     pretty_text = '\n'.join(f'{decode_keys[k]} {v}' for k, v in contact.items())
#     print(pretty_text)
#
#
# def create_contact_dict():
#     pass
#
#
# def new_contact() -> dict:
#     return dict(
#         first_name=input('Введите имя: '),
#         seond_name=input('Введите фамилию: '),
#         number=input('Введите контактный номер: ')
#     )
#
#
# def main() -> None:
#     contact = new_contact()
#     # contact = dict(
#     #     first_name='j',
#     #     seond_name='j',
#     #     number='123'
#     # )
#     on_screen(contact)
#     save_to_file(contact)
#     load_from_file()
#     find_contact(contact)
#
#
# if __name__ == '__main__':
#     main()

import json
from cmd2 import Cmd

import os


class PhoneApp(Cmd):
    phonebook = list()

def set_book(self, filename):
    self.filename = filename
    if os.path.exists(self.filename):
        self.import_phonebook()

def import_phonebook(self) -> None:
    with open(self.filename, 'r') as fd:
        self.phonebook = json.load(fd)
        fd.close()

def export_phonebook(self) -> None:
    with open(self.filename, 'w') as fd:
        json.dump(self.phonebook, fd)
        fd.close()

def do_add_contact(self, _):
    self.phonebook.append(
        dict(
            firstname=input("Введите имя:"),
            lastname=input("Введите фамилию:"),
            numbers=input("Введите номер:")
        )
    )

def print_contact(self, contact):
    print("\t".join([contact[i] for i in contact]))

def do_search_contact(self, criteria):
    for contact in self.phonebook:
        flag = False

# import os
# import json
#
#
# def find_contact(contacts: list) -> dict:
#     what = input('Кого ищем?\n>>> ')
#     found = list(filter(lambda el: what in el['first_name'] or what in el['second_name'], contacts))
#     if found:
#         show_on_screen(found)
#     else:
#         print('Никого не нашли ;(')
#
#
# def file_path(file_name='contact_list'):
#     return os.path.join(os.path.dirname(__file__), f'{file_name}.txt')
#
#
# def load_from_file():
#     path = file_path()
#
#     with open(path, 'r', encoding='UTF-8') as file:
#         data = json.load(file)
#
#     return data
#
#
# def save_to_file(contact: list) -> None:
#     path = file_path()
#
#     with open(path, 'w', encoding='UTF-8') as file:
#         json.dump(contact, file, ensure_ascii=False)
#
#
# def show_on_screen(contacts: list) -> None:
#     decode_keys = dict(
#         first_name='Имя:',
#         second_name='Фамилия:',
#         contacts='Телефон:'
#     )
#     pretty_text = str()
#     for num, elem in enumerate(contacts, 1):
#         pretty_text += f'Контакт №{num}:\n'
#         pretty_text += '\n'.join(f'{decode_keys[k]} {v}' for k, v in elem.items())
#         pretty_text += '\n________\n'
#     print(pretty_text)
#
#
# def create_contact_info():
#     pass
#
#
# def new_contact(contacts: list) -> None:
#     # Контактной информации может быть больше чем только телефон
#     # contacts.append(
#         dict(
#             first_name=input('Введите имя контакта:\n>>> '),
#             second_name=input('Введите фамилию контакта:\n>>> '),
#             contacts=input('Введите номер телефона:\n>>> ')
#         )
#     # )
#
#
# def menu():
#     commands = [
#         'Показать все контакты',
#         'Найти контакт',
#         'Создать контакт'
#     ]
#     print('Укажите номер команды:')
#     print('\n'.join(f'{n}. {v}' for n, v in enumerate(commands, 1)))
#     choice = input('>>> ')
#
#     try:
#         choice = int(choice)
#         if choice < 0 or len(commands) < choice:
#             raise Exception('Такой команды пока нет ;(')
#         choice -= 1
#     except ValueError as ex:
#         print('Я вас не понял, повторите...')
#         menu()
#     except Exception as ex:
#         print(ex)
#         menu()
#     else:
#         return choice
#
#
# def main() -> None:
#     print('Программа запущена...')
#     data = load_from_file()
#
#     command = menu()
#     if command == 0:
#         show_on_screen(data)
#     elif command == 1:
#         find_contact(data)
#     elif command == 2:
#         new_contact(data)
#
#     save_to_file(data)
#     print('Конец программы!')
#
#
# def tests():
#     contact = dict(
#         first_name='Иван',
#         second_name='Иванов',
#         contacts='123'
#     )
#     contact2 = dict(
#         first_name='Петр',
#         second_name='Петров',
#         contacts='123'
#     )
#     contact3 = dict(
#         first_name='Петр',
#         second_name='Иванов',
#         contacts='123'
#     )
#     contact4 = dict(
#         first_name='Иван',
#         second_name='Петров',
#         contacts='123'
#     )
#     contacts = [contact, contact2, contact3, contact4]
#     return contacts
#
#
# if __name__ == '__main__':
#     main()
