# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp = ListNode()
        temp.next= head
        slow = head
        fast = head
        #go till mid of list
        while fast:
            slow = slow.next
            fast = fast.next
            if fast != None:
                fast = fast.next
        prev = None
        #now reverse the links after mid
        while slow != None:
            tm = slow
            slow = slow.next
            tm.next = prev
            prev = tm
        #with a pointer at the left and right keep checking if they are same, else return false as it can't be a palindrome
        right = prev
        left= head
        
        while right:
            if left.val == right.val:
                left= left.next
                right = right.next
            else:
                return False
        return True