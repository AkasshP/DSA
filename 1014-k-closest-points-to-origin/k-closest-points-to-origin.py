import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hq = []
        for i in points:
            x,y = i
            res = x * x + y * y
            heapq.heappush(hq,(res,i))

        main_box = []
        while k:
           x,[y,z] =  heapq.heappop(hq)
           main_box.append([y,z])
           k -= 1
        
        return main_box

