class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        visited = set()
        result = []
        def combinations(arr,start):
            if len(arr) == k:
                result.append(arr[:])
                return 

            for i in range(start,n+1):
                arr.append(i)
                combinations(arr,i+1)
                arr.pop()

        
        combinations([],1)



        return result
            