class Solution:
    def characterReplacement(self, s: str, k: int) -> int:   
        i = 0
        maxc = 0
        count= {}
        maxval = 0
        for j in range(len(s)):
            count[s[j]] = 1 + count.get(s[j], 0 )
            maxval = max(maxval, count[s[j]])
            while ((j-i+1) - maxval) > k:
                count[s[i]] -= 1
                i+=1
            maxc = max(maxc, j-i+1)
        return maxc