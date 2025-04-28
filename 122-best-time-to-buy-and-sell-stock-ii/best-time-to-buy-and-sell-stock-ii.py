class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        tp=[]
        j = 0
        i = 0
        if len(prices) == 2: #use case for two value
            if prices[1] > prices[0]:
                return prices[1] - prices[0]
        if len(prices) >= 3:
            while i < len(prices):
                    ptr = prices[i]
                    j = i + 1
                    k = j + 1
                    if len(prices) > j:
                        if ptr < prices[j]:
                            print('ptr-fixed',ptr) # ptr fixed for the price level checking
                            initial_profit = prices[j] - ptr
                            if j and i and k == len(prices):
                                if prices[j] > prices[i]:
                                    updated_profit = initial_profit
                            else:
                                updated_profit = 0
                            
                            while len(prices) > k:
                                    if initial_profit  < prices[k] - ptr:
                                        if updated_profit < prices[k] - ptr:
                                            updated_profit = prices[k] - ptr #updating the profit value
                                        else:
                                            break
                                        k += 1
                                    else:
                                        if initial_profit > updated_profit:
                                            updated_profit = initial_profit
                                            print(updated_profit,'initial profit')# intial profit
                                            break
                                        else:
                                            break
                            tp.append(updated_profit)
                            i = k - 1 #skipping the iteration value
                        else:
                            pass
                        i += 1
                        #iterating the value
                    else:
                        break
        result = sum(tp) if tp else 0 
        return result

                    
         
                
