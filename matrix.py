class matrix():
    def __init__(self, matrix):
        self.matrix = matrix
        self.row = len(self.matrix)
        self.column = len(self.matrix[0])

    def __mul__(self, matrix2):
        if self.column == matrix2.row:
            new_matrix = [] #[[0 for j in range(self.line)] for i in range(matrix2.colums-1)] 
            for i in range(self.row):
                new_matrix = [*new_matrix, []]
                for l in range(matrix2.column):
                    new_num = 0
                    for j in range(self.column):
                        new_num += matrix2.matrix[j][l] * self.matrix[i][j]
                    new_matrix[i].append(new_num) 
        return matrix(new_matrix)

    def __str__(self):
        string = '------------- \n'
        for i in self.matrix:
            for j in i:
                string += " {}".format(j)
            string += '\n'
        return string

    def __add__(self, m2):
        new_matrix = []
        if not len(self.matrix) == len(m2.matrix):
            raise TypeError("nem kompatibilis mátrixok")
        for i in range(len(self.matrix)):
            new_matrix.append([])
            for j in range(len(self.matrix[i])):
                new_matrix[i].append(self.matrix[i][j] + m2.matrix[i][j])
        return matrix(new_matrix)

    def __sub__(self, m2):
        new_matrix = []
        if not len(self.matrix) == len(m2.matrix):
            raise TypeError("nem kompatibilis mátrixok")
        for i in range(len(self.matrix)):
            new_matrix.append([])
            for j in range(len(self.matrix[i])):
                new_matrix[i].append(self.matrix[i][j] - m2.matrix[i][j])
        return matrix(new_matrix)

class vector(matrix):
    def __init__(self, vector):
        self.matrix = []
        for j in vector:
            self.matrix.append([j])
        self.row = len(self.matrix)
        self.column = len(self.matrix[0])
