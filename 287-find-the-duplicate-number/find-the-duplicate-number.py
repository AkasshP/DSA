class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # visited = set()
        # for i in nums:
        #     if i not in visited:
        #         visited.add(i)
        #     else:
        #         return i
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = nums[0]
        #reusing the same fast pointer once the cycle is found. slow starts from again. fast resume from there 
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow

