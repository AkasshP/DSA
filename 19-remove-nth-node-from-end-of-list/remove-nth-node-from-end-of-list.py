# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current = head
        count = 0
        temp = []
        temp.append(current)
        while current.next is not None:
            current = current.next
            temp.append(current)
        for i in temp:
            i.next = None
        if temp:
            temp.pop(-n)
        for i in range(len(temp)):
            if i + 1 < len(temp):
                temp[i].next  = temp[i + 1]
            else:
                temp[i].next = None
        if temp:
            return temp[0]

            