class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        sub = []
        candidates.sort()
        def dfs(i):
            if sum(sub)>target:
                return
            if sum(sub)==target:
                res.append(sub[::])
                return
            prev = -1
            for k in range(i,len(candidates)):
                if candidates[k]==prev:
                    continue
                sub.append(candidates[k])
                dfs(k+1)
                sub.pop()
                prev = candidates[k]

        dfs(0)
        return res