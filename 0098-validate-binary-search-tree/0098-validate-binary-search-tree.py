# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def traverse(node,lis):
            if node:
                traverse(node.left,lis)
                lis.append(node.val)
                traverse(node.right,lis)
        lis = []
        traverse(root,lis)
        for i in range(len(lis)-1):
            if lis[i]>=lis[i+1]:
                return False
        return True