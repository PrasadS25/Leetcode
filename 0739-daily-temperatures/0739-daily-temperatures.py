class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = []
        for i,n in enumerate(temperatures):
            while len(stack)>0 and n>stack[-1][0]:
                m,j = stack.pop()
                res[j] = i-j
            stack.append([n,i])
        return res