import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjacency = {}
        for u, v, w in times:
            adjacency.setdefault(u, []).append((v, w))

        # print(adjacency,adjacency_wt)
        
        cost_dict = {k: 0}
        visited = set()                       # ← 1) visited set
        pq = []
        heapq.heappush(pq, (0, k))
        while pq:
                cur_cost, u = heapq.heappop(pq)
                if u in cost_dict:
                    if cur_cost > cost_dict[u]:
                        continue
                    if u in visited:
                        continue
                    visited.add(u)
                for i,j in adjacency.get(u, []): 
                    new_cost = cur_cost + j
                    if new_cost < cost_dict.get(i, float('inf')):
                        cost_dict[i] = new_cost
                        heapq.heappush(pq, (new_cost, i))

        # print(cost_dict,'cost_dict')
        if len(cost_dict) == n:
            return max(cost_dict.values()) #if all the nodes received the signal then you can return the maximum
        else:
            return -1 
            
                    
                        
                        
                        
        
                




        
        