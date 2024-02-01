class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def dfs(i):
            if i>= len(nums):
                res.append(sub[:])
                return
            
            sub.append(nums[i])
            dfs(i+1)
            k = sub.pop()
            
            while i+1<len(nums) and nums[i] == nums[i+1]:
                i+=1
            dfs(i+1)

        res = []
        sub = []
        dfs(0)
        return res