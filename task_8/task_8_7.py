# Задание 8.7
# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
# Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта.
# Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class Complex:
    def __init__(self, na, nb):
        self.a = na
        self.b = nb

    def __add__(self, other):
        return Complex(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return Complex(self.a * other.a - self.b * other.b, self.b * other.a + self.a * other.b)

    def __str__(self):
        return '{}+{}i'.format(self.a, self.b)


c1 = Complex(1, 2)
c2 = Complex(3, 4)
print(f'{c1} + {c2} = {c1 + c2}')
print(f'{c1} * {c2} = {c1 * c2}')