class Solution {
    ArrayList<String> arr = new ArrayList<>();
    public List<String> generateParenthesis(int n) {
        // op and close
         generate(0,0,n,"");
         return arr;
    }
    public void generate(int op, int cb, int n, String ans)
    {
        if (ans.length() == n * 2)
        {
            arr.add(ans);
            return;
        }
        if (op < n)
        {
            generate(op+1,cb,n,ans+"(");
        }
        if(cb < op)
        {
            generate(op,cb+1,n,ans+")");
        }
    }
}