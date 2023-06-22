from typing import Any

from Value import Calculate
from View import UserView


class Controller:
    models: Any  # объявление атрибутов класса с любым типом данных
    view: Any

    def __init__(self) -> None:
        self.models = Calculate()  # назначение переменных
        self.view = UserView()

    def switch_case(self, a, b, select):
        self.models.left = a
        self.models.right = b
        match select:
            case "1":
                self.view.show_result(self.models.addition())
            case "2":
                self.view.show_result(self.models.substraction())
            case "3":
                self.view.show_result(self.models.multiplication())
            case "4":
                self.view.show_result(self.models.division())
            case _:
                self.view.show_result("Введено некорректное значение")
