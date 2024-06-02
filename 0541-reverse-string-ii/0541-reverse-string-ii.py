class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        st = [a for a in s]
        for n in range(0,len(st),2*k):
            i = n
            j = min(n+k-1,len(st)-1)
            while i<j:
                tmp = st[i]
                st[i] = st[j]
                st[j] = tmp
                i+=1
                j-=1
            n+= 2 * k
        return "".join(st)