class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        visited = set()
        main_result = []
        def combination(nums,res,visited):
            if len(visited) == len(nums):
                main_result.append(res.copy())
                return 
            for i in nums: # 3 times should ocur
                if i in visited:
                    pass
                else:
                    res.append(i)
                    visited.add(i)
                    combination(nums,res,visited)
                    visited.remove(i)
                    res.pop()

        for i in nums:
            temp = []
            visited = set()
            temp.append(i)
            visited.add(i)
            combination(nums,temp,visited)
        return main_result