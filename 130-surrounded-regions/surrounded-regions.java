class Solution {
    public int row;
    public int col;
    public Set<List<Integer>> set= new HashSet<>();
    public void solve(char[][] board) {
        row = board.length;
        col = board[0].length;
        for(int i = 0; i < board.length; i++)
        {
            for(int j = 0; j < board[i].length; j++)
            {
                // once found !!!
                if(board[i][j] == 'O')
                {   
                    //calculate all safe points
                    if (i == 0 || i == row - 1 || j == 0 || j == col - 1) 
                    {
                       safepoints(i,j,board);
                    }
                }
            }
        }
        System.out.println(set);
        for(int i = 0; i < board.length; i++)
        {
            for(int j = 0; j < board[i].length; j++)
            {
                // once found !!!
                if(board[i][j] == 'O' && !set.contains(Arrays.asList(i,j))) dfs(i,j,board);
            }
        }
        
    }
    public void dfs(int i,int j,char[][] board)
    {

        if (i < 0 || i >= row || j < 0 || j >= col || board[i][j] != 'O') return;

        board[i][j] = 'X'; //mark it

        dfs(i+1,j,board); //down
        dfs(i-1,j,board); //up
        dfs(i,j+1,board); //right
        dfs(i,j-1,board); //left

    }
    public void safepoints(int i, int j, char[][] board) {
        if (i < 0 || i >= row || j < 0 || j >= col) return;
        if (board[i][j] != 'O') return;
        List<Integer> key = Arrays.asList(i, j);
        if (set.contains(key)) return;

        set.add(key);

        safepoints(i + 1, j, board);
        safepoints(i - 1, j, board);
        safepoints(i, j + 1, board);
        safepoints(i, j - 1, board);
    }
}