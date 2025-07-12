class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
            dp = [0] * (amount + 1)
            res = float('inf')
            for i in range(1,amount+1):
                for j in coins:
                    if i - j >= 0 and dp[i - j] != -1:
                        res = min(dp[i - j],res)
                    
                if res == float('inf'):
                    dp[i] = -1
                else:
                    dp[i] = res + 1
                res = float('inf')
            return dp[-1]
            

