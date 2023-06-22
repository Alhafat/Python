from OOP.homework_lesson_7.MathMetods import MathMetods


class Calculate(MathMetods):
    __left: complex
    __right: complex

    def __init__(self) -> None:
        super().__init__()
        self.left = 0
        self.right = 0

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, value: complex):
        self.__left = complex(value)

    @property  #
    def right(self):
        return self.__right

    @right.setter
    def right(self, value: complex):
        self.__right = complex(value)

    def addition(self):
        return self.left + self.right

    def substraction(self):
        return self.left - self.right

    def multiplication(self):
        return self.left * self.right

    def division(self):
        return self.left / self.right



