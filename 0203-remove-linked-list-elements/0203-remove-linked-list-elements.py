class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        #create a dummy node at the start so that we can return the head easily at the end
        temp = ListNode()
        temp.next= head
        first = temp.next
        prev = temp
        #keep a front and prev, when we find a node to remove we update the prev node's next to frist's next else we update the prev to current node.
        while first:
            if first.val == val:
                prev.next = first.next
            else:
                prev = first

            first = first.next
        
        return temp.next