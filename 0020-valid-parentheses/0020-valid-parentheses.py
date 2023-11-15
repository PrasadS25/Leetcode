class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s) % 2 != 0:
            return False

        stack = []
        top = 0
        for i in s:
            if i == '(' or i == '[' or i =='{':
                stack.append(i)
                top += 1
            elif len(stack)>0:
                if i == ')' and stack[-1] =='(':
                    stack.pop()
                    top -=1
                elif i == '}' and stack[-1] == '{':
                    stack.pop()
                    top -=1
                elif i == ']' and stack[-1] == '[':
                    stack.pop()
                    top -= 1
                else:
                    stack.append(i)
                    top += 1
            else:
                return False

        return True if len(stack)==0 else False
        
         #using hashmaps
        # maps = {
        #     '}': '{',
        #     ')':'(',
        #     ']':'['
        # }
        
        # stack = []
        
        # for i in s:
        #     if i in maps.values():
        #         stack.append(i)
        #     elif len(stack)>0 and stack[-1] == maps[i]:
        #         stack.pop()
        #     else:
        #         return False
        # return True if len(stack)==0 else  False

       
