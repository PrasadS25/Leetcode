# class Solution:
#     def longestIdealString(self, s: str, k: int) -> int:
        
#         res = [0] * len(s)
#         if k>=26:
#             return s
#         for i in range(len(s)):
#             maxval = 0
#             cur = ord(s[i])
#             for j in range(i):
#                 if res[j] > maxval:
#                     if abs(ord(s[j])-cur) <=k:
#                         maxval = res[j]
#             res[i] = maxval+1

#         return max(res)
class Solution:
    def longestIdealString(self, s: str, k: int) -> int:


        l = [0] * 128
        for c in s:
            i = ord(c)
            l[i] = max(l[i - k : i + k + 1]) + 1
        return max(l)