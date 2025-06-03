# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        temp = []
        while current is not None:
            temp.append(current)
            current = current.next
        for i in temp:
            i.next = None
        def merge(arr):
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            left = merge(arr[:mid])
            right = merge(arr[mid:])
            return merge_sort(left,right)
        def merge_sort(left, right):
            result = []
            i = j = 0
            while i < len(left) and j < len(right):  
                if left[i].val < right[j].val:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            result.extend(left[i:])
            result.extend(right[j:])
            return result
        res = merge(temp)
        for i in range(len(res)):
            if i + 1 < len(res):
                res[i].next = res[i+1]
            else:
                res[i].next = None
        if res:
            return res[0]
        
        

