class Solution {
    public int strStr(String haystack, String needle) {
        char[] char_arr = needle.toCharArray();
        char[] stack = haystack.toCharArray();
        int i = 0;
        int j;
        int x;
        int count = 0;
        boolean flag = true;

        if(char_arr.length <= stack.length)
        {
            while (i < stack.length)
            {
                if(stack[i] == char_arr[0]) //once match found
                {   
                    count = 1; // reset
                    j = 1;
                    x = i + 1;
                    flag = true; // reset the flag
                    while (j < char_arr.length && x < stack.length)
                    {
                        if(stack[x] == char_arr[j])
                        {
                            j += 1;
                            x += 1;
                            count += 1;
                        }
                        else 
                        {
                            flag = false;
                            break;
                        }
                    }
                    if(flag && count == char_arr.length)
                    {
                        return i;
                    }
                }
                i += 1;
            }
            if(count == char_arr.length)  return i;
            else return -1;
        }
        //edge case
        else 
        {
            return -1;
        }
    }

}