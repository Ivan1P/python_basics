"""
Задание 2.

Реализовать проект расчета суммарного расхода ткани на производство одежды.

Единственный класс этого проекта — одежда (класс Clothes).

К типам одежды в этом проекте относятся пальто и костюм.

У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: v и h, соответственно.

Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (v/6.5 + 0.5),
для костюма (2*h + 0.3). Проверить работу этих методов на реальных данных.

Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания: реализовать
абстрактный класс для единственного класса проекта,
проверить на практике работу декоратора @property

Пример:
Расход ткани на пальто = 1.27
Расход ткани на костюм = 20.30
Общий расход ткани = 21.57

Два класса: абстрактный и Clothes
"""

from abc import ABC, abstractmethod


class AClass(ABC):

    @abstractmethod
    def sum_v(self):
        pass
    def sum_h(self):
        pass
    def sum_total(self):
        pass



class Clothes(AClass):

    def __init__(self, v, h):
        self.v = v
        self.h = h

    def sum_v(self, v):
        self.sum_v  = v / 6.5 + 0.5

        return (self.sum_v)

    def sum_h(self, h):
        self.sum_h = h*2 +0.3
        return(self.sum_h)

    def sum_total(self):
        self.sum_total = sum_v + sum_h
        return (sum_total)




zakaz1 = Clothes(2, 1)
print(zakaz1.h)
print(zakaz1.v)
zakaz2 = Clothes(1, 1.5)
print(zakaz1.sum_v)
print(zakaz2.sum_v)
