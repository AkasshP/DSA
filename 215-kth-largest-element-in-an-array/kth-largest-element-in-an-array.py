import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxq=[]
        lar = 0
        for i in nums:
            heapq.heappush(maxq,-i)
        for i in range(k):
            lar = heapq.heappop(maxq)
        return -lar