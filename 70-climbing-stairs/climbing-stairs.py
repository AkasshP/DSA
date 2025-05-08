class Solution:
    def climbStairs(self, n: int) -> int:
        # def stairs(n):
        #     if n == 1 or n == 0:   
        #         return 1
        #     else:
        #         return stairs(n-1) + stairs(n-2) 
        # res = stairs(n)
        # return res


        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:     
            list1 = [1,2]
            for i in range(3,n + 1):
                list1.append(list1[-1] + list1[-2])
            return list1[-1]
            

