class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows,cols = len(matrix),len(matrix[0])
        dummy = [[0 for j in range(cols)] for i in range(rows)]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                dummy[i][j] = matrix[i][j]


        def transform(i,j,t):

            if i >= rows or j >= cols or i < 0 or j < 0:
                return 
            
            dummy[i][j] = 0 #mark it

            if t == 'down':
                transform(i+1,j,t) #go down

            if t == 'up':
                transform(i-1,j,t) #go up

            if t == 'left':
                transform(i,j-1,t) #go left

            if t == 'right':
                transform(i,j+1,t) #go right




        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0 :
                    transform(i+1,j,'down')
                    transform(i-1,j,'up')
                    transform(i,j+1,'right')
                    transform(i,j-1,'left')

        for i in range(len(dummy)):
            for j in range(len(dummy[i])):
                matrix[i][j] = dummy[i][j]
        

                