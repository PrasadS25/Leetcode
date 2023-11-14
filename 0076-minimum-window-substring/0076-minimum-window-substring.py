class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t =="":
            return ""
        hash1 = {}
        hash2 = {}
        for i in t:
            hash1[i] = 1+hash1.get(i,0)
        need = len(hash1)
        have = 0
        out = []
        maxc = float("infinity")
        i = 0
        for j in range(len(s)):    
            if s[j] in hash1.keys():
                hash2[s[j]] = 1 + hash2.get(s[j],0)
                if hash2[s[j]] == hash1[s[j]]:
                    have += 1      
                    
            while have == need:
                if j-i+1 < maxc:
                    maxc = j-i+1
                    out = [i,j]   
                if s[i] in hash1.keys():
                    hash2[s[i]] -= 1
                    if hash2[s[i]] < hash1[s[i]]:
                        have -=1
                i += 1

        if maxc == float("infinity"):
            return ""
        l,r = out
        return s[l:r+1]