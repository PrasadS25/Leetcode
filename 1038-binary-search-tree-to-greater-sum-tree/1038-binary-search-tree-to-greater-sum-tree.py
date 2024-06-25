# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        
        elems = []

        def inorder(root):
            if root:
                inorder(root.left)
                elems.append(root.val)
                inorder(root.right)
        
        inorder(root)
        for i in range(len(elems)-2,-1,-1):
            elems[i] += elems[i+1]
        print(elems)

        i=0
        def fix(root,elems,i):
            if root:
                i = fix(root.left,elems,i)
                root.val = elems[i]
                i+=1
                i = fix(root.right,elems,i)
                return i
            return i
        i = fix(root,elems,i)
        return root