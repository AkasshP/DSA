class Solution:
    def reverseWords(self, s: str) -> str:
        new_str = ''
        temp = []
        final_str = ''
        for i in range(len(s) - 1,-1,-1):
            if s[i] == ' ':
                new = list(new_str)
                temp.append(''.join(new[::-1]) + ' ')
                new_str = ''
            else:
                new_str = new_str + s[i]
        #last string appending method
        if new_str:
            new = list(new_str)
            temp.append(''.join(new[::-1]))
        
        cleaned = list(filter(lambda x: x != " ",temp))
        final_str = ''.join(cleaned)
        if final_str[-1] == ' ':
            return final_str[:len(final_str) - 1]
        else:
            return final_str
        