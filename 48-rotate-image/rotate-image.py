class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r,c = len(matrix),len(matrix[0])
        main = [[0] * c for _ in range(r)]
        k = c - 1
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                main[i][k-j] = matrix[j][i]

        for i in range(len(main)):
            for j in range(len(main[i])):
                matrix[i][j] = main[i][j]
                

        
        

        