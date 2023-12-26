# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        q = collections.deque()
        q.append(root)
        while q:
            l = len(q)
            for i in range(l):
                n = q.popleft()
                if n:
                    res.append(str(n.val))
                    q.append(n.left)
                    q.append(n.right)
                else:
                    res.append("N")

        return ",".join(res)
                

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        res = data.split(',')
        q = collections.deque()
        if res[0] == 'N':
            return None
        node = TreeNode(int(res[0]))
        q.append(node)
        i = 1
        count=0
        cur = TreeNode(0)
        temp = TreeNode(0)
        temp.left = node
        for i in range(1,len(res)):
            if res[i] != "N":
                node= TreeNode(int(res[i]))
                if count==0:
                    cur = q.popleft()
                    cur.left = node
                    count+=1
                else:
                    count-=1
                    cur.right=node
                q.append(node)
            else:
                if count==0:
                    cur = q.popleft()
                    count+=1
                else:
                    count-=1
        
        return temp.left







# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))