class Cell:

    def __init__(self, c_number):
        self.c_number = c_number

    def __add__(self, other):
        return self.c_number + other.c_number

    def __sub__(self, other):
        if self.c_number > other.c_number:
            return self.c_number - other.c_number
        else:
            raise ValueError

    def __mul__(self, other):
        return self.c_number * other.c_number

    def __truediv__(self, other):
        return round(self.c_number / other.c_number)

    def make_order(self, line):
        for i in range(int(self.c_number) // line):
            print('*' * line)
        print('*' * (int(self.c_number) % line))


cell_1 = Cell(29)
cell_2 = Cell(2)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 / cell_2)
print(cell_1 * cell_2)
print(cell_1.make_order(5))

