class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        i = 0
        j = len(s)-1
        
        while i<j:
                if s[i]!=s[j]:
                    l = s[i+1:j+1]
                    r = s[i:j]

                    return (l==l[::-1]) or (r==r[::-1])
                        
                i+=1
                j-=1

        return True
