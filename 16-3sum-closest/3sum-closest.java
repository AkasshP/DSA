class Solution {
    public int threeSumClosest(int[] nums, int target) {
        int n = nums.length;
        Arrays.sort(nums); //sort it
        int res = nums[0]+nums[1]+nums[2];
        if(n >= 3)
        {
            for(int i = 0; i < n - 2; i++)
            {
                int left = i + 1, right = n - 1;
                
                while(left < right)
                {
                    int sum = nums[i] + nums[left] + nums[right];
                    if (Math.abs(sum-target) < Math.abs(res-target)) res = sum;
                    if (target == sum) return target;
                    else if (sum < target) left ++;
                    else right--;
                }
            }
        }
    return res;
    }
}