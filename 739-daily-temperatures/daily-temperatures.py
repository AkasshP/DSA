class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # #brute force
        # def future_temp(temp,j):
        #     k = 1
        #     while j < len(temperatures):
        #         if temp < temperatures[j]:
        #             return k
        #         k += 1
        #         j += 1
        #     #if not appending in if then 0
        #     return 0


        # future = []
        # for i in range(len(temperatures)):
        #     day = future_temp(temperatures[i],i+1)
        #     future.append(day)
        # return future

        #optimised approach
        # future = []
        # for i in range(len(temperatures)):
        #     s = set(range(temperatures[i] + 1, 101))
        #     k = 1
        #     j = i + 1
        #     while j < len(temperatures):
        #         if temperatures[j] in s:  
        #             future.append(k)
        #             break
        #         j += 1
        #         k += 1
        #     if j >= len(temperatures):
        #         future.append(0)
        # return future
        #optimsed approach like
        day = [0] * (len(temperatures))
        stack  = []
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]: #storing just the indexes is brilliant idea in stack
                prev_index = stack.pop()
                day[prev_index] = i - prev_index
            stack.append(i) #adding the next temperature. rapidly or no stack
        return day
            

                
                

           
