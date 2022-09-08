"""
Задание 1.

Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init()__),
который должен принимать данные (список списков) для формирования матрицы.
[[], [], []]
Следующий шаг — реализовать перегрузку метода __str()__ для вывода матрицы в привычном виде.

Далее реализовать перегрузку метода __add()__ для реализации операции
сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.

Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.

Пример:
1 2 3
4 5 6
7 8 9

1 2 3
4 5 6
7 8 9

Сумма матриц:
2 4 6
8 10 12
14 16 18
"""

l1 = []
l2 = []
l3 = []
sum_lst = []
list1 = []
list2 = []
list3 = []
list4 = []

lst_1 = []


# print(lst_1[0])


class Matrix:
    def __init__(self, *args):
        self.new_lst = list(args)

    def __str__(self):
        #  for el in self.new_lst:
        #      print('{el}\n')
        pass

    def __add__(self, other):
        for el1 in self.new_lst:
            l1 = []
            for el2 in el1:
                l1.append(0)
            l2.append(l1)
            l1 = []
        sum_lst = l2

        # print(f'sum_lst={sum_lst}')
        # print(f'sum_lst_0_0={sum_lst[0][0]}')
        for i in range(0, len(self.new_lst)):
            for j in range(0, len(self.new_lst[i])):
                # print(f'i={i}')
                # print(f'sum_lst_0_0={sum_lst[0][0]}')
                # print(f'sum_lst_i_j={sum_lst[i][j]}')

                sum_lst[i][j] = self.new_lst[i][j] + other.new_lst[i][j]
        # print(f'sum_lst...={sum_lst}')
        return sum_lst

        #   i = 0
        #   for el1 in self.new_lst:
        #       i = 0
        #       list1 = []
        #       for el2 in el1:
        #           print(f'el1={el1}')
        #           print(f'el2={el2}')

        #           list1.append(el2)
        #           print(f'i={i}')
        #           print(f'list1={list1}')
        #           # i += 1
        #       list2.append(list1)
        #       print(f'list2={list2}')

        # for el1 in other.new_lst:
        #    i = 0
        #    list3 = []
        #    for el2 in el1:
        #        print(f'el1={el1}')
        #        print(f'el2={el2}')

        #        list3.append(el2)
        #        print(f'sum_lst_i= {sum_lst[0][0]}')
        #        print(f'i={i}')
        #        print(f'list1={list1}')
        #        i += 1
        #    list4.append(list3)
        #    print(f'list4={list4}')

        # return sum_lst


m1 = Matrix([1, 5, 7], [3, 3, 5], [7, 2, 1])
m2 = Matrix([3, 3, 3], [5, 5, 5], [7, 7, 7])

print(m1 + m2)
