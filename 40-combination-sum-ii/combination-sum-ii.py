class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # visited = []
        # candidates.sort()
        # n = len(candidates)
        # suffix_sum = [0]*(n+1)
        # for idx in range(n-1, -1, -1):
        #     suffix_sum[idx] = candidates[idx] + suffix_sum[idx+1]

        # def combination(i,arr):
        #     if sum(arr) + suffix_sum[i] < target:
        #         return

        #     if sum(arr) == target and sorted(arr) not in visited:
        #         visited.append(sorted(arr))
        #         return 


        #     for j in range(i,len(candidates)):
        #         if candidates[j] + sum(arr) <= target:
        #             arr.append(candidates[j])
        #             combination(j+1,arr)
        #             arr.pop()

                
                    
                
        # for i in range(len(candidates)):
        #     if candidates[i] <= target:
        #         combination(i+1,[candidates[i]])
                
                
        # if not visited and sum(candidates[:1]) == target:
        #     return [[candidates[0]]]

        # return visited

        candidates.sort()
        results = []
        
        def backtrack(start,path,total):
            if total == target:
                results.append(path.copy())
                return
            if total > target:
                return
            
            prev = None
            for i in range(start, len(candidates)):
                c = candidates[i]
                # skip duplicates at this recursion depth
                if c == prev:
                    continue
                # if adding c would overshoot, break early (since array is sorted)
                if total + c > target:
                    break
                
                path.append(c)
                backtrack(i+1, path, total + c)
                path.pop()
                
                prev = c
        
        backtrack(0, [], 0)
        return results


