class Solution:
    maxs = float('-inf')
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def sum(node):
            l=0 
            r=0

            if node.left:
                l = sum(node.left)
            if node.right:
                r = sum(node.right)
            l = max(0,l)
            r= max(0,r)
            res = l + r + node.val
            self.maxs = max(self.maxs,res)
            maxlr = max(l,r)
            
            return maxlr+node.val

        a = sum(root) 
        return max(a,self.maxs)