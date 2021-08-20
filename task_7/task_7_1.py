# Задание 7.1
# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
# (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно —
# первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, n_matrix):
        self.elements = []
        for row in n_matrix:
            current_row = []
            for el in row:
                current_row.append(el)
            self.elements.append(current_row)

    def __str__(self):
        s = ''
        for row in self.elements:
            s += ' '.join(map(str, row)) + '\n'
        return s

    def sum_with_larger_matrix(self, larger_matrix):
        for i in range(len(self.elements)):
            for j in range(len(self.elements[i])):
                larger_matrix.elements[i][j] += self.elements[i][j]
        return larger_matrix

    def __add__(self, other):
        height1 = len(self.elements)
        height2 = len(other.elements)

        width1 = len(self.elements[0])
        width2 = len(other.elements[0])

        empty_matrix = Matrix([[0 for j in range(max(width1, width2))] for i in range(max(height1, height2))])

        return other.sum_with_larger_matrix(self.sum_with_larger_matrix(empty_matrix))


matrix1 = Matrix([[31, 21], [37, 43], [51, 86]])
matrix2 = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])

print('Матрица 1:')
print(matrix1)
print('Матрица 2:')
print(matrix2)
print('Сумма матриц:')
print(matrix1 + matrix2)
