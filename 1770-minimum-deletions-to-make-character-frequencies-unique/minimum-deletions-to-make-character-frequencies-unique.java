import java.util.*;
class Solution {
    public int minDeletions(String s) {
        char[] ch = s.toCharArray();
        Map<Character,Integer> map = new HashMap<>();
        HashSet<Integer> main_set = new HashSet<>();
        ArrayList<Integer> repetion_list = new ArrayList<>();
        for(char x: ch) map.put(x,map.getOrDefault(x,0) + 1);
        int min_del = 0;
        System.out.println(map+"map");
        for(int x: map.values()) 
        {
            if (!main_set.contains(x)) main_set.add(x);
            else repetion_list.add(x);
        }
        // System.out.println(repetion_list+"repetion");
        // System.out.println(main_set+"set");
        for(int x:repetion_list)
        {
            int temp = x; // store the main copy
            while (main_set.contains(x) && x != 0)
            {
                x--; //decrement until new value found in set
            }
            
            min_del += (temp - x != 0 ? temp - x : temp); 
            if (x != 0) main_set.add(x);//update the minimum val in min_del
            
        }
    return min_del;
    }
}