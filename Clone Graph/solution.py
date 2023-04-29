"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        stack=[]
        stack.append(node)
        mapping={}
        while len(stack)>0:
            current=stack.pop()
            if current.val not in mapping:
                mapping[current.val]=Node(current.val)
            if current.neighbors!=[]:
                for neighbor in current.neighbors:
                    if neighbor.val not in mapping:
                        mapping[neighbor.val]=Node(neighbor.val)
                        stack.append(neighbor)
                    mapping[current.val].neighbors.append(mapping[neighbor.val])
        return mapping[node.val]
