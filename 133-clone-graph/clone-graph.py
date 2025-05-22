"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        g = node
        dq = deque()
        seen = set()
        clone={}
        if g:#checking intially the node is available or not
            dq.append(g)
            seen.add(g)
        while dq:
            for i in range(len(dq)):
                nodes = dq.popleft()
                for i in nodes.neighbors:
                    if clone.get(nodes.val):
                        clone[nodes.val] = clone[nodes.val] + [i.val]
                        if i not in seen:
                            dq.append(i)
                            seen.add(i)
                    else:
                        clone[nodes.val] = [i.val]
                        if i not in seen:
                            dq.append(i)
                            seen.add(i)
        #buidling a new graph
        if not clone:
            if node:
                print(node.val,'original',node.neighbors)
                g1 = Node(node.val)
                return g1
        else:
            temp = {}
            for keys in clone:
                g1 = Node(keys)
                temp[keys] = g1
            for k,v in clone.items():
                for i in v:
                    if not temp[k].neighbors:
                        temp[k].neighbors =  [temp[i]] #1 neighbour
                    else:
                        temp[k].neighbors = temp[k].neighbors + [temp[i]] # 2 neighbour
            if temp.get(1):
                sample = temp.get(1)
                return sample
        
                
            
        