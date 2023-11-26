# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #Finding size and solving method
        if head.next is None:
            head = None
            return head
        size = 0
        front = head
        while front:
            size+=1
            front = front.next
        pos = (size-n)+1
        prev = None
        front = head
        i = 1

        while i<pos and front:
            prev = front
            front = front.next
            i+=1
        if front and prev:
            prev.next = front.next
        elif front:
            head = front.next
        else:
            prev.next = None
        return head