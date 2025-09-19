class Solution {
    public int candy(int[] ratings) {
        int[] arr = new int[ratings.length];
        int[] bw = new int[ratings.length];
        int[] newarr = new int[ratings.length];
        Arrays.fill(arr,1);
        Arrays.fill(bw,1);
        int j = 1;
        while (j < arr.length)
        {
            if (ratings[j]  > ratings[j-1])
            {
                arr[j] = arr[j-1] +  1;
            }
        j++;
        }
        j = bw.length - 2; // reset the memory
        while (j >= 0)
        {
            if (ratings[j] > ratings[j+1])
            {
                bw[j] = bw[j+1] +  1;
            }
        j--;
        }
        for(int i = 0; i < ratings.length; i++) 
        {
            newarr[i] = Math.max(arr[i],bw[i]);
        }
        System.out.println(Arrays.toString(arr));
        return Arrays.stream(newarr).sum();
    } 
}