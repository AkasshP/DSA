class Solution {
    List<Integer> ar = new ArrayList<>();
    public int triangularSum(int[] nums) {
        //base case
        if (nums.length == 1) return nums[0];

        for (int i =0; i < nums.length; i++) ar.add(nums[i]); //
        return calc(ar);

    }
    public int calc(List<Integer> ar)
    {
        List<Integer> temp = new ArrayList<>();

        if (ar.size() == 1) return ar.get(0); // 

        for(int i = 0; i < ar.size() - 1; i++)
        {
            temp.add((ar.get(i) + ar.get(i+1)) % 10);
        }
        return calc(temp);
    }
}