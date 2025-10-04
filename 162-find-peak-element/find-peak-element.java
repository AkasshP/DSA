class Solution {
    public int findPeakElement(int[] nums) {

        if (nums.length == 1) return 0;
        int l = 0;
        int r = nums.length - 1;
        int mid = 0;
        
        while ( l <= r)
        {
            mid = l + (r - l) / 2;

            if (l == r) return mid;
            
            if (mid - 1 >= 0 && mid + 1 < nums.length)
            {
            if (nums[mid - 1] < nums[mid] && nums[mid] > nums[mid + 1]) return mid;
            else if (nums[mid - 1] > nums[mid]) r = mid;
            else l = mid + 1;
            }
            else
            {
                if (mid - 1 < 0) if (nums[mid] > nums[mid + 1]) return mid; else return mid + 1;
                if (mid + 1 > nums.length) if (nums[mid] > nums[mid - 1]) return mid; else return mid - 1;
            }
        }
        return mid;
    }
}