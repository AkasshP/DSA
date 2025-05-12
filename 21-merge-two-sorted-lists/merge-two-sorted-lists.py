# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        Head = None
        #arranging all the node and then putting them into a list
        mergeList = []
        while True:
            if list1 and list2:
                if list1.val <= list2.val:
                    mergeList.append(list1)
                    list1 = list1.next
                else:
                    mergeList.append(list2)
                    list2 = list2.next
            else:
                if list1 is None and list2:
                    if list2.next is None:
                        mergeList.append(list2)
                        break
                    else:
                        mergeList.append(list2)
                        list2 = list2.next
                elif list2 is None and list1:
                    if list1.next is None:
                        mergeList.append(list1)
                        break
                    else:
                        mergeList.append(list1)
                        list1 = list1.next
                else:
                    break
        #reseting the memeory address
        for i in range(len(mergeList)):
                mergeList[i].next = None
        for i in range(len(mergeList)):
            if i + 1 < len(mergeList):
                mergeList[i].next = mergeList[i+1]
            else:
                mergeList[i].next = None
                break

        if not mergeList:
            return None
        else:
            node = mergeList[0]
            return node


