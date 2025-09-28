class Solution {
    public int largestPerimeter(int[] nums) {
        Arrays.sort(nums);
        List<Integer> arr = new ArrayList<>();
        for(int i=0; i < nums.length - 2; i++)
        {
            if (nums[i] + nums[i+1] > nums[i+2]) arr.add(nums[i] + nums[i+1] + nums[i+2]);
        }
        return arr.isEmpty() ? 0 : Collections.max(arr);
    }
}