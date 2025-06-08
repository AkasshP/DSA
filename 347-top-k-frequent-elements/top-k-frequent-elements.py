class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        temp = []
        for i in nums:
            if  count.get(i) == 0 or count.get(i):
                count[i] = count[i] + 1
            else:
                count[i] = 1
        
        new_count = sorted(count.items(), key=lambda item: item[1],reverse = True)
        for i in range(len(new_count[:k])):
            temp.append(new_count[i][0])
        return temp
