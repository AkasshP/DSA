import java.util.*;

class Solution {
    public List<Integer> findSubstring(String s, String[] words) {
        List<Integer> ans = new ArrayList<>();
        if (s == null || s.isEmpty() || words == null || words.length == 0) return ans;

        int wordLen = words[0].length();
        int needCount = words.length;
        int n = s.length();
        if (n < wordLen * needCount) return ans;

        // Build target frequencies
        Map<String, Integer> need = new HashMap<>();
        for (String w : words) need.put(w, need.getOrDefault(w, 0) + 1);

        // Try all starting offsets modulo wordLen
        for (int offset = 0; offset < wordLen; offset++) {
            // Build chunks for this offset (only full words)
            List<String> chunks = new ArrayList<>();
            for (int i = offset; i + wordLen <= n; i += wordLen) {
                chunks.add(s.substring(i, i + wordLen));
            }

            // Sliding window over chunk indices
            Map<String, Integer> have = new HashMap<>();
            int left = 0; // left and right are chunk indices
            for (int right = 0; right < chunks.size(); right++) {
                String w = chunks.get(right);

                if (!need.containsKey(w)) {
                    // reset window if a non-needed word appears
                    have.clear();
                    left = right + 1;
                    continue;
                }

                // include current word
                have.put(w, have.getOrDefault(w, 0) + 1);

                // pop from left while over-using some word
                while (have.get(w) > need.get(w)) {
                    String drop = chunks.get(left);
                    have.put(drop, have.get(drop) - 1);
                    left++;
                }

                // if window holds exactly words.length chunks, record start and slide by one
                if (right - left + 1 == needCount) {
                    int startIndex = offset + left * wordLen; // absolute index in s
                    ans.add(startIndex);

                    // pop one from left to look for overlapping matches
                    String drop = chunks.get(left);
                    have.put(drop, have.get(drop) - 1);
                    left++;
                }
            }
        }
        return ans;
    }
}
