"""
Напишите программу, в которой описан класс со следующими свойствами.
В классе описан конструктор, которому в качестве аргументов
(помимо первой ссылки на создаваемый объект) передаются текст и целое число,
причем в произвольном порядке. Число и текст присваиваются как значения определенным полям.
Если переданы два текстовых значения, то создается только текстовое поле со значением,
получающимся объединением значений аргументов. Если аргументами переданы два числовых поля,
то у объекта будет только поле с целочисленным
значением, равным сумме значений аргументов. В иных случаях поля
для объекта не создаются. Создать на основе класса объекты и проверить функциональность кода.
"""


class SomeClass:
    some_value_int: int
    some_value_str: str

    def __init__(self, val_1, val_2) -> None:
        if isinstance(val_1, int) and isinstance(val_2, int):
            self.some_value_int = sum([val_1, val_2])
        elif isinstance(val_1, str) and isinstance(val_2, str):
            self.some_value_str = val_1 + val_2

    def show(self):
        if self.__dict__.get("some_value_str", 0):
            print("value_str =", self.some_value_str)
        elif self.__dict__.get("some_value_int", 0):
            print("value_int =", self.some_value_int)
