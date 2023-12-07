# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if len(lists) == 0:
            return None
        if len(lists)==1:
            return lists[0]
        k = len(lists)
        lis = []
        for head in lists:
          while head!=None:
            lis.append(head.val)
            head = head.next
        
        lis.sort()
        temp = ListNode()
        head = temp
        for n in lis:
          Node = ListNode(n)
          head.next = Node
          head = head.next

        return temp.next