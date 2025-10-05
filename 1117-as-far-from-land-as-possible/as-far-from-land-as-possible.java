class Solution {
    public int maxDistance(int[][] grid) {
        int r = grid.length;
        int c = grid[0].length;
        boolean[][] visited =  new boolean[r][c];
        boolean has0 = false;
        boolean has1 = false;
        for(int i = 0; i < r; i++)
        {
            for(int j = 0; j < c;j++)
            {
                if (grid[i][j] == 0)
                {
                    has0 = true;
                }
                if (grid[i][j] == 1)
                {
                    has1 = true;
                }
                visited[i][j] = false; // initially set false
            }
        }

        if (!has0 || !has1) return -1;

        Deque<List<Integer>> dq = new ArrayDeque<>();
        for (int i = 0; i < r; i++)
        {
            for(int j = 0; j < c; j++)
            {
                if (grid[i][j] == 1)
                    {
                        dq.offer(Arrays.asList(i,j));
                    }
            }
        }
        int cnt = 0;
        int x,y;
        while (!dq.isEmpty())
        {
            cnt += 1;
            int lvl = dq.size();
            for(int i = 0; i < lvl; i++)
            {
                List<Integer> ar = new ArrayList(dq.poll());
                x = ar.get(0);
                y = ar.get(1);
                if (x + 1 < r) if((grid[x + 1][y] == 0) && (visited[x+1][y] != true)) {
                    dq.offer(Arrays.asList(x + 1, y)); 
                    visited[x+1][y] = true;
                }
                if (x - 1 > - 1) if((grid[x - 1][y] == 0 ) && (visited[x - 1][y] != true)){
                    dq.offer(Arrays.asList(x - 1, y)); 
                    visited[x-1][y] = true;
                } 
                if (y + 1 < c) if((grid[x][y + 1] == 0 ) && (visited[x][y + 1] != true)) 
                {
                    dq.offer(Arrays.asList(x, y + 1)); 
                    visited[x][y+1] = true;
                }
                if (y - 1 > - 1) if((grid[x][y - 1] == 0 ) && (visited[x][y - 1] != true)) 
                {
                    dq.offer(Arrays.asList(x, y - 1));
                    visited[x][y-1] = true;
                }
            }
        }
        return cnt - 1;
    }
}