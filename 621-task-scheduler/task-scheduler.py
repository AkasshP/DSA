from queue import PriorityQueue
from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # pq = PriorityQueue()
        # priorities_used = set()
        # T_schedule = {}
        # for i in tasks:
        #     if T_schedule.get(i):
        #         T_schedule[i] = T_schedule[i] + 1
        #     else:
        #         T_schedule[i] = 1
        
        # j = 1
        # idx = j
        # for i in sorted(T_schedule, key=lambda x: -T_schedule[x]):
        #     pq.put((idx, i))
        #     priorities_used.add(idx)
        #     T_schedule[i] -= 1
        #     while T_schedule[i] != 0:
        #         idx += 1 + n
        #         pq.put((idx,i))
        #         priorities_used.add(idx)
        #         T_schedule[i] -= 1
        #     if j not in priorities_used:
        #         idx = j
        #     while j in priorities_used:
        #         j += 1
        #     idx = j

        # cycle = []
        # while not pq.empty():
        #     cycle.append(pq.get())
        # print(cycle)
        # return cycle[-1][0]
        
        #greedy solution
        task_counts = Counter(tasks)
        max_freq = max(task_counts.values())

        max_count = sum(1 for task in task_counts if task_counts[task] == max_freq)

        part_count = max_freq - 1
        part_length = n + 1
        empty_slots = part_count * part_length + max_count

        return max(len(tasks), empty_slots)

