class Solution {
    public int[] sortedSquares(int[] nums) {
        int[] arr = new int[nums.length];
        for (int x=0; x < nums.length; x++)
        {
            arr[x] = nums[x] * nums[x];
        }
        Arrays.sort(arr);
        return arr;
    }
}