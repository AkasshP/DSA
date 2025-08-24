class Solution {
    public int minCost(String colors, int[] neededTime) {
        
        char[] col = colors.toCharArray(); //to char array
        List<List<Integer>> main = new ArrayList<>(); //subarray initialization
        List<Integer> temp = new ArrayList<>(); // temp array
        char prev = col[0]; 
        int  total = 0;
        int j = 0;
        for (int i = 1; i < col.length; i++)
        {
            if (prev == col[i])
                {
                   temp.add(neededTime[j]);
                }
            else{
                temp.add(neededTime[j]);
                main.add(new ArrayList<>(temp)); // add the subarray 
                temp.clear();//reset the memory
            }
            prev = col[i]; //update the previous value
            j++;
        }
        temp.add(neededTime[neededTime.length - 1]); //adding last value
        main.add(temp);
        for (List<Integer> x: main)
        {
            if (x.size() > 1)
            {
            int sum = x.stream().mapToInt(Integer::intValue).sum();
            int maxTime = Collections.max(x);
            total += sum - maxTime;
            }

        }
        return total;
    }
}