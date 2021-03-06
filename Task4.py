"""
Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо
выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

** Подсказка:** попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью
оператора **. Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
"""


def super_power(x, y):
    """
    Возведение в степень
    """
    y = round(y)
    res1 = x
    for i in range(y-1):
        res1 *= x
    
    res2 = x ** y
    
    return res1, res2


print(super_power(1.234, 128))

