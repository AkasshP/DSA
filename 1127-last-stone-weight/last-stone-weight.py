import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        arr = []
        for i in stones:
            heapq.heappush(arr,-i)

        if len(arr) == 1:
            return -(arr[0])
        else:
            if not arr:
                return 0

        while arr:
            if len(arr) >= 2:
                x = -(heapq.heappop(arr))
                y = -(heapq.heappop(arr))
                if x == y:
                    pass
                if x != y:
                    if x <= y:
                        heapq.heappush(arr,-(y - x))
                    else:
                        heapq.heappush(arr,-(x - y))
            else:
                if arr:
                    return -(arr[0])
                
        if not arr:
            return 0
