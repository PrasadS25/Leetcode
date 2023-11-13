class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        newl = set(nums)
        maxc = 0
        for i in newl:
            if i-1 not in newl:
                c=1
                while i+1 in newl:
                    i+=1
                    c+=1
                maxc = max(maxc,c)
        return maxc