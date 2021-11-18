# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
# принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.

# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для  сложения двух объектов класса Matrix (двух матриц). Результатом
# сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно. Первый элемент первой строки первой матрицы складываем с
# первым элементом первой строки второй матрицы и пр.

# ----------Решение-------------
# импортируем библиотеки
import random
import itertools


# создаем класс Matrix
class Matrix:
    def __init__(self, values):
        self.values = values

    # реализоввываем перегрузку метода __str__()
    def __str__(self):
        matrix = ''
        # возврашаем матрицу как набор строк
        for lines in self.values:
            matrix += f'{lines}\n'
        return matrix.replace('[', '').replace(',', '').replace(']', '').replace(' ', '\t')

    # реализоввываем перегрузку метода __add__()
    def __add__(self, other):
        # матрица там все элементы тотокой представляют собой кортеж (item_from_first_matrix, item_from_second_matrix)
        sum_matrix = []
        # матрица с результатом matrix_1 + matrix_2
        result_matrix = []
        # временная строковая переменная для создания матрицы
        line = []

        def line_generator(length):

            empty_line = [0 for i in range(length)]
            return empty_line

        temp_matrix = list(itertools.zip_longest(self.values, other.values, fillvalue=line_generator(
            max(len(self.values[0]), len(other.values[0])))))
        # добавление остальных строк 0, если размер matrix1 и matrix2 различается

        print('adding lines with required quantity of 0 if matrix1 and matrix2 are different size:')
        print(Matrix(temp_matrix))

        for i in temp_matrix:
            temp_line = list(itertools.zip_longest(*i, fillvalue=0))
            sum_matrix.append(temp_line)
        print('matrix with tuples from first and second matrix (zero columns are added if required)')
        print(Matrix(sum_matrix))

        for l in sum_matrix:
            for i in l:
                line.append(sum(i))
            result_matrix.append(line)
            line = []
        return Matrix(result_matrix)


def random_matrix(lines, columns):
    matrix = []
    for i in range(lines):
        matrix.append([random.randint(0, 9) for n in range(columns)])
    return matrix


# проверяем
matrix_01 = Matrix(random_matrix(7, 2))
matrix_02 = Matrix(random_matrix(5, 5))
print('********************* First Matrix ***************************')
print(matrix_01)
print('********************* Second Matrix ***************************')
print(matrix_02)
print('********************* Summ of first and second matrices ***************************\n')
print(matrix_01.__add__(matrix_02))
