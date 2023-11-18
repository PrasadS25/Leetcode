class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in s:
            if i != "]":
                stack.append(i)
            else:
                strs = ""
                while stack[-1] != '[':
                    strs = stack.pop() + strs
                stack.pop()
                num = ""
                while stack and stack[-1] in ['0','1','2','3','4','5','6','7','8','9']:
                    num = stack.pop() + num
                    
                num = int(num)
                strs = strs * num
                stack.append(strs)
        stack = "".join(stack)
        return stack