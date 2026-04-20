class DynamicMatrix:
    def __init__(self):
        self.matrix=[]
    def add_row(self, row):
        if not self.matrix or len(row)==len(self.matrix[0]):
            self.matrix.append(row)
        else:
            print("рядок занадто довгий, або короткий")
    def add_column(self, column):
        if not self.matrix or len(column)==len(self.matrix):
            for n in range(len(self.matrix)):
                self.matrix[n].append(column[n])
    def total_sum(self):
        summa=0
        for n in self.matrix:
            summa+=sum(n)
        return summa
matrix=DynamicMatrix()
matrix.add_row([2,3,4,5,6,7,8])
matrix.add_row([2,3,4,5,6,7,8])
matrix.add_row([2,3,4,5,6,7,8])
matrix.add_column([1,2,3])
print(matrix.matrix)
print(matrix.total_sum())