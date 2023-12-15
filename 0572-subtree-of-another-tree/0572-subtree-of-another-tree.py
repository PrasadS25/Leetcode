# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sametree(self,r1,r2):
        if r1 == r2 == None:
            return True
        if r1 == None or r2 == None:
            return False
        if r1.val != r2.val:
            return False
        if r1.val == r2.val:
            return self.sametree(r1.left,r2.left) and self.sametree(r1.right,r2.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root==None:
            return False
        if self.sametree(root,subRoot):
            return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)