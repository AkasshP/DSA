class Solution {
    public int numWaterBottles(int numBottles, int numExchange) {
        int emp = 0;
        int drnk = 0;
        while (emp >= 0)
        {
            System.out.println(drnk);
            if (emp == 0)
            {
                if (numBottles == 0)  return drnk;
                emp = numBottles;
                drnk += numBottles;
                numBottles = 0;
            }
            else if(emp - numExchange >= 0)
            {
                emp -= numExchange;
                numBottles += 1;
            }
            else if ((emp + numBottles) - numExchange >= 0)
            {
                drnk += numBottles;
                emp += numBottles;
                emp -= numExchange;
                numBottles = 1;
            }
            else return numBottles != 0 ? drnk + numBottles : drnk;
        }
        return drnk;
    }
}