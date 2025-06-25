class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left, right = 0, len(nums) - 1


        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid  

        rp = left  
        
        def binarySearch(arr,base):
            if len(arr) > 1:
                left,right = 0,len(arr) - 1
                while left < right:
                    if arr[left] == target:
                        return base + left
                    if arr[right] == target:
                        return base + right

                    mid = (left + right) // 2
                    if arr[mid] == target:
                        return base + mid
                    if arr[mid] > target:
                        right = mid
                    else:
                        left = mid + 1
                return -1
            else:
                if arr[0] == target:
                    return base 
                else:
                    return -1

        
        if rp == 0: #no rotation point then its sorted
            return binarySearch(nums, 0)
        if nums[rp] <= target <= nums[-1]:
            return binarySearch(nums[rp:], rp)
        else:
            return binarySearch(nums[:rp], 0)



                



        