class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # check= {}
        # counts=[0]*26
        # countt = [0]*26
        # for i in s:
        #     counts[ord(i)-ord('a')] += 1 
        # # check[tuple(counts)]= s
        # for j in t:   
        #     countt[ord(j)-ord('a')] += 1 
        # # check[tuple(countt)] = t
        # # if check[tuple(countt)]==check[tuple(counts)]:
        # #     return True
        # # return False
        # if countt == counts:
        #     return True
        # return False

        countS = {}
        countT = {}

        if len(s)!=len(t):
            return False
        
        for i in range(len(s)):
            countS[s[i]] = 1+countS.get(s[i],0)
            countT[t[i]] = 1+countT.get(t[i],0)
        return countT==countS
            