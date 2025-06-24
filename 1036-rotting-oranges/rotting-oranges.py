from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        r,c = len(grid),len(grid[0])
        dq = deque()

        def top(i,j):
            if i >= r or i <= -1 or j >= c or j <= -1:
                return
            
            if  i - 1 >= 0 and grid[i-1][j] == 1:
                grid[i-1][j] = 2
                dq.append((i-1,j)) 

        def down(i,j):
            if i >= r or i <= -1 or j >= c or j <= -1:
                return
            
            if i + 1 < r and grid[i+1][j] == 1:
                grid[i+1][j] = 2
                dq.append((i+1,j)) 

        def left(i,j):
            if i >= r or i <= -1 or j >= c or j <= -1:
                return

            if j-1 >= 0 and grid[i][j-1] == 1:
                grid[i][j-1] = 2
                dq.append((i,j-1)) 
    

        
        def right(i,j):
            if i >= r or i <= -1 or j >= c or j <= -1:
                return
            
            if j+1 < c and grid[i][j+1] == 1:
                grid[i][j+1] = 2
                dq.append((i,j+1)) 


        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    dq.append((i,j))

        mint = 0
        while dq:
            for i in range(len(dq)):
                i,j = dq.popleft()
                top(i,j)
                down(i,j)
                left(i,j)
                right(i,j)

            mint += 1
        return -1 if any(1 in row for row in grid) else (mint - 1 if mint else mint)

