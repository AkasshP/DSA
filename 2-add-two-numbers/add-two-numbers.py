# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        current1,current2 = l1,l2
        dummy_head = ListNode(0)
        tail = dummy_head
        carry = 0
        current_balance = 0
        while current1 is not None and current2 is not None:
            total = current1.val + current2.val + carry
            carry = total // 10
            current_balance = total % 10
            tail.next = ListNode(current_balance)
            tail = tail.next
            
            current1 = current1.next
            current2 = current2.next

        while current1 and not current2:
            total = current1.val + carry
            carry = total // 10
            current_balance = total % 10
            
            tail.next = ListNode(current_balance)
            tail = tail.next
            
            current1 = current1.next

        while not current1 and current2:
            total = current2.val + carry
            carry = total // 10
            current_balance = total % 10
            
            tail.next = ListNode(current_balance)
            tail = tail.next
            
            current2 = current2.next

        if carry:
            tail.next = ListNode(carry)
        
        # Return the real head
        return dummy_head.next


        
