class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        sub = []
        def dfs(i):
            if i>=len(candidates) or sum(sub) > target:
                return
            elif sum(sub) == target:
                res.append(sub.copy())
                return
            sub.append(candidates[i])
            dfs(i)

            sub.pop()
            dfs(i+1)
            
        dfs(0)
        return res