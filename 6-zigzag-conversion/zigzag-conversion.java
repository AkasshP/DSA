
class Solution {
    public String convert(String s, int numRows) {
    
        int i;
        String[] main_str =  s.split("");
        int col = zigzagColumns(main_str.length,numRows);
        String[][] str = new String[numRows][col];
        int j = 0;
        int k = 0;

        if (numRows == main_str.length) return s; //edge case

        while(k < main_str.length)
        {
            for(i = 0; i < numRows; i++)
            {
                if (k >= main_str.length) break;
                str[i][j] = main_str[k++];
            }
            j++;
            for(i = numRows - 2 ; i > 0; i--)
            {
                if (k >= main_str.length) break;
                str[i][j] = main_str[k++];
                j++;
            }
        }
        StringBuilder main = new StringBuilder(main_str.length);
        for(String[] x: str)
        {
            StringBuilder temp = new StringBuilder(main_str.length);
            for(String y: x)
            {
               if (y != null) temp.append(y);
            }
            main.append(temp);
        }
        return main.toString();
    }
    public static int zigzagColumns(int n, int r) {
    // n = string length, r = numRows
    if (r <= 1 || n <= 1) return n;      

    int cycle = 2 * r - 2;               
    int full  = n / cycle;               
    int rem   = n % cycle;               
    int cols  = full * (r - 1);          
    int extra;

    if (rem == 0)  extra = 0;
    else if (rem <= r)  extra = 1;              
    else  extra = 1 + (rem - r);   

    return cols + extra;
    }
} 