"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""

print('Пожалуйста, введите целое положительное число: ')
s = input()  # считываем строку, переводим в int и кладём её в переменную
a = int(s) + int(s+s) + int (s+s+s)
print(f"Сумма чисел n + nn + nnn = {a}")