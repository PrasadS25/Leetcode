class Solution:
    maxd =0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dia(node):
            if not node:
                return -1
            else:
                maxl = dia(node.left)
                maxr = dia(node.right)
                d = 2 + maxl + maxr
                self.maxd = max(d,self.maxd)
                return 1 + max(maxl,maxr)
        d = dia(root)
        return self.maxd