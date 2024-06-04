class Solution:
    def longestPalindrome(self, s: str) -> int:
        maps = {}
        for i in s:
            if i not in maps:
                maps[i] = 1
            else:
                maps[i] += 1
        odd = 1
        total = 0
        for i in maps.values():
            if i%2==1:
                if odd ==1:
                    total+=i
                    odd -=1
                else:
                    total+=i-1    
            elif i%2 == 0:
                total += i
        return total