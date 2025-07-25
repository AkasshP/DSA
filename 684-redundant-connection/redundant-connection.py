class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adjacency = {}
        n = len(edges)
        
        # Build undirected graph
        for i, j in edges:
            adjacency.setdefault(i, []).append(j)
            adjacency.setdefault(j, []).append(i)
        
        def remove(k, v):
            if k in adjacency and v in adjacency[k]:
                adjacency[k].remove(v)
                if not adjacency[k]:
                    del adjacency[k]
        
        def add(k, v):
            adjacency.setdefault(k, []).append(v)
        
        def dfs(node, parent):
            visited.add(node)
            
            if node in adjacency:
                for neighbor in adjacency[node]:
                    if neighbor not in visited:
                        if dfs(neighbor, node):
                            return True  # Cycle found
                    elif neighbor != parent:
                        # Back edge found (cycle)
                        return True
            
            return False
        
        # Try removing edges from last to first
        for k in range(n-1, -1, -1):
            i, j = edges[k]
            
            # Remove edge (both directions)
            remove(i, j)
            remove(j, i)
            
            # Reset visited and check for cycle
            visited = set()
            
            # Start DFS from any existing node
            if adjacency:
                start = next(iter(adjacency))
                has_cycle = dfs(start, -1)
                
                # If no cycle and all nodes visited
                total_nodes = len(set(x for edge in edges for x in edge))
                if not has_cycle and len(visited) == total_nodes:
                    return [i, j]
            
            # Add edge back
            add(i, j)
            add(j, i)
        
        return []