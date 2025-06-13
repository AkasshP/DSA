from collections import deque
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # substr = []
        # i = 0
        # j = 1
        # length_str = 0
        # temp_k = k

        # def similarity(temp_k,s,substr,i,j):
        #     while temp_k != 0:
        #         if substr:
        #             char = substr[0]
        #             substr.append(char)
        #             temp_k -= 1
        #     return substr,temp_k


        # while i < len(s):

        #     if not substr:
        #         substr.append(s[i])
        #     if j >= len(s):
        #         break #because no need of re-iterating we are the end of s. no need of i loop
        #     while j < len(s):
        #         if s[j] in tuple(substr):
        #             substr.append(s[j])
        #         else: 
        #             substr,temp_k = similarity(temp_k,s,substr,i,j)

        #             #checking the length of the string everytime
        #             print(substr,'checking')
        #             length_str = max(length_str,len(substr)) 

        #             if temp_k == 0: #once the k is used completely
        #                 i += 1 #moving the window
        #                 j = i + 1 #reintiating the next to i
        #                 temp_k = k # again giving new k values to temp_k
        #                 substr.clear() #resetting for new_string

        #         j += 1
        # print(length_str,'length_str')

        def max_freq(freq):
            return max(freq.values())


        i = 0
        j = 1
        dq = deque() # window
        char_freq = {}
        if s: #intially
            dq.append(s[i])
            char_freq[s[i]] = 1
            length = 1

        while i < len(s) and j < len(s):
            dq.append(s[j])
            char_freq[s[j]] = char_freq.get(s[j], 0) + 1

            while len(dq) - max_freq(char_freq) > k:
                char = dq.popleft()
                char_freq[char] -= 1
                i += 1  # left shrink
        
            length = max(length, len(dq))
            j += 1
        return length
            