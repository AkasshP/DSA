import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))

        pq = []
        final = defaultdict(list)
        heapq.heappush(pq,(0,src,0))
        cost_dict = {(src, 0): 0}
        while pq:
            cur_cost,u,stops  = heapq.heappop(pq)
            if u == dst and stops <= k+1:
                return cur_cost
            if stops > k:
                continue
            if u in graph:
                for v,w in graph[u]:
                    new_cost = cur_cost + w
                    if new_cost < cost_dict.get((v,stops+1),float('inf')):
                        cost_dict[(v, stops+1)] = new_cost
                        heapq.heappush(pq,(new_cost,v,stops+1))

        return -1
        