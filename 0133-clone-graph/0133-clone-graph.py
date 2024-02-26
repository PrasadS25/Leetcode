"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        maps = {}

        def clone(node):
            if node in maps:
                return maps[node]

            temp = Node(node.val)
            maps[node] = temp
            for neighbor in node.neighbors:
                temp.neighbors.append(clone(neighbor))
            
            return temp

        return clone(node) if node else None