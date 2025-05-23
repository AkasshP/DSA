class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        #rows and columns
        r = len(matrix)
        c = len(matrix[0])
        output = []
        visited = set()
        # right implementation
        def right(i,j):
            if len(visited) == r * c:
                    return
            if i >= r or j >= c or i <= -1 or j <= -1:
                    return down(i+1,j-1)
            else:
                if (i,j) not in visited:
                    output.append(matrix[i][j])
                    visited.add((i,j))
                    right(i,j+1)
                else:
                    down(i+1,j-1)
                    print('right-visit')

        # down implementation
        def down(i,j):
            if len(visited) == r * c:
                    return
            if i >= r or j >= c or i <= -1 or j <= -1:
                    return left(i-1,j-1)
            else:
                if (i,j) not in visited:
                    output.append(matrix[i][j])
                    visited.add((i,j))
                    down(i+1,j)
                else:
                    left(i-1,j-1)
                    print(i,j,'already visited down') 

        def left(i,j):
            if len(visited) == r * c:
                    return
            if i >= r or j >= c or i <= -1 or j <= -1:
                    return up(i-1,j+1)
            else:
                if (i,j) not in visited:
                    output.append(matrix[i][j])
                    visited.add((i,j))
                    left(i,j-1)
                else:
                    up(i-1,j+1)
                    print(i,j,'already visited left') 

        def up(i,j):
            if len(visited) == r * c:
                    return
            if i >= r or j >= c or i <= -1 or j <= -1:
                    return 
            else:
                if (i,j) not in visited:
                    output.append(matrix[i][j])
                    visited.add((i,j))
                    up(i-1,j)
                else:
                    right(i+1,j+1)
                    print(i,j,'up - visited already')
        
        i = j = 0
        right(i,j)
        return output
        # print(output,'cheking')
        
