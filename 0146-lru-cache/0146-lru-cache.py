class Node:
    def __init__(self,key,val):
        self.key,self.val = key,val
        self.next,self.prev = None,None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.maps = {}
        self.left,self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self,node):
        prev,next = node.prev,node.next
        prev.next,next.prev = next,prev
        

    def insert(self,node):
        prev,next= self.right.prev,self.right
        prev.next,next.prev = node,node
        node.next = next
        node.prev = prev

    def get(self, key: int) -> int:
        if key in self.maps:
            self.remove(self.maps[key])
            self.insert(self.maps[key])
            return self.maps[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.maps:
            self.remove(self.maps[key])
        self.maps[key] = Node(key,value)
        self.insert(self.maps[key])

        if len(self.maps) > self.capacity:
            node = self.left.next
            del self.maps[node.key]
            self.remove(node)



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)