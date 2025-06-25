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
        if rp:
            left = nums[:rp]
            right = nums[rp:]
        

        def binarySearchR(arr):
            if len(arr) > 1:
                left,right = 0,len(arr) - 1
                while left < right:
                    if arr[left] == target:
                        return rp + left
                    if arr[right] == target:
                        return rp + right

                    mid = (left + right) // 2
                    if arr[mid] == target:
                        return rp + mid
                    if arr[mid] > target:
                        right = mid
                    else:
                        left = mid + 1
                return -1
            else:
                if arr[0] == target:
                    return rp + 0
                else:
                    return -1

        def binarySearchL(arr):
            if len(arr) > 1:
                left,right = 0,len(arr) - 1
                while left < right:
                    if arr[left] == target:
                        return left
                    if arr[right] == target:
                        return right

                    mid = (left + right) // 2
                    if arr[mid] == target:
                        return mid

                    if arr[mid] > target:
                        right = mid
                    else:
                        left = mid + 1
                return -1
            else:
                if arr[0] == target:
                    return 0
                else:
                    return -1
        
        if rp: #no rotation point then. its sorted
            if right[0] <= target <= right[-1]:
                return binarySearchR(right)
            else:
                return binarySearchL(left)
        else: # apply binary search
            return binarySearchL(nums)



                



        