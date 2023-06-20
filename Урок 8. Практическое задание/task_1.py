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

class Date:
    # day_month_year = "dd.mm.yyyy"



    def __init__(self, day_month_year):
         self.day_month_year = day_month_year



    @staticmethod
    def validation(day_month_year):
        year_min = 1
        year_max = 9999
        month_min = 1
        month_max = 12
        day_min = 1
        day_max = 31
        d1 = day_month_year.split(".")
        day = int(d1[0])
        month = int(d1[1])
        year = int(d1[2])
        if (year_min <= year <=  year_max) and  (day_min <= day <= day_max) and  (month_min <= month <=  month_max) :
            return  day_month_year
        else:
            print (f"Некорректная дата")





    @classmethod
    def to_int(cls, day_month_year):
         d1 = day_month_year.split(".")
         print    (d1)
         day = int (d1[0])
         month = int (d1[1])
         year = int (d1[2])
         print(f"День = {day} месяц = {month} год = {year}" )


d2 = Date("10.01.1040")

d3 = "10.02.2019"
print(f"Date = {d3}")

Date.to_int("05.08.2045")

d3 = Date("20.02.2020")
Date.to_int("05.06.2021")


Date.to_int("06.06.2022")
Date.validation("12.13.2022")
Date.validation("33.10.2000")




# d1.to_int("10.12.2020")
# print (f"day = {d1}")
# d1.to_int("10.02.2019")
# print(f"date  = {a1.day_month_year}")
# d1.validation_day()
# d1.validation_month(da)
# d1.validation_year()
# print (f"Date = {d1}")
# Date.validation_year()
