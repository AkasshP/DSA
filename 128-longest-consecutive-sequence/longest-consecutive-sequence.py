class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        new_arr = sorted(list(set(nums))) #removed duplicates
        if len(nums) > 1:
            t = new_arr[0] + 1
            max_count = 0
            cnt = 1
            for i in range(1,len(new_arr)):
                if t == new_arr[i]:
                    t = new_arr[i] + 1
                    cnt += 1
                else:
                    max_count = max(max_count,cnt)
                    cnt = 1 #reseting
                    t = new_arr[i] + 1

            max_count = max(max_count,cnt)
            return max_count
        elif len(nums) == 1:
            return 1
        else:
            return 0
                    
