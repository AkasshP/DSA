import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxq=[]
        lar = 0
        for i in nums:
            heapq.heappush(maxq,-i)
        for i in range(k-1):
            heapq.heappop(maxq)
        return -maxq[0]