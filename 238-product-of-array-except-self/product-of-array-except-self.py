class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #brute force like multipying all elements in an array,each turn and then we are avoiding the elements which are present in the array.
        prd = [1] * len(nums)
        left = [1] * len(nums)
        right = [1] * len(nums)
        for i in range(1,len(nums)):
            left[i] = left[i-1] * nums[i-1]
        for i in range(len(nums) - 2,-1,-1):
            right[i] = right[i+1] * nums[i+1]
        k = 0
        for i,j in zip(left,right):
            prd[k] = i * j
            k += 1
        return prd
        #simple brute force
        # for i in range(len(nums)):
        #     prd[i] = int(reduce(lambda acc,x: acc * x,nums[:i] + nums[i+1:],1))
        # return prd