import java.util.*;
class Solution {
    public int minDeletions(String s) {
        Map<Character,Integer> map = new HashMap<>();
        HashSet<Integer> main_set = new HashSet<>();
        for(char x: s.toCharArray()) map.put(x,map.getOrDefault(x,0) + 1);
        int del = 0;
        for(int i: map.values()) 
        {
            int x = i;
            while(x > 0 && main_set.contains(x))
            {
                x--;
                del++;
            }
            if (x > 0) main_set.add(x);
        }
        
    return del;
    }
}