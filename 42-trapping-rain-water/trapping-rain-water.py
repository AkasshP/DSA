class Solution:
    def trap(self, height: List[int]) -> int:
        # print(height)
        n = len(height)
        water = 0
        # for i in range(1,len(height)):
        #     left = max(height[:i])
        #     right = max(height[i:])
        #     water_loger = min(left,right)
            
        #     if (water_loger - height[i]) > 0 :
        #         water += (water_loger - height[i])
        
        # return water
        left = [0] * n
        right = [0] * n
        left[0] = height[0]
        for i in range(1,n):
            left[i] = max(left[i-1],height[i])
        right[n - 1] = height[-1] 
        for i in range(n-2,-1,-1):
            right[i] = max(right[i + 1],height[i])

        for i in range(len(height)):
            water += min(left[i],right[i]) - height[i]
        return water

        # print(left)
        # print(right)