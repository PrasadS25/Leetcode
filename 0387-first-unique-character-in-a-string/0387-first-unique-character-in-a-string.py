class Solution:
    def firstUniqChar(self, s: str) -> int:
        maps = {}
        res = -1
        for i in range(len(s)):
            if s[i] in maps.keys():
                maps[s[i]][0] += 1
            else:
                maps[s[i]] = [1,i]

        for i in range(len(s)):
            if maps[s[i]][0] == 1:
                res = maps[s[i]][1]
                break

        return res