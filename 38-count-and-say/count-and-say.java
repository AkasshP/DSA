class Solution {
    public String countAndSay(int n) {
        //base case
        if (n == 1) return "1";


        List<String> arr =  new ArrayList<>();
        // n > 1
        arr.add("11");
        for(int i = 2; i < n; i++)
        {
            String s = arr.remove(arr.size() - 1); // pops the last element
            System.out.println(s+"string");
            String[] srr = s.split("(?<=.)");
            arr.add(cluster(srr));
        }
        return arr.get(0);

    }

    public String cluster(String[] s)
    {
        List<String> temp = new ArrayList<>();//reset it
        String prev = s[0];
        int cnt = 1;
        for(int i = 1; i < s.length; i++)
        {

            if (prev.equals(s[i])) cnt++;
            else 
            {
                temp.add((String.valueOf(cnt) + String.valueOf(prev)));
                cnt = 1;// reset the value 
            }
            prev = s[i]; //set the previous value
        }
        if (s.length >= 2)
        {
        if (!prev.equals(s[s.length - 2]))
        {
            temp.add((String.valueOf(1) + String.valueOf(prev)));
        }
        }
        if (cnt > 1)// left over cnt
        {
            String res = (String.valueOf(cnt) + String.valueOf(prev));
            temp.add(res);
        }
        System.out.println(temp);
        return String.join("",temp);
        
    }
}