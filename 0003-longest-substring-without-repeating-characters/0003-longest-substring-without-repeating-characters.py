class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        maps = set()
        maxc = 0
        i=0
        for j in range(len(s)):
            if s[j] in maps:
                while s[j] in maps:
                    maps.remove(s[i])
                    i+=1
            maps.add(s[j])
            maxc = max(j-i+1,maxc)
        return maxc