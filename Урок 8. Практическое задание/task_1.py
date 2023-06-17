"""
Задание 1.

Реализовать класс «Дата», на уровне класса определить атрибут day_month_year,
присвоить ему значение

В рамках класса реализовать два метода.

Первый, с декоратором @classmethod, должен извлекать число, месяц,
год, преобразовывать их тип к типу «Число» и делать атрибутами класса.

Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""


###

class Data:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
        year_min = 1
        year_max = 9999
        month_min = 1
        month_max = 12
        day_min = 1
        day_max = 31

    def day_month_year(self):
        return f"Дата : {self.day}.{self.month}.{self.year}"

    @staticmethod
    def validation_year(cls, year):
        return cls.year_min <= year <= year_max

    @staticmethod
    def validation_month(cls, month):
        return cls.month_min <= month <= month_max

    @staticmethod
    def validation_day(cls, day):
        return cls.day_min <= day <= day_max

    def to_int_day(cls, day):
        return cls.int(day)

    @classmethod
    def to_int_month(cls, month):
        return (cls, int(month))

    @classmethod
    def to_int_year(cls, year):
        return (cls, int(year))


a1,a2,a3 = input("Введите дату  в формате дд.мм.гггг: ").split()
Data.day_month_year((a1,a2,a3))
print(f"Дата : {a1}")
