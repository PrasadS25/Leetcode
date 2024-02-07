import numpy as np
class Solution:
    def frequencySort(self, s: str) -> str:
        # maps = {}

        # for i in s:
        #     maps[i] = maps.get(i,0)+1

        # sorted_ind = sorted(maps.items(), key = lambda x:x[1], reverse=True)
        # sorted_ind = dict(sorted_ind)

        # res = ""
        # for key,val in sorted_ind.items():
        #     res += key*val
            
        # return res

        #2
        maps = {}
        res = ""
        for i in s:
            maps[i] = maps.get(i,0)+1
        lis = {}
        for k,v in maps.items():
            lis[v] = lis.get(v,[])+[k]
        for i in range((len(s)),-1,-1):
            if i in lis.keys():
                for k in lis[i]:
                    res += i*k
        
        return res


