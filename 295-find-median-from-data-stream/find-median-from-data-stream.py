import heapq
import math
class MedianFinder:

    def __init__(self):
        self.hq = []

    def addNum(self, num: int) -> None:
        bisect.insort(self.hq, num)

    def findMedian(self) -> float:
            if len(self.hq) % 2 == 0:
                i = len(self.hq) / 2
                return (self.hq[int(i)-1] + self.hq[int(i)])/ 2
            else:
                idx = len(self.hq) // 2
                return self.hq[idx]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()