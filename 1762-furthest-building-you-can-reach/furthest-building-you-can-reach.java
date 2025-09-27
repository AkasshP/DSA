import java.util.*;
class Solution {
    public int furthestBuilding(int[] heights, int bricks, int ladders) {
        // Edge Cases 
        int ptr = 0;
        int i;
        if (bricks == 0 && ladders == 0)
        {
            for(i = 1; i < heights.length; i++)
            {
                if (heights[ptr] > heights[i]) 
                {
                    ptr++;
                    continue;
                }
                else return i - 1;
            }
            return i - 1; 
        }

        PriorityQueue<Integer> heap = new PriorityQueue<>(Comparator.reverseOrder());// to track the highest usage
        int result;
        for(i = 1; i < heights.length;i++)
        {

            if (heights[ptr] >= heights[i]) 
            {
                ptr++;
                continue;
            }

            if (bricks == 0 && ladders == 0 ) return i - 1; // base case

            else 
            {
                result = heights[ptr] - heights[i];
                heap.offer(Math.abs(result));
                bricks += result; 
                if (bricks < 0){
                    if (ladders != 0) //make sure ladder does count
                    {
                        int num =  heap.poll(); // return the maximum used bricks
                        ladders -= 1;
                        bricks += num; // swapping back with bricks 
                    }
                    else return i - 1;
                }
            }
            ptr++;
        }
        return heights.length - 1; // suppose if the till last end it touches
    }
}