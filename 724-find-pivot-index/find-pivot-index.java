class Solution {
    static void reverse(int[] a) {
    int i = 0, j = a.length - 1;
    while (i < j) {
        int tmp = a[i];
        a[i] = a[j];
        a[j] = tmp;
        i++;
        j--;
    }
    }
    public int pivotIndex(int[] nums) {
        int[] left = new int[nums.length];
        int[] right = new int[nums.length];
        left[0] = 0;
        int j = 1;
        for(int i = 0;i < nums.length; i++)
        {
            if (j < nums.length)
            {
            left[j] = left[j-1] + nums[i];
            j++;
            }
        }
        right[0] = 0;
        int k = 1;
        for(int i = nums.length - 1;i > -1; i--)
        {
            if (k < nums.length)
            {
            right[k] = right[k-1] + nums[i];
            k++;
            }
        }
        reverse(right);
        for(int i = 0; i < left.length;i++)
        {
            if (left[i] == right[i]) return i;
        }
        return -1;
    }
}