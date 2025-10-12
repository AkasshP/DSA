class Solution {
    public String mergeAlternately(String word1, String word2) {
        int remain = Math.abs(word1.length() - word2.length());
        int max = Math.max(word1.length(), word1.length());
        if (remain != 0) remain += max;
        else remain = word1.length();
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < remain; i++)
        {
            if (i < word1.length()) sb.append(word1.charAt(i));
            if (i < word2.length()) sb.append(word2.charAt(i));
        }
        return sb.toString();
    }
}
