class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r,c = len(matrix),len(matrix[0])
        # main = [[0] * c for _ in range(r)]
        # k = c - 1
        check = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                check[str(i)+str(j)] = False

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i == j:
                    continue
                elif check[str(i)+str(j)] == False:
                    matrix[i][j],matrix[j][i] =  matrix[j][i],matrix[i][j]
                    check[str(i)+str(j)] = True
                    check[str(j)+str(i)] = True
                else:
                    continue

        
        
        for i in range(len(matrix)):
            k = c - 1
            for j in range(len(matrix[i])): #two pointer techinique j is forward and k is backward once meets break the loop
                if k <= j:
                    break
                else:
                    matrix[i][j],matrix[i][k] = matrix[i][k],matrix[i][j]
                k -= 1
                
        


        
        

        