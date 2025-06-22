# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        arr = []
        current = head
        while current is not None:
            arr.append(current)
            current = current.next
        # print(arr,'arr')
        for i in arr:
            i.next = None
        # print(arr,'chekcing')
        mid = len(arr) // 2
        left = deque(arr[:mid])
        right = deque(arr[mid:])
        new_linked_list = []

        while left or right:
            if left:
                new_linked_list.append(left.popleft())  
            if right:
                new_linked_list.append(right.pop())

        for a, b in zip(new_linked_list, new_linked_list[1:]):
            a.next = b
        new_linked_list[-1].next = None

        