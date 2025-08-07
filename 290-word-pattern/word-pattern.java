class Solution {
    public boolean wordPattern(String pattern, String s) {
        pattern = pattern.trim(); 
        int i = 0;
        char ch;
        String[] words = s.split(" ");
        char[] char_arr = pattern.toCharArray();
        HashMap<Character, String> map = new HashMap<>();

        if (char_arr.length != words.length) {
            return false;
        }

        for (String x : words) {
            ch = char_arr[i];
            System.out.println(ch);  // For debugging
            if (map.containsKey(ch)) {
                if (!map.get(ch).equals(x)) {
                    return false;
                }
            } else {
                if (map.containsValue(x)) {
                    return false;
                }
                map.put(ch, x);
            }
            i++;
        }
        return true;
    }
}
