class Solution {
    public String gcdOfStrings(String str1, String str2) {
        //brute force
        // String str,max;
        // StringBuilder sb = new StringBuilder();
        // if (str1.length() < str2.length()) 
        // { 
        //     str = str1;
        //     max = str2;
        // }
        // else 
        // {   
        //     str = str2;
        //     max = str1;
        // }
        // for (int i = 0; i < str.length(); i++) {
        //     if (sb.length() == 0) sb.append(str.charAt(i));
        //     else{
        //     int y = i;
        //     int x = 0;
        //     int cnt = 0;

        //     while (sb.length() != 0 && x < sb.length() && y < str.length()) {
        //         if (sb.charAt(x) == str.charAt(y)) {
        //             cnt += 1;
        //             x += 1;
        //             y += 1;
        //         } else {
                
        //             break;
        //         }
        //     }
        //     if (cnt == sb.length()) break;
        //     if (i < str.length()) sb.append(str.charAt(i));
        //     }
        // }
        // // System.out.println(sb.toString());
        // // return "ABC";
        // int x = 0;
        // for(int i = 0; i < max.length(); i++)
        // {
        //     if (x == sb.length())
        //     {
        //         //final check
        //        return sb.charAt(0) == max.charAt(i) ? sb.toString() : "";
        //     }

        //     else if (sb.charAt(i) == max.charAt(i)) x += 1;

        //     else return "";
        // }
        // return "";

    if (!(str1 + str2).equals(str2 + str1)) return "";

    BiFunction<Integer,Integer,Integer> gcd = (a,b) ->
    {
        while (b != 0) {
        int t = a % b;
        a = b;
        b = t;
    }
    return a;
    };
    int g = gcd.apply(str1.length(), str2.length());
    return str1.substring(0, g);  
    }
}