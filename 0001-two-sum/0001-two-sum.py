class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        maps = {}
        for i,n in enumerate(nums):
            if target-n in maps:
                return [maps[target-n],i]
            else:
                maps[n] = i
