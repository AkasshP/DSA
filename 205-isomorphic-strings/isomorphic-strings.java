class Solution {
    public boolean isIsomorphic(String s, String t) {
        HashMap<Character,Character> map = new HashMap<>();
        char[] ch = s.toCharArray();
        char[] ch2 = t.toCharArray();
        int i;
        for (i = 0; i < ch.length ; i++)
        {
            if (map.containsKey(ch[i]))
                {
                    if (map.get(ch[i]) == ch2[i]) continue;
                    else return false;
                    
                }
            else
                { 
                    if (map.containsValue(ch2[i])) return false;
                    
                    map.put(ch[i],ch2[i]);
                }
        }
        return true;
    }
}