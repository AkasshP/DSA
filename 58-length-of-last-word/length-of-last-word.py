class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        arr = []
        temp = []
        for i in s:
            if i == ' ':
                arr.append(''.join(temp))
                temp = []
                continue
            temp.append(i)

        if temp:
            arr.append(''.join(temp))
        
        stripped = list(filter(lambda x:x != '',arr))
        return len(stripped[-1])

