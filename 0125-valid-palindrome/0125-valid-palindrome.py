class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        i=0
        j=len(s)-1
        while i<j:
            while not self.check(s[i]) and i<j:
                i+=1
            while not self.check(s[j]) and j > i:
                j-=1
            if s[i]!=s[j] :
                return False
            i+=1
            j-=1 
        return True

    def check(self,n):
        return (ord('a') <= ord(n) <= ord('z')) or (ord('0') <= ord(n) <= ord('9'))  