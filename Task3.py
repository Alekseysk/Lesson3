"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму
наибольших двух аргументов.
"""


def my_func(*n):
    """
    Сумма двух наибольших
    """
    m_list = list(n)
    min_ind = m_list.index(min(m_list))
    m_list.pop(min_ind)
    return sum(m_list)


print(my_func(3, 1, 1))

