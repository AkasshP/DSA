class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        m,n = len(grid),len(grid[0])
        max_area = 0
        

        def birection(i,j,c):
            if i >= m or j >= n or i < 0 or j < 0 or grid[i][j] == 0:
                return c
            grid[i][j] = 0 #marking
            c += 1
            c = birection(i+1,j,c) #down
            c = birection(i,j-1,c) #left
            c = birection(i,j+1,c) #right
            c = birection(i-1,j,c) #up
            return c
            

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    val = birection(i,j,0)
                    max_area = max(max_area,val)
        return max_area