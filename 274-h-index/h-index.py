class Solution:
    def hIndex(self, citations: List[int]) -> int:
        h = []
        citations.sort() #sort the array
        j = 0
        while True:
            temp = []
            for i in range(len(citations)):
                if j <= citations[i]:
                    temp.append(citations[i])

            if j <= len(temp):
                h.append(len(temp))
                j += 1
            else:
                break
        return j-1
            