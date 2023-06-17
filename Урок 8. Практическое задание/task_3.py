"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""


class OnlyInteger:
    def __init__(self, attr):
        self.attr = attr

    def __set__(self, instance, value):
        if not type(value) == int:
            raise ValueError("Можно вводить только числа")
        instance.__dict__[self.attr] = value


class Numbers:
    number1 = OnlyInteger('number1')
    number2 = OnlyInteger('number2')
    number3 = OnlyInteger('number3')
    number4 = OnlyInteger('number4')
    number5 = OnlyInteger('number5')

    def __init__(self, number1, number2, number3, number4, number5):
        self.number1 = number1
        self.number2 = number2
        self.number3 = number3
        self.number4 = number4
        self.number5 = number5

    def average_num(self):
        return (self.number1 + self.number2 + self.number3 + self.number4 + self.number5) / 5


OBJ = Numbers(50, 43, 40, 5, 0)
print(f"Среднее арифметическое - {OBJ.average_num()}")

OBJ2 = Numbers("aaa", 43, 40, 5, 0)
print(f"Среднее арифметическое - {OBJ2.average_num()}")



