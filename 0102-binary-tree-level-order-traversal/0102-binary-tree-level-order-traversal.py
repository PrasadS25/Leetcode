# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        queue = collections.deque()
        queue.append(root)

        while queue:
            store= []
            l = len(queue)
            for i in range(l):
                a = queue.popleft()
                if a:
                    store.append(a.val)
                    queue.append(a.left)
                    queue.append(a.right)
            if store:
                res.append(store)
        return res