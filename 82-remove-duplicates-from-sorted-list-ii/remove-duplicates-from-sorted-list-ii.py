# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        dupl = []
        prev = None
        while curr is not None:
            if prev:
                if prev.val == curr.val:
                    dupl.append(prev.val)
            prev = curr
            curr = curr.next

        duplicate = set(dupl)
        current = head
        prev = None
        Flag = False
        node_count = 0
        while current is not None:
            if current.val in duplicate:
                current = current.next
                Flag = True
                continue 
              

            if Flag:
                if prev:
                    prev.next = current
                    Flag = False
                else:
                    head = current
                    Flag = False
            prev = current
            current = current.next
            node_count += 1

        if node_count:
            if Flag:
                if prev:
                    prev.next =  None
                    return head
            else:
                return head
        else:
            head = None #since everyhting is skippable
            return head

        
            