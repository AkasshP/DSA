import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles) 
        result = high
        while low <= high:
            t_hours = 0
            mid = ( low + high ) // 2
            for pile in piles:
                t_hours += math.ceil(pile / mid)
            if t_hours <= h:
                result = mid
                high = mid - 1 
            else:
                low = mid + 1
        return result


