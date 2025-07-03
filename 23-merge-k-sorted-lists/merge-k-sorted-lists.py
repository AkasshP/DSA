# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from itertools import chain
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

        final_result = []

        while any(main_arr):
            # build a list of (value, list_index) for each non-empty sublist
            candidates = [
            (sub[0].val, idx)
            for idx, sub in enumerate(main_arr)
            if sub
            ]
            # pick the smallest value and its originating index
            _, winner_idx = min(candidates, key=lambda x: x[0])
            # pop the head node and append it to your result
            node = main_arr[winner_idx].pop(0)
            final_result.append(node)


        for i in range(len(final_result)):
            if i + 1 < len(final_result):
                final_result[i].next = final_result[i+1]
            else:
                final_result[i].next = None

        #returning head       
        if final_result:
            return final_result[0]


        
            

        
       
       