class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dicti = set()
        for num in nums:  
            if num in dicti:
                return True
            dicti.add(num)
        return False