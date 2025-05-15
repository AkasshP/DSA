"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cur = head          # start at the real head
        index_map = {}     
        i = 0
        #insertion
        def insert(head, val):
            new_node = Node(val)
            if head is None:
                return new_node
            curr = head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node
            return head
        #mapping based on index
        def mapping(new_head,random_map):
            new_map={}
            j = 0
            cur = new_head
            while cur is not None:
                new_map[cur] = j
                cur = cur.next
                j += 1
            nodes_in_order = list(new_map.keys())
            curr = new_head
            while curr is not None:
                map_idx = new_map.get(curr,None)
                rand_index = random_map.get(map_idx,None)
                if rand_index is not None:
                    curr.random = nodes_in_order[rand_index]
                curr = curr.next
            return new_head
        #index_map
        while cur is not None:
            index_map[cur] = i
            i += 1
            cur = cur.next  
        
        new_head = None 
        ptr = head          
        random_map = {}     
        i = 0   
        #found the respective map          
        while ptr is not None:
            if ptr.random is not None:
                random_map[i] = index_map[ptr.random]
            new_head = insert(new_head,ptr.val)
            ptr = ptr.next   
            i += 1  

        curr = new_head
        final_head = mapping(curr,random_map)
        return final_head
        

            
                