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
        maps = {None : None}
        new = head
        while new:
            node = Node(new.val)
            maps[new] = node
            new = new.next
        new = head
        while new:
            node = maps[new]
            node.next = maps[new.next] 
            node.random = maps[new.random] 
            new = new.next
        
        return maps[head]