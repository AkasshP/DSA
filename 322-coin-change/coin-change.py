class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #greedy
        # n = len(coins)
        # few_coins =  []
        # if n < 2: #base case
        #     if amount:
        #         if amount % coins[0] == 0:
        #             return amount // coins[0] 
        #         else:
        #             return -1
        #     else:
        #         return 0
        
        # else:
            # updated_amount = amount
            # coin_arr = []
            # def coincalc(coins,amount,updated_amt,coin_arr):
            #     if coins:
            #         max_ = max(coins)
            #         if updated_amt % max_ == 0:
            #             max_coins = updated_amt // max_ 
            #             few_coins = coin_arr +  [max_] * max_coins
            #             if sum(few_coins) == amount:
            #                 return few_coins
            #             else:
            #                 newarr = list(filter(lambda x: x != max_,coins))
            #                 updated_amt = amount - sum(few_coins)
            #                 return coincalc(newarr,amount,updated_amt,few_coins)
            #         else:
            #             max_coins = updated_amt // max_ # maximum coins can be used
                        
            #             if max_coins: #no max_coins found then go with the remaining
            #                 few_coins = coin_arr + [max_] * max_coins
            #             else:
            #                 few_coins = coin_arr

            #             if sum(few_coins) == amount:
            #                 return few_coins
            #             else:
            #                 newarr = list(filter(lambda x: x != max_,coins))
            #                 updated_amt = amount - sum(few_coins)
            #                 return coincalc(newarr,amount,updated_amt,few_coins)
            #     else:
            #         if sum(coin_arr) < amount:
            #             return coin_arr

            # few_currency = coincalc(coins,amount,updated_amount,coin_arr)
            # if amount:
            #     if few_currency:
            #         return len(few_currency)
            #     else:
            #         return -1
            # else: 
            #     return 0
            dp = [amount + 1] * (amount + 1)
            dp[0] = 0
            for x in range(1,amount + 1):
                for i in coins:
                        if x - i >= 0:
                            dp[x] = min(dp[x], 1 + dp[x - i])
                        
            return dp[amount] if dp[amount] != amount + 1 else -1
                    

        
                    
            
              