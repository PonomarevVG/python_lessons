# Задание 8.2
# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class ZerroDevision(Exception):
    def __init__(self, exception_txt):
        self.txt = exception_txt


a = int(input('Введите число a: '))
b = int(input('Введите число b: '))
try:
    if b == 0:
        raise ZerroDevision('Число b не должно быть равно 0! Делить на ноль нельзя!')
    print(f'a/b = {a / b}')
except ZerroDevision as err:
    print(err.txt)
