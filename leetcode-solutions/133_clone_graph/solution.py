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
        if not node: return node

        queue = deque([node])
        clones = { node.val: Node(node.val, []) }

        while queue:
            curr_node = queue.popleft()
            curr_clone = clones[curr_node.val]

            for neighbor in curr_node.neighbors:
                if neighbor.val not in clones:
                    clones[neighbor.val] = Node(neighbor.val, [])
                    queue.append(neighbor)
                    
                curr_clone.neighbors.append(clones[neighbor.val])

        return clones[node.val]