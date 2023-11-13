class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
         
        maps={}
        i,j = 0,1
        maps[nums[i]] = 1
        while j<len(nums):
            if abs(i-j) >k :
                del maps[nums[i]]
                i+=1
            
            if nums[j] in maps:
                return True
            else:
                maps[nums[j]] = 1
            j+=1
            
        return False

