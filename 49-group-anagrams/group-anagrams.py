from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map_char= {}
        map_idx = {}

        for i in range(len(strs)):
            map_char.clear()
            for j in strs[i]:
                map_char[j] = map_char.get(j, 0) + 1
            map_idx[i] = map_char.copy()
        
        print(map_idx,'map_idx')

        if all(not value for value in map_idx.values()):
            return [strs]
        else:
            group  = []
            temp_group = []
            for i in sorted(map_idx):
                j = i + 1
                temp_group.clear()
                if i in map_idx:
                    while j < len(strs):
                        if j in map_idx:
                            if map_idx[i] == map_idx[j]:
                                temp_group.append(strs[j])
                                del map_idx[j]
                        j += 1
                    temp_group.append(strs[i])
                    del map_idx[i]

                if temp_group:
                    group.append(temp_group.copy())
            return group
        
        
