# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        current = head
        prev_node = None
        new_node = None
        first_node = None
        last_node = None
        cnt = 1
        dummy = ListNode(0)
        Main_head = dummy
        
        if left == right:
            return head

        if left <= right:
            dummy = ListNode(0)
            Main_head = dummy
            flag = False
            while current is not None:
                if cnt == left:
                    flag = True
                    prev_node = dummy 
                    first_node = current
        
                if cnt == right:
                    last_node = current
                    new_node = current.next

                if not flag:
                    dummy.next = current
                    dummy = dummy.next

                current = current.next
                cnt += 1

            
            curr = first_node
            prev = None
            cnt = 0
            while cnt != (right - left) + 1: 
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
                cnt += 1


            if Main_head.next is None:
                first_node.next = new_node
                return prev
            else:
                first_node.next = new_node
                dummy.next = prev
                return Main_head.next
            





        