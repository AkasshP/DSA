class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        m, n = len(grid), len(grid[0])
        def dfs(i,j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
               return
            grid[i][j] = '0' 
            dfs(i+1,j) #down
            # print(grid,'recursion')
            dfs(i,j+1) #right
            dfs(i-1,j) #up
            dfs(i,j-1) #left
            
        island_count = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i, j)  
                    island_count += 1  
        
        return island_count
            
            
            