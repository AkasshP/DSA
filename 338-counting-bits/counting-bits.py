class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        for i in range(len(dp)):
            res = bin(i)
            dp[i] = res[2:]
        for i in range(len(dp)):
            dp[i] = len(list(filter(lambda x: x == '1',list(dp[i]))))
        return dp