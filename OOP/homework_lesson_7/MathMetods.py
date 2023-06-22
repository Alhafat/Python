from abc import ABC, abstractmethod


class MathMetods(ABC):
    pass

    @abstractmethod
    def addition(self):
        pass

    @abstractmethod
    def substraction(self):
        pass

    @abstractmethod
    def multiplication(self):
        pass

    @abstractmethod
    def division(self):
        pass
