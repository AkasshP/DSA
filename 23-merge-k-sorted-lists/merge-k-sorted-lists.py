# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        main_arr = []
        for i in lists:
            current = i
            Temp_arr = []
            while current is not None:
                Temp_arr.append(current)
                current = current.next
            main_arr.append(Temp_arr)

        for i in main_arr:
            for j in i:
                j.next = None

        heap = []

        for idx, sub in enumerate(main_arr):
            if sub:
                heap.append((sub[0].val, idx))
        heapq.heapify(heap)

        final_result = []
        while heap:
            val, i = heapq.heappop(heap)
            node = main_arr[i].pop(0)   
            final_result.append(node)
            if main_arr[i]:
                heapq.heappush(heap, (main_arr[i][0].val, i))

        for i in range(len(final_result)):
            if i + 1 < len(final_result):
                final_result[i].next = final_result[i+1]
            else:
                final_result[i].next = None

        #returning head       
        if final_result:
            return final_result[0]


        
            

        
       
       