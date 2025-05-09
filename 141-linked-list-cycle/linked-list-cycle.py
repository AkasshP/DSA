# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #memory detection
        # current = head
        # mem = set()
        # while current is not None and current.next is not None:
        #     if current in mem:
        #         return True
        #     else:
        #         mem.add(current.next)
        #     current = current.next
        #     print(mem,'memory')
        # return False
        #two pointer
        if head is not None and head.next is not None:
            slow = head.next
            fast = head.next.next
            while fast and fast.next:
                if slow is fast:
                    return True
                if fast.next is not None:
                    slow = slow.next
                    fast = fast.next.next
          
        return False




        