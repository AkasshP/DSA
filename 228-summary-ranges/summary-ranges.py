class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        final_interval = []
        i = 0
        while i < len(nums):
            interval = [] # every cycle reseting the interval array
            current = nums[i]
            j = i + 1 
            interval.append(current)
            while j < len(nums): 
                if current + 1 == nums[j]:
                    current = nums[j]
                    interval.append(current)
                    flag = True #iteration detection
                else:
                    break
                j += 1
            i = j - 1
            if len(interval) > 1:
                schedule = str(interval[0]) + '->' + str(interval[-1])
                final_interval.append(schedule)
            else:
                final_interval.append(str(interval[0]))
            i += 1
            
        return final_interval
