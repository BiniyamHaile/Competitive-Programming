class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.matrixSum = [[0 for i in range(len(matrix[0]))] for i in range(len(matrix))]
        self.rowSum = 0
        self.columnlen = len(matrix[0])-1

        for row in range(len(matrix)):
            for column in range(len(matrix[0])):
                if column == 0 and row == 0:
                    self.rowSum += matrix[row][column]
                    self.matrixSum[row][column] = self.matrix[row][column]
                    
                elif row == 0:
                    self.rowSum += matrix[row][column]
                    self.matrixSum[row][column] = self.matrixSum[row][column-1] + self.matrix[row][column]
                    
                elif column == 0:
                    #print(" self.matrixSum[row-1][column]   is : " ,  self.matrixSum[row-1][column] )
                    self.rowSum += matrix[row][column]
                    self.matrixSum[row][column] = self.matrixSum[row-1][column] + self.matrix[row][column]
                    
                else :  
                    self.rowSum += matrix[row][column]
                    self.matrixSum[row][column] = self.matrixSum[row-1][column]  + self.rowSum 
            self.rowSum = 0

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1 == row2 and col1 == col2 :
            return self.matrix[row1][col1]
        if col1 == 0 and row1 == 0:
            return (self.matrixSum[row2][col2])
        elif col1 == 0 and row1!= 0:
            return self.matrixSum[row2][col2] - self.matrixSum[row1-1][col2]
        elif row1 == 0:
            return (self.matrixSum[row2][col2]-self.matrixSum[row2][col1-1])
        elif row1 !=0:
            return self.matrixSum[row2][col2]-self.matrixSum[row2][col1-1]- (self.matrixSum[row1-1][col2] - self.matrixSum[row1-1][col1-1])
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)