class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        j=0
        for i in s:
            if j<len(t) and i==t[j]:
                j+=1
        return len(t) - j