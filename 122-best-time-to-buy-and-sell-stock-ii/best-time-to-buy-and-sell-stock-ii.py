class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        tp=[]
        j = 0
        i = 0
        if len(prices) == 2:
            if prices[1] > prices[0]:
                return prices[1] - prices[0]
        if len(prices) >= 3:
            while i < len(prices):
                    ptr = prices[i]
                    j = i + 1
                    k = j + 1
                    if len(prices) > j:
                        if ptr < prices[j]:
                            print('ptr-fixed',ptr)
                            initial_profit = prices[j] - ptr
                            if j and i and k == len(prices):
                                if prices[j] > prices[i]:
                                    updated_profit = initial_profit
                            else:
                                updated_profit = 0
                            
                            while len(prices) > k:
                                    if initial_profit  < prices[k] - ptr:
                                        if updated_profit < prices[k] - ptr:
                                            updated_profit = prices[k] - ptr
                                        else:
                                            break
                                        k += 1
                                    else:
                                        if initial_profit > updated_profit:
                                            updated_profit = initial_profit
                                            print(updated_profit,'initial profit')
                                            break
                                        else:
                                            break
                            tp.append(updated_profit)
                            i = k - 1
                        else:
                            pass
                        i += 1
                        print(i,'updating the i value')
                    else:
                        break
        result = sum(tp) if tp else 0 
        return result

                    
         
                
