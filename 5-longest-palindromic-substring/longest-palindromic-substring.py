class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        for i in range(len(s)):
            if i + 1 < len(s):
                if s[i] == s[i+1]:
                    dp[i][i+1] = True

        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    # if the substring length is 2 or 3
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        # for length ≥4
                        dp[i][j] = dp[i+1][j-1]

        best_len = 1  
        best_start = 0  
        for i in range(n):
            for j in range(i, n):
                if dp[i][j]:
                    length = j - i + 1
                    if length > best_len:
                        best_len = length
                        best_start = i

        return s[best_start : best_start + best_len]

