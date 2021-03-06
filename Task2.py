"""
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя,
фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры
как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
"""


def user_info(name, family_name, year_birth, home_city, email, phone):
    """
    вывод данных о пользователе
    """
    print(f'=============================================\n'
          f'Пользователь: {name} {family_name}, {year_birth} г.р.\n'
          f'проживает в г. {home_city}\n'
          f'электронная почта: {email}\nтелефон: {phone}\n'
          f'=============================================')


user_info(name='Алексей', family_name='Клименко', year_birth=1976, home_city='Новосибирск',
          email='aleksey@gmail.com', phone='+7(456) 07-05-033')
