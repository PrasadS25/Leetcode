class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        maps = {0:1}
        count = 0
        prefixsum = 0
        for i in range(len(nums)):
            prefixsum = (prefixsum+nums[i])%k
            if prefixsum in maps:
                count+= maps[prefixsum]
                maps[prefixsum] += 1    
            else:
                maps[prefixsum] = 1
        return count