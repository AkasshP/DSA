class Solution {
    public boolean wordPattern(String pattern, String s) {
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
