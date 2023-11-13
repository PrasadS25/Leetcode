import numpy as np
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        maps = {}
        store = [[] for i in range(len(nums)+1)] 

        for i in nums:
            if maps.get(i):
                maps[i] += 1
            else:
                maps[i] = 1

        for i,j in maps.items():    
            store[j].append(i)

        result =[]

        for i in range((len(store)-1), 0, -1):
            for j in store[i]:
                result.append(j)
                if len(result)==k:
                    return result
        