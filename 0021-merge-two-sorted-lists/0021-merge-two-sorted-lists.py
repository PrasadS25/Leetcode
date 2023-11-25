# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode()
        mergelist = temp
        
        while list1 and list2:
            if list1.val<=list2.val:
                mergelist.next = list1
                list1 = list1.next
            else:
                mergelist.next = list2
                list2 = list2.next
            mergelist = mergelist.next
        
        if list1:
            mergelist.next = list1
        elif list2:
            mergelist.next = list2
        return temp.next