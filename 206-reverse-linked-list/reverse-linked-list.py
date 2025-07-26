# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def rev(node):
            if node is None or node.next is None:
                return node
            new_head = rev(node.next)
            node.next.next = node # eg, 4 4.next-> 5, then 5.next-> none but pointing 4
            node.next = None #break connection
            return new_head

        return rev(head)