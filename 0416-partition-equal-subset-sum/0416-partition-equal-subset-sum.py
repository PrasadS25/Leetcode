class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)/2
        if sum(nums)%2:
            return False
        dp = set()
        dp.add(0)
        for i in nums:
            nextdp = dp.copy()
            for j in dp:
                nextdp.add(j+i)
            dp = nextdp.copy()
            if target in dp:
                return True
        return target in dp 