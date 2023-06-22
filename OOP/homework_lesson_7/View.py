class UserView:

    @staticmethod
    def input_from_user():
        select = input("1. Операция сложения\n"
                       "2. Операция вычитания\n"
                       "3. Операция умножения\n"
                       "4. Операция деления\n"
                       "Введите требуемое действие:\n")
        a = input('Введите комплексное число вида a+bj, где a и b числа: \n>> ')
        b = input('Введите комплексное число вида a+bj, где a и b числа: \n>> ')
        return a, b, select

    @staticmethod
    def show_result(result):
        print(result)


