class Solution:
    def countSubstrings(self, s: str) -> int:
        # def checkPalin(substr):
        #     if substr == substr[::-1]:
        #         return True
        #     return False
        # count = 0
        # for i in range(len(s)):
        #     for j in range(i+1,len(s)+1):
        #         if (s[i] != s[j-1]):
        #             continue
        #         if checkPalin(s[i:j]):
        #             count+=1
        # return count

        count = 0
        
        for i in range(len(s)):
            l=r = i
            while l>=0 and r<len(s) and s[l]==s[r]:
                count+=1
                l-=1
                r+=1
            l,r = i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                count+=1
                l-=1
                r+=1
            
        return count

