class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dict1 = set(wordDict)
        # result=[]
        # i = 0
        # for j in range(1,len(s)+1):
        #     if s[i:j] in dict1:
        #         result.append(s[i:j])
        #         i = j
        # print(result)
        # m_str = ''.join(result)
        # return m_str == s 
        # Convert wordDict to a set for O(1) "in" checks:
        dict1 = set(wordDict)            # e.g. {"aaa", "aaaa"}
        
        n = len(s)
        # dp[i] will be True if s[0:i] can be segmented by words in dict1
        dp = [False] * (n + 1)
        
        # Base case: empty string (prefix of length 0) is "segmented"
        dp[0] = True
        
        # Now fill dp[1], dp[2], ..., dp[n]
        for i in range(1, n + 1):
            # We try every possible split: s[0:j] | s[j:i]
            # If s[0:j] was segmentable (dp[j] == True) and s[j:i] is in dict1,
            # then s[0:i] is segmentable, so dp[i] = True.
            for j in range(i):  # j goes from 0, 1, 2, …, i−1
                if dp[j] and s[j:i] in dict1:
                    dp[i] = True
                    break  # no need to check smaller j once we know dp[i]=True
        
        # dp[n] tells us if s[0:n] == s can be segmented
        return dp[n]


        # word_set = set(wordDict)           
        # n = len(s)
        # dp = [False] * (n + 1)             
        # dp[0] = True                       

        # for i in range(n):
        #     if not dp[i]:
        #         continue                   
        #     for j in range(i + 1, n + 1):
        #         if s[i:j] in word_set:    
        #             dp[j] = True
        #         print(dp,'dynamic')
        # return dp[n]