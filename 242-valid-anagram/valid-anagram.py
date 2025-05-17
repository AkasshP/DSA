class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            s_map = {}
            t_map = {}
            for i in s:
                if s_map.get(i):
                    s_map[i] = s_map[i] + 1
                else:
                    s_map[i] = 1
            print(s_map,'s_map')
            for i in t:
                if t_map.get(i):
                    t_map[i] = t_map[i] + 1
                else:
                    t_map[i] = 1
            print(t_map,'s_map')
            for key in s_map.keys():
                if t_map.get(key):
                    if s_map[key] == t_map[key]:
                        pass
                    else:
                        return False
                else:
                    return False
            return True
        else:
            return False