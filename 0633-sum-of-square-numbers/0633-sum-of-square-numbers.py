import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        squares = set()
        i=0
        j=int(math.sqrt(c))

        while i<=j:
            val = (i**2) + (j**2)
            if val == c:
                return True
            elif val<c:
                i+=1
            elif val>c:
                j-=1
        return False