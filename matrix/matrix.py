class Matrix(object):

    def __init__(self, matrix_string):
        self.matrix = [[int(digit) for digit in str_row.split(" ") if digit.isdigit()] for str_row in matrix_string.splitlines()]

    def row(self, index):
        return self.matrix[int(index-1)]

    def column(self, index):
        return [row[index-1] for row in self.matrix]
        
