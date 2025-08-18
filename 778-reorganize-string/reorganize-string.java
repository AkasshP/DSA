class CharFreq {
    char ch;
    int freq;
    
    CharFreq(char ch, int freq) {
        this.ch = ch;
        this.freq = freq;
    }
}

class Solution {
    public String reorganizeString(String s) {
        int n = s.length();
        HashMap<Character,Integer> freq = new HashMap<>();
        ArrayList<Character> str = new ArrayList<>();
        PriorityQueue<CharFreq> pq = new PriorityQueue<>((a, b) -> b.freq - a.freq); //max-heap
        for (char c: s.toCharArray())
        {
            freq.put(c,freq.getOrDefault(c, 0) + 1);
        }
        int max = 0;
        for (int v : freq.values()) max = Math.max(max, v);
        if (max > (n + 1) / 2) return "";

        for(Map.Entry<Character,Integer> x: freq.entrySet())
        {
            Character key = x.getKey();
            Integer value = x.getValue();
            pq.offer(new CharFreq(key,value));
        }
        //adding 1st element
        CharFreq prev = null;
        StringBuilder sb = new StringBuilder(n);
        while (!pq.isEmpty()) 
        {
           CharFreq current = pq.poll();
           sb.append(current.ch);
           current.freq--;
           
           if (prev != null) pq.offer(prev);

           prev = current.freq > 0 ? current :  null;

        }
        return sb.toString();
    }
}