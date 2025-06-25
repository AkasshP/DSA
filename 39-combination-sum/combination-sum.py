class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        visited = set()
        new_arr = []
        def combinations(temp):
            
            if sum(temp) == target and tuple(sorted(temp)) not in visited:
                arr = sorted(temp)
                visited.add(tuple(arr))
                new_arr.append(arr)
                return

            for i in candidates:
                if i + sum(temp) <= target:
                    temp.append(i)
                    combinations(temp)
                    if temp:
                        temp.pop()
        
        
        for i in candidates:
            temp = []
            temp.append(i)
            combinations(temp)

        return new_arr
        
        
        
