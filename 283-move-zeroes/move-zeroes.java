import java.util.*;
class Solution {
    public void moveZeroes(int[] nums) {
        int count = 0;
        for (int x: nums)
        {
            if (x == 0) count++;

        }
        while (count != 0)
        {
            for (int i=0; i < nums.length; i++)
            {
                if (nums[i] == 0) 
                {
                    if (i + 1 < nums.length)
                    {
                        nums[i] = nums[i+1];
                        nums[i+1] = 0;
                    }
                }
            }
            count--;
        }
    }
}