# Осуществить программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс «Клетка».
# В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число). В классе должны
# быть реализованы методы перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()),
# умножение (__mul__()), деление (__floordiv____truediv__()). Эти методы должны применяться только к клеткам и
# выполнять увеличение, уменьшение, умножение и округление до целого числа деления клеток соответственно.
# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух
# клеток.
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять, только если разность количества ячеек двух клеток
# больше нуля, иначе выводить соответствующее сообщение.
# Умножение. Создаётся общая клетка из двух. Число ячеек общей клетки — произведение количества ячеек этих двух клеток.
# Деление. Создаётся общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества
# ячеек этих двух клеток.
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Этот
# метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, а количество ячеек в ряду — 5. В этом случае метод make_order()
# вернёт строку: *****\n*****\n**.
# Или количество ячеек клетки — 15, а количество ячеек в ряду равняется 5. Тогда метод make_order() вернёт строку:
# *****\n*****\n*****.

# ----------Решение-------------

# создаем класс Cell
class Cell:

    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        try:
            return '*' * (self.number + other.number)
        except Exception as e:
            print(e)

    def __sub__(self, other):
        try:
            if self.number - other.number > 0:
                return '*' * (self.number - other.number)
            else:
                return 'initial cell is too small. Subtraction cannot be done.'
        except Exception as e:
            print(e)

    def __mul__(self, other):
        try:
            return '*' * (self.number * other.number)
        except Exception as e:
            print(e)

    def __floordiv__(self, other):
        try:
            if self.number // other.number > 0:
                return '*' * (self.number // other.number)
            else:
                return 'initial cell is too small. Division cannot be done.'
        except Exception as e:
            print(e)

    def __truediv__(self, other):
        try:
            if self.number // other.number > 0:
                return '*' * (self.number // other.number)
            else:
                return 'initial cell is too small. Division cannot be done.'
        except Exception as e:
            print(e)

    def make_order(self, qnty):
        return ('*' * qnty + '\n') * (self.number // qnty) + '*' * (self.number % qnty)


# создаем клетки
cel_1 = Cell(5)
cel_2 = Cell(3)

# проверяем
print(cel_1.__add__(cel_2))
print(cel_1.__sub__(cel_2))
print(cel_2.__sub__(cel_1))
print(cel_1.__mul__(cel_2))
print(cel_1.__floordiv__(cel_2))
print(cel_2.__floordiv__(cel_1))
print(cel_1.__truediv__(cel_2))
print(cel_2.__truediv__(cel_1))
print(cel_1.make_order(2))
