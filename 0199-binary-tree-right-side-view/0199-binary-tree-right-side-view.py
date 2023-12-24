class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        q = collections.deque()
        q.append(root)
        while q:
            l = len(q)
            for i in range(l):
                a = q.popleft()
                if a.left:
                    q.append(a.left)
                if a.right:
                    q.append(a.right)
            res.append(a.val)
        return res