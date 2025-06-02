class Solution:
    def isHappy(self, n: int) -> bool:
        happy = {}
        visited = set()
        def happyornot(n):
            s = str(n)
            if len(s) == 1:
                if s[0] == '1':
                    return True
                else:
                    if s[0] in visited:
                        return False
            
            if s not in visited:
                visited.add(s)
                l1 = [int(ch) for ch in s]
                value = sum(list(map(lambda x: happy.setdefault(x, x * x), l1)))
                print(visited)
                return happyornot(value)
            else:
                return False
                    
        return happyornot(n)
                