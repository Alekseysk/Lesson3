"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def division(n1, n2):
    """
    Деление чиселок
    :param n1: первая чиселка
    :param n2: вторая чиселка
    :return: частное
    """
    if n2 == 0:
        return None
    return n1 / n2


n1, n2 = input('Введите 2 числа, через пробел:\n').split()
if n1.isdigit() and n2.isdigit():
    print(division(int(n1), int(n2)))
else:
    print('Неверный ввод!!!')
