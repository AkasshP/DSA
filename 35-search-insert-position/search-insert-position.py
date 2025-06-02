class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        new_arr = []
        def bs(num):
            mid = len(num) // 2
            if num[mid] == target:
                return nums.index(num[mid])
            else:
                if num[mid] > target:
                    if len(num) == 1:
                        print(num[mid],'mid checking')
                        idx = nums.index(num[mid])
                        if idx == 0:
                            return idx
                        return idx + 1
                    new_arr = num[:mid]
                    return bs(new_arr)
                else:
                    if len(num) == 1:
                        idx = nums.index(num[mid])
                        return idx + 1
                    new_arr = num[mid:]
                    print(new_arr)
                    return bs(new_arr)

                    
                
        return bs(nums)
