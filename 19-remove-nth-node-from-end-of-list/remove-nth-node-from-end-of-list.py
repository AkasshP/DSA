# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # current = head
        # count = 0
        # temp = []
        # temp.append(current)
        # while current.next is not None:
        #     current = current.next
        #     temp.append(current)
        # for i in temp:
        #     i.next = None
        # if temp:
        #     temp.pop(-n)
        # for i in range(len(temp)):
        #     if i + 1 < len(temp):
        #         temp[i].next  = temp[i + 1]
        #     else:
        #         temp[i].next = None
        # if temp:
        #     return temp[0]

        #two pointers
        current = head
        count = 0
        while current.next is not None:
            current = current.next
            count += 1
        node_count = count - n + 1

        curr = head
        count = 0

        if node_count == 0:
            return head.next
            
        while curr.next is not None:
            if node_count - 1  == count:
                temp = curr.next
                next_node = temp.next
                curr.next = next_node
                break
            curr = curr.next
            count +=  1
        return head


            