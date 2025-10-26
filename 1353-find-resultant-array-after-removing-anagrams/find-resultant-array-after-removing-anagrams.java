class Solution {
    public List<String> removeAnagrams(String[] words) {
         Map<Integer, Map<String,Integer>> main_map = new HashMap<>();
         List<String> res = new ArrayList<>();
         Set<Map<String,Integer>> set = new HashSet<>();
         for(int i = 0; i < words.length; i++)
         {
            String[] temp = words[i].split("(?<=.)");
            Map<String,Integer> sub_map = new HashMap<>();
            int j = 0;
            while(j < temp.length)
            {
                sub_map.put(temp[j],sub_map.getOrDefault(temp[j],0) + 1);
                j++;
            }
            main_map.put(i,new HashMap(sub_map));
         }
         int j = 0;
         res.add(words[j]);
         for(int i = 1; i < words.length;i++)
         {
            if (main_map.get(j).equals(main_map.get(i))) main_map.remove(i);
        
            else{
                res.add(words[i]);
                j = i; // jump the pointer to that location
            }
         }
        return res;
    }
} 