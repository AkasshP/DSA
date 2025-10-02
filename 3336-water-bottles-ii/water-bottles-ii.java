class Solution {
    public int maxBottlesDrunk(int numBottles, int numExchange) {
        int bt_drnk = 0;
        int bt_empty = 0;
        while (bt_empty >= 0 || numBottles >= 0)
        {
            if (bt_empty == 0) {
                if (numBottles == 0) return bt_drnk;
                bt_empty = numBottles;
                bt_drnk += numBottles;
                numBottles = 0; // completely used 
            }
            if (bt_empty - numExchange >= 0)  {
                bt_empty -= numExchange;
                numExchange += 1;
                numBottles += 1;
            }
            else{
                if((bt_empty + numBottles) - numExchange >= 0)
                {
                    bt_drnk += numBottles;
                    bt_empty += numBottles;
                    numBottles = 0; //used completely
                }
                else
                {
                    return numBottles != 0 ? bt_drnk + numBottles : bt_drnk; // if there were any remaining it was there
                }
            }

        }
        return bt_drnk;
    }
}