class Matrix:
    def __init__(self, list_of_lists):
        self.list_of_lists = list_of_lists

    def __str__(self):
        return '\n'.join(map(str, self.list_of_lists))

    def __add__(self, other):
        for x in range(len(self.list_of_lists)):
            for y in range(len(self.list_of_lists[x])):
                self.list_of_lists[x][y] = self.list_of_lists[x][y] + other.list_of_lists[x][y]
        return Matrix.__str__(self)


lst = Matrix([[-1, 6, 1], [-4, 0, 1], [7, 1, -1], [1, 5, -7]])

lst_2 = Matrix([[1, 7, 9], [-7, 9, 2], [0, 2, -2], [2, 2, -7]])
print(lst.__add__(lst_2))