
# class Matrix:
#    def __init__(self, list):
#        self.list = list
#
#    def __add__(self, other):
#        ret_matrix = []
#        for el_1, el_2 in zip(self.list, other.list):
#            ret_matrix.append([x + y for x, y in zip(el_1, el_2)])
#
#        return ret_matrix
#
#    def __str__(self):
#        self.list
#        for line in self.list:
#            print(line)
#
#matrix_1 = Matrix([[1, 2, 3],
#                   [4, 5, 6],
#                   [7, 8, 9]])
#matrix_2 = Matrix([[1, 2, 3],
#                   [4, 5, 6],
#                   [7, 8, 9]])
#
#print(matrix_1 + matrix_2)
#


class Matrix:
    def __init__(self, list):
        self.list = list

    def __str__(self):
        return '\n'.join([' '.join([str(el) for el in line]) for line in self.list])

# сложение двух матриц
    def __add__(self, other):
#        ret_matrix = ''
        ret_matrix = []
        if len(self.list) == len(other.list):
            for line_1, line_2 in zip(self.list, other.list):
                if len(line_1) != len(line_2):
                    return 'Размерности матриц не совпадают'

#                line_3 = [x + y for x, y in zip(line_1, line_2)]
#                ret_matrix += ' '.join([str(i) for i in line_3]) + '\n'
                ret_matrix.append([x + y for x, y in zip(line_1, line_2)])
        else:
            return 'Размерности матриц не совпадают'
        return ret_matrix


matrix_1 = Matrix([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
matrix_2 = Matrix([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
#matrix_2 = Matrix([[1, 2, 3], [4, 5, 6], [6, 7, 9], [10, 20, 11]])
matrix_3 = Matrix(matrix_1 + matrix_2)

print(matrix_1)
print()
print(matrix_2)
print()
print(matrix_1 + matrix_2)
print()
print(matrix_3)
