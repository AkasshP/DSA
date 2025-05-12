class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #it works like maintain two pointers
        substr = set()
        i = 0
        count = 0
        if s:
            while i < len(s):
                substr.add(s[i])
                j = i + 1
                while j < len(s):
                    if s[j] in substr: 
                        print(substr,'substring')
                        count = max(count,len(substr))
                        substr.clear()
                        break
                    else:
                        substr.add(s[j])
                    j += 1

                if j > len(s): # only adding may substring sequence
                    count = max(count,len(subtr)) #it will only shrink no use to checking again
                    break
                i += 1
            if substr:
                count = max(count,len(substr))
            return count
        else:
            return 0
            
            
            