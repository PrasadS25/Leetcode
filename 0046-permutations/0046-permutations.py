class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        k = len(nums)
        def dfs(path,used):

            if len(path)==k:
                res.append(path[:])
                return
            
            for i in range(k):
                if used[i]:
                    continue
                path.append(nums[i])
                used[i] = True
                dfs(path,used)

                path.pop()
                used[i] = False  
        dfs([],[False]*k)
        return res