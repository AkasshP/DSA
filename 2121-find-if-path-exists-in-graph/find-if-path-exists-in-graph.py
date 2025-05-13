class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        #adjacency list
        nodes = {i: [] for i in range(n)}
        print(nodes)
        for u, v in edges:
            nodes[u].append(v)
            nodes[v].append(u)
        seen = set()
        def dfs(src,dest):
            print('src',src)
            if src == dest:
                return True
            val = nodes[src]
            for i in val:
                if i not in seen:
                    seen.add(i)
                    if dfs(i, dest): #dfs
                        return True
            return False
        ans = dfs(source,destination)
        return ans
        