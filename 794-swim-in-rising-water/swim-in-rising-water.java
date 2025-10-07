import java.util.*;

class Solution {
    PriorityQueue<Integer> pq = new PriorityQueue<>();
    Map<Integer,List<Integer>> idx = new HashMap<>();
    int r;
    int c;
    boolean[][] visited;
    int[][] grd;
    int cnt = 0;

    public int swimInWater(int[][] grid) {
        r = grid.length;
        c = grid[0].length;
        grd = grid;
        visited = new boolean[r][c];

        cnt = grd[0][0];

        List<Integer> arr = new ArrayList<>();
        Deque<List<Integer>> dq = new ArrayDeque<>();
        for(int i = 0; i < r; i++)
        {
            for(int j = 0; j < c; j++)
            {
                visited[i][j] = false;
                arr.addAll(Arrays.asList(i,j));
                idx.put(grid[i][j], new ArrayList<>(arr));
                arr.clear();
            }
        }

        dq.offer(Arrays.asList(0,0));
        visited[0][0] = true;

        while (!dq.isEmpty())
        {
            int lvl = dq.size();
            for(int i=0; i < lvl;i++)
            {
               List<Integer> temp = new ArrayList<>();
               temp = dq.poll();
               visited[temp.get(0)][temp.get(1)] = true;
               if (temp.get(0) == r - 1 && temp.get(1) == c - 1) return cnt;
               List<Integer> next = bfs(temp.get(0), temp.get(1)); 
               if (next != null) dq.offer(next); 
               // pass the recent arguments and catch the minimum elements in the place in the queue
            }
        }

        return cnt;
    }

    public List<Integer> bfs(int i, int j)
    {

        if (i + 1 < r && visited[i+1][j] != true)
        {
            pq.offer(grd[i+1][j]);
        }
        if (i - 1 > -1 && visited[i-1][j] != true)
        {
            pq.offer(grd[i-1][j]);
        }
        if (j + 1 < c && visited[i][j+1] != true)
        {
            pq.offer(grd[i][j+1]);
        }
        if (j - 1 > -1 && visited[i][j-1] != true)
        {
            pq.offer(grd[i][j-1]);
        }

        if (!pq.isEmpty())
        {
            int min = pq.poll();

            cnt = Math.max(cnt, min);

            return idx.get(min); // return the minimum list index
        }
        return null;
    }
}